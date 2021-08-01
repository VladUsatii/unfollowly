from selenium import webdriver

class Grab(object):
	def __init__(self):
		# open chrome headless
		op = webdriver.ChromeOptions()
		op.add_argument('headless')
		self.driver = webdriver.Chrome(options=op)
	def print(self, user) -> str:
		driver = self.driver
		driver.maximize_window()
		driver.get(f"https://www.instagram.com/{user}/")
		return str(driver.page_source)

grab = Grab().print("vladusatii_")

from unfollowly import app
from flask import Flask, render_template

@app.route('/')
def index(info: str):
	return render_template('index.html', info=grab)


"""
TODO:
  - Figure out how to render the output into a variable passed to HTML via werkzeug's url_for()
"""
