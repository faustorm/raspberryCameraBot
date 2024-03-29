#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2018 The Python-Twitter Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utility to get your access tokens."""

from __future__ import print_function

from requests_oauthlib import OAuth1Session
import webbrowser

import sys

if sys.version_info.major < 3:
    input = raw_input

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'


def get_access_token(consumer_key, consumer_secret):
    """Get an access token for a given consumer key and secret.
    Args:
        consumer_key (str):
            Your application consumer key.
        consumer_secret (str):
            Your application consumer secret.
    Returns:
        (None) Prints to command line.
    """
    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret, callback_uri='oob')

    print('\nRequesting temp token from Twitter...\n')

    resp = oauth_client.fetch_request_token(REQUEST_TOKEN_URL)

    url = oauth_client.authorization_url(AUTHORIZATION_URL)

    print('I will try to start a browser to visit the following Twitter page '
          'if a browser will not start, copy the URL to your browser '
          'and retrieve the pincode to be used '
          'in the next step to obtaining an Authentication Token: \n'
          '\n\t{0}'.format(url))

    webbrowser.open(url)
    pincode = input('\nEnter your pincode? ')

    print('\nGenerating and signing request for an access token...\n')

    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret,
                                 resource_owner_key=resp.get('oauth_token'),
                                 resource_owner_secret=resp.get('oauth_token_secret'),
                                 verifier=pincode)
    try:
        resp = oauth_client.fetch_access_token(ACCESS_TOKEN_URL)
    except ValueError as e:
        raise 'Invalid response from Twitter requesting temp token: {0}'.format(e)

    print('''Your tokens/keys are as follows:
        consumer_key         = {ck}
        consumer_secret      = {cs}
        access_token_key     = {atk}
        access_token_secret  = {ats}'''.format(
            ck=consumer_key,
            cs=consumer_secret,
            atk=resp.get('oauth_token'),
            ats=resp.get('oauth_token_secret')))


def main():
    """Run script to get access token and secret for given app."""
    

    CONSUMER_KEY = 'b75xPpzpsdnjf08Yo340mHvbF';
    CONSUMER_SECRET = 'N0zOqUzGePVHEu3pJ1OMs1XqWVdhG2bn0lzaaYzpziNQmZXKZb';

    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    get_access_token(consumer_key, consumer_secret)


if __name__ == "__main__":
    main()
