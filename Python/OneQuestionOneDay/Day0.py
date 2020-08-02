'''第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字
，类似于微信未读信息数量那种提示效果。 类似于图中效果'''

from PIL import Image
im = Image.open('M:\\Python\\OneQuestionOneDay\\Day0_meizi.jpg')
#im.show()
box=(100,100,500,500)
region = im.crop(box)
#region.show()
#region.save('After_crop.jpg','JPEG')
#im.paste(region,box)
#output = im.getpixel((40,40))
#print(output)
#im.putpixel((4,4),(255,0,0))
drawlist = [(10,6),(10,7),(10,8),(10,9),(10,10),(10,11),(10,12),(7,9),
            (11,11),(10,13),(10,14),(9,11),(8,11),(7,11),(6,11),(6,10),
            (8,8),(8,7),(10,6),(10,5),(9,6)]

def draw_4(start,size):
    '4-6 as the smallest size'
    x,y = start
    x1 = x+4*size
    y1 = y+6*size
    drawlist = list()
    center = (x1,y1)
    drawlist.append(center)
    for i in range(1,size+1):
        drawlist.append((x1+i,y1))
    for i in range(1,2*size+1):
        drawlist.append((x1,y1+i))
    for i in range(1,4*size):
        drawlist.append((x1-i,y1))
    for i in range(1,6*size):
        drawlist.append((x1,y1-i))
    begin = (x,y1)
    end = (x1,y)
    pointer = (x+1.3,y1-0.45)
    while pointer[0] < x1:
        m = pointer[0]
        n = pointer[1]
        drawlist.append((int(m//1),int(n//1)))
        pointer = (m+0.3,n-0.45)
    print(drawlist)
    return drawlist

drawlist = draw_4((500,6),6)
for xy in drawlist:
    im.putpixel(xy,(123,0,0))
im.show()
im.save('Outcome.jpg','JPEG')
