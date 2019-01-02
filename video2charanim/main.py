#-*- coding:utf-8 -*-

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
