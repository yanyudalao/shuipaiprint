from PIL import Image, ImageDraw, ImageFont
import os

path = os.getcwd()+'\\'+'人员名单(可带公司名称).txt'
print(path)
f = open(path,encoding='utf-8')
x = 45
y = 58
x2 = 45
y2 = 68


def faction(name1,name2):
    filepath = os.getcwd()+'\\'+'台卡模板.jpg'
    filename = os.getcwd()+"\\"+name1 + ".jpg"
    fillColor = "#000000"  # 黑色
    image = Image.open(filepath)
    setFont = ImageFont.truetype('C:/windows/fonts/simhei.ttf', 200) #主行
    setFont2 = ImageFont.truetype('C:/windows/fonts/simhei.ttf', 100) #次行
    image_size = image.size
    x_ture = x / 100 * image_size[0]
    y_ture = y / 100 * image_size[1]
    x2_ture = x2 / 100 * image_size[0]
    y2_ture = y2 / 100 * image_size[1]
    print(name1)
    if len(name1)==3:
        name1=name1[0]+" "+name1[1]+" "+name1[2]
    else:
        name1 = " "+name1[0]+"  "+name1[1]

    draw = ImageDraw.Draw(image)
    draw.text((x_ture, y_ture), name1, font=setFont, fill="#000000", direction=None) #加入人名
    draw.text((x2_ture, y2_ture), name2, font=setFont2, fill=fillColor, direction=None) #加入公司名


    image=image.transpose(Image.ROTATE_180)  #旋转操作
    draw = ImageDraw.Draw(image)
    draw.text((x_ture, y_ture), name1, font=setFont, fill="#000000", direction=None) #加入人名
    draw.text((x2_ture, y2_ture), name2, font=setFont2, fill=fillColor, direction=None) #加入公司名

    image.save(os.getcwd()+"\\"+"name(company)"+"\\"+name1 + ".jpg")

for i in f.readlines():
    name1 = i.split(",")[0]
    name2 = i.split(",")[-1][:-1] #取出次行名称和去掉换行符
    name2 = name2.center(12, ' ')
    faction(name1,name2)

f.close()