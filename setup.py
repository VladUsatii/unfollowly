from setuptools import setup

setup(
	name='unfollowly',
	packages=['unfollowly'],
	include_package_data=True,
	install_requires=[
		'flask',
		'selenium',
		'instaloader',
	],
)
