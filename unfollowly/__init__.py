from flask import Flask
from flask_apscheduler import APScheduler

app = Flask(__name__)

import unfollowly.views

if __name__ == '__main__':
	print(app)
