#!/usr/bin/env python3

import os,glob
from PIL import Image

user = os.getenv('USER') # To get the username from environment variable
# folder_path = '/Users/{}/PycharmProjects/Google IT Automation with Python/project4/supplier-data/images/'.format(user) #mac
folder_path = '/home/{}/supplier-data/images/'.format(user) #linux

# resizing
for file in glob.glob(folder_path+"*.tiff"):
   im = Image.open(file)
   out_name = os.path.splitext(file)[0]
   im.resize((600,400)).convert("RGB").save(out_name + ".jpeg", "JPEG")
   print(out_name)


print(folder_path)
print(os.getcwd())
