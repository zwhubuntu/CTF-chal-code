'''

@author: wenhuizone
'''
import Image  
import sys   
im = Image.open('d:/flag.bmp')
pix = im.load()  
width = im.size[0]  
height = im.size[1]  
print "/* width:%d */"%(width)  
print "/* height:%d */"%(height)  
count = 0   
for h in range(0, height):  
    for w in range(0, width):  
        pixel = im.getpixel((w, h))+1
        for i in range(0,3):  
            count = (count+1)%16  
            if (count == 0):   
                print "0x%02x,/n"%(pixel[i]),  
            else:  
                print "0x%02x,"%(pixel[i]), 
im