from flask import Flask
app = Flask(__name__)

import unfollowly.views


if __name__ == '__main__':
	print(app)
