# _*_coding : utf-8 _*_
# @Time : 2024/5/31 22:40 
# @Author : hosee
# @File : 03
# @Project : caiyukou
import paddlehub as hub

# 加载模型
senta = hub.Module(name="senta_lstm")

# # 待分类文本
# test_text = ["好崩溃每天都是折磨真的生不如死", "姐姐   我可以去找你吗","内心阴暗至极……","大家今晚都是因为什么没睡","既然儿子那么好     那就别生下我啊     生下我又把我扔下     让我自生自灭     这算什么","走饭小姐姐怎么办我该怎么办每天都心酸心如刀绞每天都有想要死掉的念头我不想那么痛苦了"]

with open("/ai/die.txt", 'r', encoding='utf-8') as f:
    test_text = []
    for line in f:
        test_text.append(line.strip())

# 情感分类
results = senta.sentiment_classify(data={"text": test_text})

# 得到结果
for result in results:
    print(result)

