# _*_ coding: utf-8 _*_
__author__ = 'Mr. Yu Zhong.'
__date__ = '2020-05-04'

import os
import shutil


def classification(path):
    files_list = os.listdir(path)
    for file in files_list:
        fishname = file.rsplit('_', 1)
        print(os.path.join(path, file))  # 路径拼接
        print(os.path.join(path, fishname[0]))  # 路径拼接
        if not os.path.exists(os.path.join(path, fishname[0])):
            os.makedirs(os.path.join(path, fishname[0]))
            print("目录创建成功！")
        shutil.move(os.path.join(path, file), os.path.join(path, fishname[0]))

if __name__ == '__main__':
    path = r'L:\study\比赛\fish\WildFish_version1\images\WildFish_part1'
    classification(path)
    path = r'L:\study\比赛\fish\WildFish_version1\images\WildFish_part2'
    classification(path)
    path = r'L:\study\比赛\fish\WildFish_version1\images\WildFish_part3'
    classification(path)
    path = r'L:\study\比赛\fish\WildFish_version1\images\WildFish_part4'
    classification(path)
