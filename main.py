"""
Sends alart to Reddit account when there is a new post on 
/r/dailyprogrammer

Python 3
"""

import praw
import time

user_agent = 'sends /u/user an alert for new posts in /r/dailyprogramming'

r = praw.Reddit(user_agent=user_agent)
r.login()
already_sent = []

while True:
	subreddit = r.get_subreddit('dailyprogrammer')
	for submission in subreddit.get_new(limit=10):
		if submission.id not in already_sent:
			msg = '[New Daily Programmer Post!]({0})'.format(submission.short_link)
			r.send_message('','Daily Programming Challenge',msg)
			already_sent.append(submission.id)
	time.sleep(3600)



