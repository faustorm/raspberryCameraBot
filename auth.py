from requests_oauthlib import OAuth1Session

CONSUMER_KEY = 'b75xPpzpsdnjf08Yo340mHvbF';
CONSUMER_SECRET = 'N0zOqUzGePVHEu3pJ1OMs1XqWVdhG2bn0lzaaYzpziNQmZXKZb';

consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET

def get_resource_token():
    #create an object of OAuth1Session    
    request_token = OAuth1Session(client_key=consumer_key,                     client_secret=consumer_secret)
    # twitter endpoint to get request token
    url = 'https://api.twitter.com/oauth/request_token'
    # get request_token_key, request_token_secret and other details
    data = request_token.get(url)
    # split the string to get relevant data 
    data_token = str.split(data.text, '&')
    ro_key = str.split(data_token[0], '=')
    ro_secret = str.split(data_token[1], '=')
    resource_owner_key = ro_key[1]
    resource_owner_secret = ro_secret[1]
    resource = [resource_owner_key, resource_owner_secret]
    return resource
