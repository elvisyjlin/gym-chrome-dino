#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Elvis Yu-Jing Lin <elvisyjlin@gmail.com>
# Licensed under the MIT License - https://opensource.org/licenses/MIT

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='gym_chrome_dino', 
    version='0.0.3', 
    author='Elvis Yu-Jing Lin', 
    author_email='elvisyjlin@gmail.com', 
    description='Chrome Dino in OpenAI Gym', 
    long_description=long_description, 
    long_description_content_type='text/markdown', 
    url='https://github.com/elvisyjlin/gym-chrome-dino', 
    packages=find_packages(), 
    classifiers=[
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ], 
    install_requires=[
        'beautifulsoup4>=4.4.1', 
        'gym>=0.10.8', 
        'lxml>=3.5.0', 
        'numpy>=1.15.3', 
        'opencv-python>=3.4.2.17', 
        'Pillow>=3.1.2', 
        'requests>=2.9.1', 
        'selenium>=3.14.1'
    ], 
    license='MIT', 
    zip_safe=False
)
