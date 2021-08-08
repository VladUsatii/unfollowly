#!/usr/bin/env python3
# test file for this new module i've never used before
import instaloader

l = instaloader.Instaloader()
l.login('', '') # username and password
profile = instaloader.Profile.from_username(l.context, '') # username goes in the ''`s
follow_list = []
count = 0
for f in profile.get_followers():
	follow_list.append(f.username)
	count += 1
print(follow_list, count)
