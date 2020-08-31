#!/usr/bin/env python3

import os
import requests

# variables
path = os.path.expanduser('~')+'/test/data/feedback/'
keys = ["title", "name", "date", "feedback"]

# iteration over the file
for file in os.listdir(path):
    mydict = {}
    keyscount = 0
    with open(path+file) as file:
        for line in file:
            value = line.strip()
            mydict[keys[keyscount]] = value
            keyscount +=1
    print(mydict)
    response = requests.post("http://35.184.93.113/feedback/",json=mydict) #change the ip address
print(response.request.body)
print(response.status_code)
