import os
from setuptools import setup, find_packages
from distutils.core import setup

# Utility function to read the README file.

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "geoLid",
	version = "1.0",
	author = "Jonathan Dunn",
	author_email = "jedunn@illinois.edu",
	description = ("Geographically-informed language identification"),
	license = "GNU GENERAL PUBLIC LICENSE v3",
	url = "https://github.com/jonathandunn/geoLid",
	keywords = "lid, language identification, geographic, geography",
	packages = find_packages(exclude=["*.pyc", "__pycache__"]),
	install_requires=["clean-text",
						"fasttext",
						],
	long_description=read('README.md'),
    long_description_content_type='text/markdown',
	)
