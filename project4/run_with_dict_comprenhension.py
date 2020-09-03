#!/usr/bin/env python3

import os, glob, json
import requests

# dictionary iteration key + txt line file reading
def push_data(url, descriptions_folder):
    '''Returns a list of dictionaries containing the name, weight, description
    and the image_name, and push the result data to the localhost'''

    fruit_keys = ["name", "weight", "description", "image_name"]
    fruits = []
    # iterating over text files
    for filename in glob.glob(descriptions_folder + '*.txt'):
        fdict = {}
        with open(filename, 'r', encoding='utf-8') as infile:

            fdict = {fruit_keys[i]: line.strip() for i, line in enumerate(infile)}
            # for i, line in enumerate(infile):
            #     fdict[fruit_keys[i]] = line.strip()

            # changing and appending filename
            filename = os.path.basename(filename)
            fdict['weight'] = int(fdict['weight'].replace(' lbs',''))
            fdict['image_name'] = filename.replace(".txt",".jpeg")

        # creating json file
        fruits.append(fdict)

    print(fruits)

    #pushing data to the server
    for i in range(len(fruits)):
        response =  requests.post(url, json=fruits[i])
        response.raise_for_status()
    return 0


if __name__=='__main__':
    url = 'http://localhost/fruits/'
    user = os.getenv('USER')
    descriptions_folder = '/home/{}/supplier-data/descriptions/'.format(user)
    descriptions_folder = '/Users/{}/PycharmProjects/Google IT Automation with Python/Automating Real-World Tasks/project4/supplier-data/descriptions/'.format(user) #mac
    push_data(url, descriptions_folder)
