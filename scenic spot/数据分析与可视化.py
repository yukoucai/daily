# _*_coding : utf-8 _*_
# @Time : 2022/6/16 10:32 
# @Author : hosee
# @File : 数据分析与可视化
# @Project : untitled
from matplotlib import cm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取数据
sight_clean = pd.read_csv("sight_clean.csv")

# 数据可视化
# 显示中文和符号
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


# 各省市景区数量饼图
def drawpie():
    # 新建一个列表存放“位置”列数据
    lis = []
    lis = list(sight_clean['位置'])
    # 新建一个字典，用for循环计算每个省份所拥有的景区数量
    dic = {}
    for i in lis:
        dic[i] = dic.get(i, 0) + 1
    print("各省市景区数量为:",dic)
    key = dic.keys()
    value = dic.values()
    colors = cm.GnBu(np.arange(len(value)) / len(value))
    explode = []
    for p in range(len(key)):
        p = p * 0.01 + 0.1
        explode.append(p)
    # 画饼图
    plt.figure(figsize=(15,15))
    plt.axis('equal')
    plt.pie(x=value,labels=key,explode=explode,autopct='%.2f%%',colors=colors,pctdistance=0.9,radius=0.9)
    plt.title("各省市景区数量统计饼图",loc='center')
    plt.savefig("各省市景区数量统计饼图.jpg")
    plt.show()
drawpie()


# 各省市4A~5A景区数量柱状图
def drawbar():
    # 取"等级"为4A景区或5A景区的数据
    data1 = sight_clean[(sight_clean["等级"] == '4A景区') | (sight_clean["等级"] == '5A景区')]
    # 新建一个列表存放“位置”列数据
    lis=list(data1['位置'])
    # 新建一个字典，用for循环计算每个省份所拥有的4A~5A景区数量
    dic={}
    for i in lis:
        dic[i]=dic.get(i,0)+1
    print('各省市4A~5A的景区数量为：',dic)
    key=dic.keys()
    value=dic.values()
    # 画柱状图
    plt.figure(figsize=(15,10))
    plt.bar(key,value,color='thistle')
    plt.xticks(rotation=-45)
    plt.xlabel("省份")
    plt.ylabel("4A~5A景点数量")
    plt.title("各省市4A~5A景区数量统计图")
    # 为每个条形图添加数值标签
    for x,y in enumerate(value):
        plt.text(x-0.35,y+1,'%s'%int(y))
    plt.savefig("各省市4A~5A景区数量统计柱状图.jpg")
    plt.show()
drawbar()


# 各地区热度高于0.7的景点数量气泡图
def drawqipao():
    # 选取热度大于0.7的数据
    a = sight_clean[sight_clean['热度']>0.7]
    a = a.loc[:,['位置','热度']]
    b = a.groupby(a['位置']).count()
    x = list(b.index)
    y = list(b['热度'])
    color = np.random.rand(len(x))
    # 画图
    plt.figure(figsize=(15,7))
    plt.scatter(x,y,c=color,alpha=0.6)
    plt.xticks(rotation=45)
    for i in range(len(x)):
        plt.text(x[i],y[i],x[i],color='r',rotation=15)
    plt.title('各地区热度高于0.7的景点数量气泡图')
    plt.xlabel("省份")
    plt.ylabel('热度高于0.7的景点个数')
    plt.savefig("各地区热度高于0.7的景点数量气泡图.jpg")
    plt.show()
drawqipao()


# 月销售额前10景点数据图
def drawtu():
    data2 = sight_clean.sort_values(axis=0, by='月销售额', ascending=True).iloc[-10:]
    key=data2['景点名']
    value=data2['月销售额']
    # 画图
    plt.figure(figsize=(15,10))
    plt.ylim([0,20000000])
    plt.bar(key,value,color='wheat')
    plt.xlabel("景区名")
    plt.ylabel("月销售额")
    plt.xticks(rotation=90)
    plt.title("月销售额前10景点数据图")
    for x,y in enumerate(value):
        plt.text(x,y,'%s'%int(y))
    plt.savefig("月销售额前10景点数据图.jpg")
    plt.show()
drawtu()

