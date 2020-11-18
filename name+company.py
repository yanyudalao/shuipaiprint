from PIL import Image, ImageDraw, ImageFont
import os ,sys

def draw(moban_path,location,conment,font0='C:/windows/fonts/simhei.ttf',str_volume_1=200,str_volume_2=100):
    '''在某个位置上绘画某些内容
    设置打印文字的颜色，大小，字体属性
    打开图片
    提出所有的人名和公司名并且绘画上去
    保存图片'''
    fillColor = "#000000"  # 黑色
    try:
        setFont = ImageFont.truetype(font0, str_volume_1)  # 主行
        setFont2 = ImageFont.truetype(font0,str_volume_2) #次行
    except:
        print("可能你的字体路径出错了，请自行看源码解决")
        input("按回车键关闭程序")
        sys.exit(0)
    for i in conment:
        image = Image.open(moban_path)
        try:
            name,company = i.split(",")[0],i.split(",")[1]
            draw_name, draw_company = str_space(name).center(6, '　'), str_space(company).center(10, '　')
        except:
            print(f'【{i}】格式不对，跳过')
            continue
        draw_txt = ImageDraw.Draw(image)
        draw_txt.text((location[0],location[1]), draw_name , font=setFont, fill=fillColor, direction=None)
        draw_txt.text((location[2],location[3]), draw_company , font=setFont2, fill=fillColor, direction=None)
        image = image.transpose(Image.ROTATE_180)
        draw_txt = ImageDraw.Draw(image)
        draw_txt.text((location[0],location[1]), draw_name , font=setFont, fill=fillColor, direction=None)
        draw_txt.text((location[2],location[3]), draw_company , font=setFont2, fill=fillColor, direction=None)
        image.save(f'{os.getcwd()}\\输出文件夹\\{company}_{name}.jpg')
        print(f'输出【{company}_{name}.jpg】完成')
    print("全部打印完毕")
    input("回车键结束")

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
    f = open(txt_path, encoding='utf-8')
    for i in f.readlines():
        b=i.replace(" ", "").replace("\t","").strip()
        conment_list.append(b)
    return conment_list

def str_space(string):
    string0 = ''
    for i in string:
        string0 += i + ' '
    return string0[0:-1]

def new_init():
    '''分别判断需要的文件和文件夹是否存在'''
    if os.path.exists(moban_path) == False:
        print('【台卡模板.jpg】不存在！！！请再读10遍说明')
        input("按回车键关闭程序")
        sys.exit(0)
    if os.path.exists(txt_path) == False:
        open(txt_path, 'w', encoding='utf-8').write('人名,公司名称, \n')
        print("【人员名单(可带公司名称).txt】不存在，已创建，请填写内容后再运行本程序")
        input("按回车键关闭程序")
        sys.exit(0)
    if os.path.exists('输出文件夹') == False:
        os.mkdir("输出文件夹")
        print("【输出文件夹】不存在"
              "创建【输出文件夹】完毕")

txt_path = os.getcwd() + '\\' + '人员名单(可带公司名称).txt'
moban_path = os.getcwd() + '\\' + '台卡模板.jpg'

print("说明：\n"
      "本文件会使用当前路径下的【人员名单(可带公司名称).txt】读取文件\n"
      "和在【输出文件夹】内生成需要的文件\n"
      "如果不存在，会自动生成\n"
      "名单填写方式是一行一个【人名,公司名(可不填),】看准，是有英文标点的逗号的\n"
      "必须：还要一个【台卡模板.jpg】文件和本程序放在一起\n"
      "如果看不懂，请再读一遍\n")
input("看完了就按回车键开始")


new_init()
draw(moban_path,location(moban_path,30,60,30,70),conment(txt_path))



