# _*_ coding:utf-8 _*_
#!/usr/local/bin/python3

from PIL import Image, ImageFont, ImageDraw
import argparse
import os
import imageio

#命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-d','--duration',type = float, default = 1)#播放时间
#获取参数
args = parser.parse_args()
File = args.file
DURARION = args.duration
#像素对应ascii码
ascii_char = list("M!N@H?Q$O#C\6/7<+>:-. ")

# 将像素转化为ascii码
def getChar(r, g, b, alpha = 256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]

# 创建字符画
def char2png(file_name, font, scale=1):
    im = Image.open(file_name).convert("RGB")
    #gif拆分后的图像，需要转换，否则报错，由于gif分割后保存的是索引颜色
    raw_width = int(im.width*scale)
    raw_height = int(im.height*scale)
    font_w, font_h = font.getsize('M') #获取字体的宽高
    block_w = int(font_w*scale)
    block_h = int(font_h*scale)
    width = int(raw_width/block_w)
    height = int(raw_height/block_h)
    im = im.resize((width,height),Image.NEAREST)
    txt=""
    colors = []
    for i in range(height):
        for j in range(width):
            pixel = im.getpixel((j,i))
            colors.append((pixel[0],pixel[1],pixel[2]))
            if(len(pixel) == 4):
                txt += getChar(pixel[0],pixel[1],pixel[2],pixel[3])
            else:
                txt += getChar(pixel[0],pixel[1],pixel[2])        
        txt += '\n' 
        colors.append((255,255,255))
    im_txt = Image.new("RGB",(raw_width,raw_height),(255,255,255))
    dr = ImageDraw.Draw(im_txt)
    font=ImageFont.load_default().font
    x=y=0
    # font_h *=1 #调整后更佳
    #ImageDraw为每个ascii码进行上色
    for i in range(len(txt)):
        if(txt[i]=='\n'):
            x+=font_h
            y=-font_w
        dr.text([y*scale,x*scale],txt[i],colors[i])
        y+=font_w
    name = file_name.split('.')[0]+'-txt'+'.png'
    print(name)
    im_txt.save(name)

# 拆分GIF
def gif2png(file_name,scale):
    '''将GIF拆分并将每一帧处理成字符画
    fileName: GIF文件
    '''
    # GIF文件打开为一个序列
    image = Image.open(file_name)
    path = os.getcwd()
    # Cache文件用以保存拆分以后的图片和生成的字符画
    cache_path = path+"/Cache"
    font = ImageFont.load_default().font
    if(not os.path.exists(cache_path)):
        os.mkdir(cache_path)
    os.chdir(cache_path)
    #  清空Cache文件夹下的内容，防止多次运行时被之前的文件影响
    for f in os.listdir(cache_path):
        os.remove(f)
    # GIF打开后的序列通过tell返回每一帧的索引，超出索引范围后抛出异常
    try:
        while 1:
            current = image.tell()
            name = file_name.split('.')[0] + '-' + str(current) + '.png'
            # 将每一帧处理为字符画
            image.save(name) #gif分割后保存的是索引颜色
            print(name + " saved.")
            char2png(name,font,scale)
            image.seek(current+1)
    except:
        os.chdir(path)

#转换为gif
def png2gif(dir_name):
    path = os.getcwd()
    os.chdir(dir_name)
    dirs = os.listdir()
    images = []
    num = 0
    for d in dirs:
        if d.split('-')[-1] == 'txt.png':
            images.append(imageio.imread(d))
            num += 1
    os.chdir(path)
    imageio.mimsave(d.split('-')[0]+'-txt_c.gif',images,duration = DURARION)

if __name__=='__main__':
    gif2png(File,1)
    path = os.getcwd()
    png2gif(path+"/Cache")