from setuptools import setup, find_packages
import sys
import os

wd = os.path.dirname(os.path.abspath(__file__))
os.chdir(wd)
sys.path.insert(1, wd)

name = 'easy_gar'
author = 'David Amos'
email = 'somacdivad@gmail.com'
version = '1.0.0'
classifiers = [
    'Programming Language :: Python :: 3.6',
]
copyright = "2018, %s " % author
license = "MIT"

readme = open(os.path.join(wd, 'README.md'), 'r').readlines()
description = readme[1]
long_description = ''.join(readme)

reqs = ['google-api-python-client==1.6.7', 'pandas==0.23.0']

if sys.version_info < (3, 6):
    raise ImportError("Python 3.6+ required.")

install_requires = ['google-api-python-client==1.6.7', 'pandas==0.23.0']

setup(
    name=name,
    version=version,
    author=author,
    author_email=email,
    url='https://github.com/somacdivad/easy-ga-reporting',
    maintainer=author,
    maintainer_email=email,
    description=description,
    long_description=long_description,
    classifiers=classifiers,
    install_requires=reqs,
    packages=find_packages(),
    license=license,
    keywords='easyGAR, easy-ga-reporting',
)
