import os
from numpy.lib.type_check import imag
import requests
import cv2

import cv2

# with open('download.png', 'rb') as image_file:
#     content1 = image_file.read()

# image = cv2.imread('download.png')
# success, encoded_image = cv2.imencode('.png', image)
# content2 = encoded_image.tobytes()
# print(content1 == content2)

URL = "https://httpbin.org/post"
# image = open("download.png", "rb").read()
image = cv2.imread('download.png')
success, encoded_image = cv2.imencode('.png', image)
content2 = encoded_image.tobytes()

DATA = {
    "event": "person",
    "number": 2,
    "image": content2
}
x = requests.post(url=URL, data=DATA)

# files = {'file': ('image.png', content2, 'image/png', {'Expires': '0'}), 'number':2}
# x = requests.post(url=URL, files=files)

print(x.text)