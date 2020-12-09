import os
from PIL import Image
import re
pathIn = 'Images\\Stock\\'
pathOut = 'Images\\Converted\\'
images = ''

for items in os.walk(pathIn):
    images = items[2]
for image in images:
    if re.match(r'.*\.jpg', image):
        im = Image.open(pathIn + image)
        im.save(pathOut + image[:-4] + '.png', 'png')
