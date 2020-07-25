# -*- coding: utf-8 -*-
# @Project  :pythonfile
# @File     :problem_4
# @Date     :2020/7/16 0:30

import numpy as np
import pandas as pd


if __name__=="__main__":
    k=3
    demo=[1,2,3,4,5,6,0,-2,9,8]
    result_idx=np.argsort(np.array(demo))
    result=np.array(demo)[result_idx][::-1][:k]
    print("result is {}".format(result))