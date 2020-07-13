#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='hdfsbrowser',
<<<<<<< HEAD
      version='1.1.1',
=======
      version='0.0.11',
>>>>>>> e422455e4b77a57bea93a4478d0d645476751606
      description='HDFS Browser Extension for Jupyter Notebook',
      author='Prasanth Kothuri',
      author_email='prasanth_kothuri@hotmail.com',
      url='https://github.com/prasanthkothuri/hdfsbrowser',
      include_package_data=True,
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          'bs4'
      ],
      )
