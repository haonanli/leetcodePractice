#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/2 11:26 下午 
# @Author : Haonan 
# @File : problem_2.py
# https://leetcode-cn.com/problems/add-two-numbers/
# 链表 每个位置对应值相加

"""
1、定义链表结构
2、定义链表起始结点
3、每个位置链表对应值的运算（加减乘除）,运算结果放入链表结点对应值中,同时将上一个结点的指针指向当前链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def func(l1: ListNode, l2: ListNode):
    # 定义链表起始点
    dummy = p = ListNode(None)
    s = 0

    # 循环,每个位置递加
    while l1 or l2 or s:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0

        s += l1_val + l2_val
        # 判断是否大于10,如果大于10,则取余,作为当前结点的值,并对s除10的结果取整,累加到下一阶段中
        p.next = ListNode(s % 10)  # 上一个结点的链接指向当前结点
        s = s // 10

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
