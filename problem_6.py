#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/5 11:36 下午 
# @Author : Haonan 
# @File : problem_6.py
# https://leetcode-cn.com/problems/zigzag-conversion/
# Z字形变换

"""
边界问题处理
1、找出边界点
2、在边界点处实施反转操作
"""


def func(item, num):
    if num < 2:
        return item
    s = ["" for _ in range(num)]
    i = 0
    flag = -1
    for char in item:
        s[i] = s[i] + char
        if i == 0 or i == num - 1:# 边界判断,边界与索引相差1个单位
            flag = -flag
        i = i + flag
    return "".join(s)

if __name__=="__main__":
    demo='LEETCODEISHIRING'
    num=3
    result=func(demo,num)
    print("the Z transform is {}".format(result))

