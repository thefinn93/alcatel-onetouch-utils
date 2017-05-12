#!/usr/bin/env python
from distutils.core import setup

setup(name='alcatel-onetouch-utils',
      version='0.1.0',
      description='Utilities for interacting with Alcatel OneTouch devices',
      author='Finn Herzfeld',
      author_email='finn@finn.io',
      url='https://github.com/thefinn93/alcatel-onetouch-utils',
      packages=['onetouch'],
      install_requires=["requests>=2"],
      entry_points={'console_scripts': ['onetouch = onetouch.cli:main']})
