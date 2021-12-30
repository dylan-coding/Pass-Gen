# Author: Dylan Smith
# Class: CS 361
# Description: This software is a microservice image transformer with the capabilities of resizing images and adding
#               transparent backgrounds.

import requests
from PIL import Image
from io import BytesIO


url = 'http://flip3.engr.oregonstate.edu:9114/'
files = {'image': open('test.png', 'rb')}
r = requests.post(url, files=files)
i = Image.open(BytesIO(r.content))
i.save('new_image.png')
