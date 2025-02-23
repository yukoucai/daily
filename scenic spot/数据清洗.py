# _*_coding : utf-8 _*_
# @Time : 2022/6/9 8:13 
# @Author : hosee
# @File : 数据清洗
# @Project : untitled
import pandas as pd

# 读取csv文件并添加索引
sight = pd.read_csv('sight.csv',header=None,names=['景点名','位置','等级','描述','热度','票价','月销量'])

# 计算月销售额
sight["月销售额"] = sight["票价"] * sight["月销量"]

# '热度'列保留2位小数,'票价'列保留1位小数,'月销售额'列保留1位小数
sight['热度']= sight['热度'].round(2)
sight['票价']= sight['票价'].round(1)
sight['月销售额']= sight['月销售额'].round(1)

# 去空（一行中主要有一个空值就删除）
sight_null = sight.dropna(axis=0, how='any',inplace=False)

# 去重（去除景点名重复的值）
sight_only = sight_null.drop_duplicates(subset=['景点名'], keep='last', inplace=False)

# 保存
sight_only.to_csv('sight_clean.csv', index=False,encoding='utf_8_sig')