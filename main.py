import requests
from requests_oauthlib import OAuth1
import os

consumer_key = 'b75xPpzpsdnjf08Yo340mHvbF';
consumer_secret = 'N0zOqUzGePVHEu3pJ1OMs1XqWVdhG2bn0lzaaYzpziNQmZXKZb';
access_token = 'WEVTSF9yMjVSN3E1dUFzczRvd1o6MTpjaQ';
access_token_secret = 'Xca2MTzVlu0eelGKfmicaw2r8R4U17MDBlyYuZH_kOqnkohAVy';

def random_fact():
    fact = requests.get("https://catfact.ninja/fact?max_length=280").json()
    return fact["fact"]


def format_fact(fact):
   return {"text": "{}".format(fact)}

def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
   url = "https://api.twitter.com/2/tweets"
   auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
   return url, auth


def hello_pubsub(event, context):
   fact = random_fact()
   payload = format_fact(fact)
   url, auth = connect_to_oauth(
       consumer_key, consumer_secret, access_token, access_token_secret
   )
   request = requests.post(
       auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
   )
