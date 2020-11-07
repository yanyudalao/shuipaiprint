from PIL import Image, ImageDraw, ImageFont
import os

path = os.getcwd()+'\\'+'名单.txt'
print(path)
f = open(path,encoding='utf-8')

def faction(people,company):
    filepath = r"C:\Users\75600\Desktop\python_project\台卡模板.jpg"
    filename = os.getcwd()+"\\"+people + ".jpg"
    print(filename)
    fillColor = "#000000"  # 黑色
    image = Image.open(filepath)
    setFont = ImageFont.truetype('C:/windows/fonts/simhei.ttf', 200) #人名字体
    setFont2 = ImageFont.truetype('C:/windows/fonts/simhei.ttf', 100) #公司名字体
    if len(people)==3:
        people=people[0]+" "+people[1]+" "+people[2]
    else:
        people = people[0]+"  "+people[1]
    draw = ImageDraw.Draw(image)
    draw.text((850, 1500), people, font=setFont, fill="#000000", direction=None) #加入人名
    draw.text((800, 1800), company, font=setFont2, fill=fillColor, direction=None) #加入公司名

    image=image.transpose(Image.ROTATE_180)  #旋转操作
    draw = ImageDraw.Draw(image)
    draw.text((850, 1500), people, font=setFont, fill="#000000", direction=None)
    draw.text((800, 1800), company, font=setFont2, fill=fillColor, direction=None) #加入公司名
    image.save(filename)

for i in f.readlines():
    people = i.split(",")[0]
    company = i.split(",")[-1][:-1] #取出公司名称和去掉换行符
    company = company.center(12, '*')
    faction(people,company)

f.close()





