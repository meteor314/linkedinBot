const { Client } = require('linkedin-private-api');

const COUNTRY_CODE = ''; // your code
const NETORK_TYPE = '';

const wait = seconds => new Promise(res => setTimeout(res, seconds * 1000));

// ID to connect on linkedin
const USERNAME = 'ghj';  // your name
const PASSWORD = 'yghjkl'; //your linkedin passowrd

const buildMessage = profile => `
Hello 
Thhis message is send via nodejs bot. Thank you for connecting !
HAve a good day :)
`;

const Invites = async (client, companyIds) => {
  const peopleScroller = client.search.searchPeople({
    filters: {
      currentCompany: companyIds,
      geoUrn: COUNTRY_CODE,
      network: NETORK_TYPE,
    },
  });

  let searchHits;
  let counter = 0;

  while ((searchHits = await peopleScroller.scrollNext()) && searchHits.length) {
    for (const searchHit of searchHits) {
      const { profile } = searchHit;

      await client.invitation.Invite({
        profileId: profile.profileId,
        trackingId: profile.trackingId,
      });

      await wait(3);
    }
    if (counter === 3) {
      counter = 0;
      await wait(1800);
    } else {
      counter += 1;
      await wait(10);
    }
  }

  console.log('Finished processing all search results!');
};

const sendMessages = async (client, companyIds) => {
  const connectionsScroller = client.search.searchOwnConnections({
    filters: {
      currentCompany: companyIds,
      geoUrn: COUNTRY_CODE,
    },
  });

  let connections;
  let counter = 0;

  while ((connections = await connectionsScroller.scrollNext()) && connections.length) {
    for (const connection of connections) {
      const { profile } = connection;

      const [conversation] = await client
        .conversation
        .getConversations({
          recipients: profile.profileId,
        })
        .scrollNext();

      if (!conversation) {
        const message = buildMessage(profile);

        await client.message.sendMessage({
          profileId: profile.profileId,
          text: message,
        });

        counter += 1;
        await wait(5);
      }
    }

    if (counter === 30) {
      counter = 0;
      await wait(1800);
    } else {
      await wait(10);
    }
  }

  console.log('Finished processing all connections!');
};

(async () => {
  const client = new Client();
  await client.login.userPass({ username: USERNAME, password: PASSWORD });

  const [[{ company: google }], [{ company: microsoft }], [{ company: facebook }], [{ company: linkedin }]] = await Promise.all([
    client.search.searchCompanies({ keywords: 'Google' }).scrollNext(),
    client.search.searchCompanies({ keywords: 'Microsoft' }).scrollNext(),
    client.search.searchCompanies({ keywords: 'Facebook' }).scrollNext(),
    client.search.searchCompanies({ keywords: 'LinkedIn' }).scrollNext(),
  ]);

  const companyIds = [google.companyId, microsoft.companyId, facebook.companyId, linkedin.companyId];

  Invites(client, companyIds);
  setInterval(() => {
    sendMessages(client, companyIds);
  }, 14400000);
})();