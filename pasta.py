'''
scrape reddit for copypastas
main function that returns a string which is the body of the pasta post
Personal Use Script: o35oRrqg7LhJ-g
Secret: IE0i671J3ZYR80XprXD7X2TBdOw
'''

#! usr/bin/env python3
import praw
import random 
import os

source_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(source_path,'keychain','redditkey.txt')) as file:
    keys = file.read().split('\n')

reddit = praw.Reddit(client_id=keys[0],client_secret=keys[1],user_agent=keys[2],username=keys[3],password=keys[4])
print(f'Logged into reddit as: {reddit.user.me()}')

pasta = reddit.subreddit('copypasta').hot(limit=100)

pastaList = []

for submission in pasta:
    pastaList.append(submission)

def getPasta():
    post = random.choice(pastaList)
    return post.selftext
