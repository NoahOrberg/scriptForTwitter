#!/usr/bin/env python
# -*- coding:utf-8 -*-
from requests_oauthlib import OAuth1Session
import json
import sys
import codecs
sys.stdout= codecs.getwriter("utf-8")(sys.stdout)
maxId= ""
cmdParams= sys.argv
f= open("OAuth_key.json","r")
oauthKeyDict= json.load(f)
f.close()

def tweetSearch(searchWord, maxId):#{{{
    twUrl= "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params= {
        "screen_name": searchWord,
        "count": 200,
    }
    if maxId!= "":
        maxid= int(maxId)
        params.update({
            "max_id": maxid - 1
        })
    twTimeLine= OAuth1Session(oauthKeyDict["consumer_key"],oauthKeyDict["consumer_secret"],oauthKeyDict["access_token"],oauthKeyDict["access_token_secret"])
    req= twTimeLine.get(twUrl, params= params)
    if req.status_code!= 200:
        print "Err: %d" %(req.status_code)
    tweets= json.loads(req.text)
    return tweets#}}}
#--------------------------------------
def main():#{{{
    while 1:
        tweets= tweetSearch(cmdParams[1].decode("utf-8"), maxId)
        if len(tweets)==0:
            break
        for tweet in tweets:
            global maxId
            maxId= tweet[u"id_str"]
            screenName= tweet[u"user"][u"screen_name"]
            print "userId:", screenName
            userName= tweet[u"user"][u"name"]
            print "userName:", userName
            userDescription= tweet[u"user"][u"description"]
            print "userDesc:", userDescription
            text= tweet[u"text"]
            print "text:", text
            createdAt= tweet[u"created_at"]
            print "Date:", createdAt
            print "-----****************************************************************-----"
    return#}}}

if __name__== "__main__":
    main()
