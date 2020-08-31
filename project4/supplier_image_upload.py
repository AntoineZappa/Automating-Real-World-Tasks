#!/usr/bin/env python3

import requests, glob, os

user = os.getenv('USER')
url = "http://localhost/upload/"
folder_path = '/home/{}/supplier-data/images/'.format(user)

for file in glob.glob(folder_path + '*.jpeg'):
    with open(file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
