import sys, os, subprocess
from unfollowly import app
from flask import Flask, render_template, url_for
import instaloader
from pathlib import Path

# pwd
cwd = os.getcwd()


class Grab(object):
	def __init__(self):
		# open chrome headless
		# self.op = webdriver.ChromeOptions()
		# self.op.add_argument('headless')
		# self.driver = webdriver.Chrome(options=self.op)

		self.L = instaloader.Instaloader()

	def followers(self, username, password) -> str:
		self.L.login(username, password)
		profile = instaloader.Profile.from_username(self.L.context, username)
		followers = ''
		for follower in profile.get_followers():
			followers = f'{followers}{follower.username} '
		return followers

	def profile_picture(self, username: str):
		# check cache
		if Path(f'{cwd}/unfollowly/static/pp.jpg').is_file():
			pass
		else:
			self.L.download_profile(username, profile_pic_only=True)
			subprocess.run(['bash', 'renderProfile.sh', f'{username}'])

	def get_followers(self, username: str, password: str) -> str:
		# login (risky operation)
		self.L.login(username, password)
		profile = instaloader.Profile.from_username(self.L.context, username)

		follow_list = []
		count = 0

		for followee in profile.get_followers():
			follow_list.append(followee.username)
			count += 1
		followers = count
		return [followers, follow_list]

name = ''
password = ''

grab = Grab()
pp = grab.profile_picture(name)

gf = grab.get_followers(name, password)
followers = str(gf[0])
follow_list = gf[1]

@app.route('/')
def index():
	return render_template('index.html', profilename=name, followers=followers, follow_list=follow_list)

