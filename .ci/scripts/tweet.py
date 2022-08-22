import os
import sys
from tweepy import Client

release_version = sys.argv[1]
client = Client(
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_KEY_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
)
link = "https://docs.pulpproject.org/pulp_ansible/changes.html"
msg = f"pulp_ansible-{release_version} - Check out for more details: {link}"
release_msg = f"Hey! We've just released {msg}"
client.create_tweet(text=release_msg)
