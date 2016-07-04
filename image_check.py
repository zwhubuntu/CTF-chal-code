'''

@author: wenhuizone
'''
import Image
import pytesseract
import PIL

im=Image.open('D:/1.bmp')
imgry=im.convert('L')
threshold = 140  
table = []  
for i in range(256):  
    if i < threshold:  
        table.append(0)  
    else:  
        table.append(1)
out = imgry.point(table,'1')
text = pytesseract.image_to_string(out)

print text