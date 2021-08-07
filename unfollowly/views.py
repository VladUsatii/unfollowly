import sys, os, subprocess
from unfollowly import app
from flask import Flask, render_template, url_for
import instaloader

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
		self.L.download_profile(username, profile_pic_only=True)
		subprocess.run(['bash', 'renderProfile.sh', f'{username}'])

grab = Grab()
pp = grab.profile_picture('vladusatii_')


@app.route('/')
def index():
	# return render_template('index.html', info=grab.followers('vladusatii_', 'fhrg79h3nu9fnr3uj0odsfj@FHJUER(FHNSD')) # high risk operation, can get banned
	return render_template('index.html')

