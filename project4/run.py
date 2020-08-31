#!/usr/bin/env python3

import os, glob
import requests

# dictionary iteration key + txt line file reading
def push_data(url, descriptions_folder):
    '''Returns a list of dictionaries containing the name, weight, description
    and the image_name, and push the result data to the localhost'''
    fdict = {}
    fruits = []
    keys = ["name", "weight", "description", "image_name"]

    # iterating over text files
    for file in glob.glob(descriptions_folder + '*.txt'):
        with open(file, 'r', encoding='utf-8') as infile:
            reader = infile.read().split("\n")
            for i in range[3]:
                fdict.update({keys[i] : reader[i]}) #append values to the dictionary

        # changing and appending filename
        filename = os.path.basename(file)
        img = filename.replace(".txt",".jpeg")
        fdict.update({keys[3]: img})

    #convert the weight value to integer
    for keys in fruits:
        i = keys["weight"][:3]
        keys["weight"] = i
    for keys in fruits:
        keys["weight"] = int(keys["weight"])

    # creating json file
    fruits.append(fdict)
    print(fruits)
    print(fdict)

    # pushing data to the server
    for i in range(len(fruits)):
        response =  requests.post(url, json=fruits[i])
        response.raise_for_status()
    return 0


if __name__=='__main__':
    url = 'http://localhost/fruits/'
    user = os.getenv('USER')
    descriptions_folder = '/home/{}/supplier-data/descriptions/'.format(user)
    # descriptions_folder = '/Users/{}/PycharmProjects/Google IT Automation with Python/project4/supplier-data/descriptions/'.format(user) #mac
    push_data(url, descriptions_folder)