try:
	from setuptools import setuptools
except ImportError:
	from distutils.core import setup

config = {
	'description': 'MyProject',
	'author': 'GBryson',
	'url': 'url to get it at',
	'download url': 'where to download it',
	'author email': 'giuliabryson@protonmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'

}

setup(**config)