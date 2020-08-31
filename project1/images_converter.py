#!/usr/bin/env python3

import os
from PIL import Image

'''Images converter to change path, size, rotation, format and color mode'''

img_fold = '/images/' #images folder
old_path = os.path.expanduser('~') + img_fold #original path
new_path = '/opt/icons/' #final path
new_size = (128, 128) #image size
rotation = -90 #Range betweeen -360 to 360
colormod = "RGB" #L, RGB, CMYK
new_form = 'jpeg' # image final format

for image in os.listdir(old_path):
    if '.' not in image[0]:
        img = Image.open(old_path + image)
        img.rotate(rotation).resize(new_size).convert(colormod).save(new_path + image.split('.')[0], new_form)
        img.close()
