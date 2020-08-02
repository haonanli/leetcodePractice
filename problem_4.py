#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/2 6:03 下午 
# @Author : Haonan 
# @File : problem_4.py
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
# 分治类问题
# 问题描述：寻找两个正序数组中位数问题

'''
分解成分治类问题解决，求第K小的数
注意事项：
    1、奇偶数问题,在递归结果中处理
    2、索引问题,第K个数在数组中的索引为k-1
    3、边界问题,k=1与空值问题
'''


def func(A, B, k):
    t = k // 2

    # 确定最长序列与最短序列,保证A为最长序列
    if len(A) < len(B):
        A, B = B, A

    # 过程追踪
    print(k, t, A, B, A[0], A[1])

    # 边界条件处理
    if k == 1:
        return A[0] if len(A) % 2 == 1 else ((A[0] + A[1]) / 2)

    if len(B) == 0:
        return A[k - 1] if len(A) % 2 == 1 else ((A[k - 1] + A[k]) / 2)

    # 递归
    if A[t - 1] < B[t - 1]:
        return func(A[t:], B, k - t)
    else:
        return func(A, B[t:], k - t)


if __name__ == '__main__':
    A = [4, 5, 6]
    B = [3, 4, 5, 5, 9]
    len_A = len(A)
    len_B = len(B)
    k = (len_A + len_B) // 2
    medium = func(A, B, k)
    print("medium is {}".format(medium))
