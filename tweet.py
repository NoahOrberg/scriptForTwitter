#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import json
import sys

cmdParams= sys.argv
f= open('OAuth_key.json', 'r')
oauthKeyDict= json.load(f)
f.close()
twUrl= "https://api.twitter.com/1.1/statuses/update.json"
params= {"status": cmdParams[1]}
twTweet= OAuth1Session(oauthKeyDict[u"consumer_key"], oauthKeyDict[u"consumer_secret"], oauthKeyDict[u"access_token"], oauthKeyDict[u"access_token_secret"])
req= twTweet.post(twUrl, params = params)
if req.status_code!= 200: print ("ERR: %d" % req.status_code)
