'''

@author: wenhuizone
'''
import pytesseract
from PIL import Image
pic=Image.open('d:/1.bmp')

picgr=pic.convert('L')
threshold=200
table=[]
for i in range(256):
    if i>threshold:
        table.append(0)
    else:
        table.append(1)
out=picgr.point(table,'1')

text = pytesseract.image_to_string(out)
print text
