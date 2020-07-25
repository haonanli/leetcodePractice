# -*- coding: utf-8 -*-
# @Project  :pythonfile
# @File     :problem_3
# @Date     :2020/7/16 0:30

def func(item):
    length = len(item)
    left = 0
    right = 0
    max_str = []
    max_str_len = 0

    cur_str=[]
    for i in range(length):
        right = i

        if item[right] in cur_str:
            if len(cur_str) > max_str_len:
                max_str_len=len(cur_str)
                max_str=cur_str
            else:
                left=right
        else:
            cur_str=item[left:right+1]
    return max_str,max_str_len

if __name__=='__main__':
    demo='abcdeaebcefghijki'
    max_str, max_str_len=func(demo)
    print("max_str is {}".format(max_str))
    print("max_str_len is {}".format(max_str_len))


