const {Client} = require('linkedin-private-api');
(async () => {
    const client  = new Client();
    await client.login.userPass({
        username : 'meteor3141592@gmail.com',
        password : '*$m&8^^%S465' // change with your current password
    })
})