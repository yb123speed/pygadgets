#-*- coding:utf-8 -*-
#!/usr/local/bin/python3
# whl包对应python3.6平台

import numpy as np

def video2imgs(video_name, size):
    """
    :param video_name: 字符串，视频文件的路径
    :param size: 二元组，(宽,高)，用于指定生成的字符画的尺寸
    :return: 一个 img对象的列表，img对象实际上就是numpy.ndarray 数组
    """
    # 导入opencv
    import cv2
    img_list = []
    # 从指定文件创建一个VideoCapture对象
    cap = cv2.VideoCapture(video_name)
    # 如果cap对象已经初始化完成了，就返回true，换句话说就是一个 while true 循环
    while cap.isOpened():
        # cap.read()返回值介绍：
        #   ret 表示是否读取到图像
        #   frame 为图像矩阵，类型为numpy.ndarray.
        ret, frame = cap.read()
        if ret:
            # 转换成灰度图，也可不做这一步，转换成彩色字符视频
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            #resize 图片，保证图片转换成字符画后，能完整地在命令行中显示
            img = cv2.resize(gray,size,interpolation=cv2.INTER_AREA)
            # 分帧保存转换结果
            img_list.append(img)
        else:
            break
    # 结束是要释放空间
    cap.release()
    return img_list

pixels = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"

def img2chars(img):
    res = []
    """

    :param img: numpy.ndarray,图像矩阵
    :return: 字符串的列表：图像对应的字符画，其每一行对应图像的一行像素
    """
    
    # 要注意这里的顺序和 之前的 size 刚好相反
    height, width = img.shape
    for row in range(height):
        line = ""
        for col  in range(width):
            # 灰度是用8位表示的，最大值为255.
            # 这里将灰度转化到0~1之间
            percent = img[row][col] / 255

            # 将灰度值进一步转换成 0 到 (len(pixels) - 1)之间，这样就好pixels里的字符对应起来了
            index = int(percent * (len(pixels) - 1))

            # 添加字符像素 （最后面加一个空格，是因为命令行有行距却几乎没有字符间距，用空格当间距）
            line += pixels[index] + ' '
        res.append(line)
    return res

def imgs2chars(imgs):
    video_chars = []
    for img in imgs:
        video_chars.append(img2chars(img))
    return video_chars

def play_video(video_chars):
    """
    播放字符视频
    :param video_chars: 字符画的列表，每个元素为一帧
    ：return: None
    """
    # 导入需要的模块
    import time,curses

    # 获取字符画的尺寸
    width, height = len(video_chars[0][0]), len(video_chars[0])

    # 初始化curses
    stdscr = curses.initscr()
    curses.start_color()
    try:
        #调整窗口大小，宽度最好略大于字符画宽度。另外注意curses的height和width的顺序
        stdscr.resize(height, width*2)
        
        for pic_i in range(len(video_chars)):
            # 显示pic_i，即第1帧字符画
            for line_i in range(height):
                # 将pic_i的第1行写入第i列。(line_i, 0)表示从第i行的开头开始写入。最后一个参数设置字符为白色
                stdscr.addstr(line_i, 0, video_chars[pic_i][line_i], curses.COLOR_WHITE)
            stdscr.refresh() # 写入后需要refres才会立即更新界面

            time.sleep( 1/ 24) # 粗略地控制播放速度。更精确的方式是使用游戏编程里，精灵的概念
    finally:
        # curses 使用前要初始化，用完后无论有没有异常，都要关闭
        curses.endwin()
    return

if __name__ == "__main__":
    import sys
    imgs = video2imgs(sys.path[0]+"\BadApple.mp4",(64, 48))
    video_chars = imgs2chars(imgs)
    input("转换完成！按Enter键开始播放")
    play_video(video_chars)