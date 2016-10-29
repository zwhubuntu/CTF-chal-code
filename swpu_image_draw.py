from PIL import Image,ImageDraw
image = Image.new('RGB',(887, 111))
file = open('ce.txt')
draw = ImageDraw.Draw(image)
for i in xrange(887):
    for j in xrange(111):
        c = file.readline().split(',')
        draw.point((i, j), fill = (int(c[0]), int(c[1]), int(c[2])))
image.save("flag.jpg", "jpeg")