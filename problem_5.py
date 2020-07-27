# -*- coding: utf-8 -*-
# @Project  :pythonfile
# @File     :problem_5
# @Date     :2020/7/27 23:39
# https://leetcode-cn.com/problems/longest-palindromic-substring/
import pandas as pd


def func(item):
    max_sent = 0
    max_sent_str = ""

    length = len(item)
    s = [[0 if i!=j else 1 for j in range(length)] for i in range(length)]



    for i in range(1,length):
        for j in range(i-1,0,-1):
            if item[i]==item[j] and (s[j+1][i-1]==1 or i-j==1): # 解决奇数位和偶数位问题
                s[j][i]=1
                max_sent_str = item[j:i+1]
                max_sent = len(max_sent_str)

    return max_sent_str,max_sent,s

if __name__=="__main__":
    demo = 'babadbbccabcbdbdadbdb'
    max_str, max_str_len,s = func(demo)
    print("max_str is {}".format(max_str))
    print("max_str_len is {}".format(max_str_len))
    print("whether Palindrome string matrix {}".format(pd.DataFrame(s)))
