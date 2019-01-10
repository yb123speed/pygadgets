#!/usr/bin/python
# -*- coding: utf8 -*-

import rarfile
import zipfile
import os
import re
from multiprocessing.dummy import Pool
def un_rar(file_name,pwd=None):
    try:
        if file_name.split('.')[-1]=='rar':
            rar = rarfile.RarFile(file_name)
            rar.extractall(path=file_name.split('.')[0],pwd=pwd)
        elif file_name.split('.')[-1]=='zip':
            zip = zipfile.ZipFile(file_name)
            zip.extractall(path=file_name.split('.')[0],pwd=pwd)
    except Exception as e :
        print(e)
        print('Fail：'+file_name)
    else:
        print('Success')
def point_file_name(path):
    return [os.path.join(item[0],file_name) for item in os.walk(path) for file_name in item[-1] if re.search(r'.rar$|.zip$',file_name)]
if __name__ == '__main__':
    path = r'dirpath'
    pwd = 'password'
    # with open(r'UnRAR.exe','rb') as f:
    #     with open(os.path.join(path,'UnRAR.exe'),'wb') as other:
    #         other.write(f.read())
    file_names = point_file_name(path)
    pool= Pool()
    pool.starmap(un_rar,zip(file_names,[pwd]*len(file_names)))
    pool.close()
    pool.join()