import requests
# import os
# from numpy.lib.type_check import imag
# import cv2

# import cv2

# with open('download.png', 'rb') as image_file:
#     content1 = image_file.read()

# image = cv2.imread('download.png')
# success, encoded_image = cv2.imencode('.png', image)
# content2 = encoded_image.tobytes()
# print(content1 == content2)

# URL = "https://httpbin.org/post"
# # image = open("download.png", "rb").read()
# image = cv2.imread('download.png')
# success, encoded_image = cv2.imencode('.png', image)
# content2 = encoded_image.tobytes()

# DATA = {
#     "event": "person",
#     "number": 2,
#     "image": content2
# }
# x = requests.post(url=URL, data=DATA)

# files = {'file': ('image.png', content2, 'image/png', {'Expires': '0'}), 'number':2}
# x = requests.post(url=URL, files=files)

# URL = "http://192.168.1.102:5000/api/triggers/fire?auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJUcmlnZ2VyQ3JlYXRvcklkIjoiMSIsIlRyaWdnZXJJZCI6ImQ1MzUwMWYyLWZhZDUtNDFmNi04NTE2LWJjZmIyNGM0NThhYyIsIm5iZiI6MTYyOTk5Njg5MSwiZXhwIjozNTIzNDUyODkxLCJpYXQiOjE2Mjk5OTY4OTF9.XCghdyWOGE6l1128Z3M6IiBTVN3rrmR51_rfzXpcT1I"
# DATA = {
#     "ValueType": 0,
#     "Value": "1"
# }

# # print(DATA)

# x = requests.post(url=URL, data=DATA)

# print(x.text)


url = "http://192.168.1.102:5000/api/triggers/fire?auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJUcmlnZ2VyQ3JlYXRvcklkIjoiMSIsIlRyaWdnZXJJZCI6ImQ1MzUwMWYyLWZhZDUtNDFmNi04NTE2LWJjZmIyNGM0NThhYyIsIm5iZiI6MTYyOTUwMDgwNiwiZXhwIjozNTIyOTU2ODA2LCJpYXQiOjE2Mjk1MDA4MDZ9.NVWma68Vbq1sE6nDuIUXYAd5GzCMx0kbPRZcM6hvBks"

payload="{\r\n    \"ValueType\": 0,\r\n    \"Value\": \"Ahmad\"\r\n}\r\n"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)