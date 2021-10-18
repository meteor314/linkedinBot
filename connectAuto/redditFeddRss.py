import praw
from requests import Session
import urllib
import time
import random
import requests
import os
import glob


SUBREDDIT_TO_MONITOR = 'meme'
IMAGE_DIR = 'images'
session = Session()
session.verify = "/path/to/certfile.pem"
POSTED_CACHE = 'posted.ini'

Reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="testscript by u/meteor314"
)
"""
for submission  in reddit.subreddit('space').hot(limit=11):
    print(submission.title)
    #print( submission.description)
    print('=======================')
"""


def setup_connection_reddit(subreddit):
    ''' Creates a connection to the reddit API. '''
    print('[bot] Setting up connection with reddit')
    reddit_api = praw.Reddit(format(subreddit))
    return reddit_api.get_subreddit(subreddit)

def get_image(img_url):
    ''' Downloads i.imgur.com images that reddit posts may point to. '''
    if 'imgur.com' in img_url:
        file_name = os.path.basename(urllib.parse.urlsplit(img_url).path)
        img_path = IMAGE_DIR + '/' + file_name
        print('[bot] Downloading image at URL ' + img_url + ' to ' + img_path)
        resp = requests.get(img_url, stream=True)
        if resp.status_code == 200:
            with open(img_path, 'wb') as image_file:
                for chunk in resp:
                    image_file.write(chunk)
            # Return the path of the image, which is always the same since we just overwrite images
            return img_path
        else:
            print('[bot] Image failed to download. Status code: ' + resp.status_code) #200 || 404
    else:
        print('[bot] Post doesn\'t point to an i.imgur.com link')
    return ''




def main():
    ''' Runs through the bot posting routine once. '''
    # If the tweet tracking file does not already exist, create it
    if not os.path.exists(POSTED_CACHE):
        with open(POSTED_CACHE, 'w'):
            pass
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    subreddit = setup_connection_reddit(SUBREDDIT_TO_MONITOR)


    # Clean out the image cache
    for filename in glob(IMAGE_DIR + '/*'):
        os.remove(filename)

if __name__ == '__main__':
    main()