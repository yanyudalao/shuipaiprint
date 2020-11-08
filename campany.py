from PIL import Image, ImageDraw, ImageFont
import os

path = os.getcwd()+'\\'+'公司名单.txt'
print(path)
f = open(path,encoding='utf-8')


def faction(name1):
    x = 45
    y = 62
    filepath = os.getcwd()+'\\'+'台卡模板.jpg'
    filename = os.getcwd()+"\\"+name1 + ".jpg"
    fillColor = "#000000"  # 黑色
    image = Image.open(filepath)
    setFont = ImageFont.truetype('C:/windows/fonts/simhei.ttf', 200) #主行
    print(name1)
    if len(name1)<4:
        pass
    elif len(name1)<5:
        setFont = ImageFont.truetype('C:/windows/fonts/simhei.ttf', 180)  # 主行
    elif len(name1)<7:
        setFont = ImageFont.truetype('C:/windows/fonts/simhei.ttf', 160)  # 主行
        x = 42
    elif len(name1)<9:
        setFont = ImageFont.truetype('C:/windows/fonts/simhei.ttf', 135)  # 主行
        x = 38

    image_size = image.size
    x_ture = x / 100 * image_size[0]
    y_ture = y / 100 * image_size[1]

    draw = ImageDraw.Draw(image)
    draw.text((x_ture, y_ture), name1, font=setFont, fill="#000000", direction=None) #加入人名


    image=image.transpose(Image.ROTATE_180)  #旋转操作
    draw = ImageDraw.Draw(image)
    draw.text((x_ture, y_ture), name1, font=setFont, fill="#000000", direction=None) #加入人名
    image.save(os.getcwd()+"\\"+"campany"+"\\"+name1 + ".jpg")

for i in f.readlines():
    #name1 = i.split(",")[-1][:-1]  # 取出次行名称和去掉换行符
    name1 = i.replace("\n", "")
    faction(name1)

f.close()