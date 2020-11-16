from PIL import Image, ImageDraw, ImageFont
import os

def draw(moban_path,location,conment,str_volume_1=200,str_volume_2=100):
    '''在某个位置上绘画某些内容
    设置打印文字的颜色，大小，字体属性
    打开图片
    提出所有的人名和公司名并且绘画上去
    保存图片'''
    fillColor = "#000000"  # 黑色
    setFont = ImageFont.truetype('C:/windows/fonts/simhei.ttf', str_volume_1)  # 主行
    setFont2 = ImageFont.truetype('C:/windows/fonts/simhei.ttf',str_volume_2) #次行
    if os.path.exists('输出文件夹') == False:
        os.mkdir("输出文件夹")
    for i in conment:
        image = Image.open(moban_path)
        name,company = i.split(",")[0],i.split(",")[1]
        draw_name,draw_company = str_space(name).center(6,'　'),str_space(company).center(10,'　')
        draw_txt = ImageDraw.Draw(image)
        draw_txt.text((location[0],location[1]), draw_name , font=setFont, fill=fillColor, direction=None)
        draw_txt.text((location[2],location[3]), draw_company , font=setFont2, fill=fillColor, direction=None)
        image = image.transpose(Image.ROTATE_180)
        draw_txt = ImageDraw.Draw(image)
        draw_txt.text((location[0],location[1]), draw_name , font=setFont, fill=fillColor, direction=None)
        draw_txt.text((location[2],location[3]), draw_company , font=setFont2, fill=fillColor, direction=None)
        image.save(f'{os.getcwd()}\\输出文件夹\\{company}_{name}.jpg')
        print(f'输出【{company}_{name}.jpg】完成')


def location(moban_path,*args):
    '''确定位置函数,
    打开文件，
    获取图像size，
    把需要写入文字的位置百分比算出来，
    加入到location_list内'''
    location_list=[]
    try:
        image = Image.open(moban_path)
    except:
        return print("模板路径不对，请重新输入")
    image_size = image.size
    for i in args:
        if i//2 == 0:
            location_list.append(i/100*image_size[0])
        else:
            location_list.append(i/100*image_size[1])
    return location_list

def conment(txt_path=''):
    '''提取打印内容,
    判断文档能否正常打开'''
    conment_list=[]
    if txt_path=='':
        return  "未填写文档路径"
    try:
        f = open(txt_path, encoding='utf-8')
    except:
        return "文档路径出错"
    for i in f.readlines():
        b=i.replace(" ", "").replace("\t","").strip()
        conment_list.append(b)
    return conment_list

def str_space(string):
    string0 = ''
    for i in string:
        string0 += i + ' '
    return string0[0:-1]

txt_path = os.getcwd() + '\\' + '人员名单(可带公司名称).txt'
moban_path = os.getcwd() + '\\' + '台卡模板.jpg'

draw(moban_path,location(moban_path,30,60,30,70),conment(txt_path))

