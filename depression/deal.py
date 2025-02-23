# _*_coding : utf-8 _*_
# @Time : 2024/6/4 18:24
# @Author : hosee
# @File : 01
# @Project : caiyukou
import jieba
import re
# 读取停用词文件并存储到集合中
def load_stop_words(stop_words_file_path):
    with open(stop_words_file_path, 'r', encoding='utf-8') as file:
        stop_words = set([line.strip() for line in file])
    return stop_words
# 清洗、分词并去除停用词
def clean_segment_and_remove_stop_words(line, stop_words):
    # 使用正则表达式去除所有非中文字符、字母和数字
    regex_pattern = re.compile(r'[^\u4e00-\u9fa5]')
    cleaned_line = regex_pattern.sub('', line)
    # 使用结巴进行分词
    words = jieba.cut(cleaned_line)
    # 去除停用词
    filtered_words = [word for word in words if word not in stop_words]
    # 返回处理后的单词列表
    return filtered_words

# 处理文件并保存结果
def process_file(file_path, output_file_path, stop_words):
    with open(file_path, 'r', encoding='utf-8') as file, \
         open(output_file_path, 'w', encoding='utf-8') as output:
        for line in file:
            # 按行清洗、分词并去除停用词
            processed_line = clean_segment_and_remove_stop_words(line, stop_words)
            # 将处理后的单词列表转换为字符串，并写入新文件
            output.write(' '.join(processed_line) + '\n')

# 指定原始文本文件路径、输出文件路径和停用词文件路径
file_path = 'D:\\pycharm\\pycharmProjects\\caiyukou\\ai\\normal.txt'
output_file_path = 'D:\\pycharm\\pycharmProjects\\caiyukou\\ai\\normal_01.txt'
stop_words_file_path = 'D:\\pycharm\\pycharmProjects\\caiyukou\\ai\\stop.txt'
# 加载停用词
stop_words = load_stop_words(stop_words_file_path)
# 处理文件并保存结果
process_file(file_path, output_file_path, stop_words)