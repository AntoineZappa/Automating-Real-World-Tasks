#! /usr/bin/env python3

import os
import glob
import requests

user = os.getenv('USER')
text_files = glob.glob(
    "/home/{}/supplier-data/descriptions/*.txt".format(user))
keys = ["name", "weight", "description", "image_name"]
feed_list = []

# parsing through the text files
for files in text_files:
    with open(files, 'r', encoding='utf-8') as f:
        dict = {}
        reader = f.read().split("\n")
        for i in range(3):
            # append values to the dictionary
            dict.update({keys[i]: reader[i]})

        files = os.path.basename(files)
        img = files.replace(".txt", ".jpeg")
        dict.update({keys[3]: img})  # appending the image files

        feed_list.append(dict)  # creating a list of dictionary
# convert the weight value to integer
for keys in feed_list:
    i = keys["weight"][:3]
    keys["weight"] = i
for keys in feed_list:
    keys["weight"] = int(keys["weight"])

# feed data to the website
url = "http://localhost/fruits/"
for i in range(len(feed_list)):
    response = requests.post(url, json=feed_list[i])
    response.raise_for_status()
