# _*_ coding:utf-8 _*_
#!/usr/local/bin/python3

from PIL import Image
import os

# 拆分GIF
def gif2png(fileName, asciiChar, font, isgray, scale):
    '''将GIF拆分并将每一帧处理成字符画
    fileName: GIF文件
    asciiChar: 灰度值对应的字符串
    font: ImageFont对象
    isgray: 是否生成黑白动图
    scale: 缩放比例
    '''
    # GIF文件打开为一个序列
    image = Image.open(fileName)
    path = os.getcwd()
    # Cache文件用以保存拆分以后的图片和生成的字符画
    cachePath = path+"/Cache"
    if(not os.path.exists(cachePath)):
        os.mkdir(cachePath)
    os.chdir(cachePath)
    # 清空Cache文件夹下的内容，防止多次运行时被之前的文件影响
    for f in os.listdir(cachePath):
        os.remove(f)
    # GIF打开后的序列通过tell返回每一帧的索引，超出索引范围后抛出异常
    try:
        while 1:
            current = image.tell()
            name = fileName.split('.')[0] + '-' + str(current) + '.png'
            # 将每一帧处理为字符画
            image.save(name)

