# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 15:05
# @Author  : zxl
# @FileName: DataBias.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""
看看数据分布是怎么样的
"""

if __name__ =="__main__":

    root="C://zxl/Data/GPA-large/processed/"
    gpa_file=root+"gpa.csv"
    df=pd.read_csv(gpa_file)

    for f, group_df in df.groupby(['failed']):
        gpa_values=group_df['gpa'].values
        plt.hist(gpa_values)
        plt.title('failed: %d'%f)
        plt.show()
    plt.hist(df['gpa'].values)
    plt.title('whole')
    plt.show()


    pass_df=df[df['failed']==0]
    fail_df=df[df['failed']==1]
    print("通过人数：%d, 挂科人数：%d"%(pass_df.shape[0],fail_df.shape[0]))
