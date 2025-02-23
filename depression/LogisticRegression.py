# _*_coding : utf-8 _*_
# @Time : 2024/6/4 20:05
# @Author : hosee
# @File : 04
# @Project : caiyukou
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 加载数据
with open("die_01.txt", "r", encoding="utf-8") as f:
    die_data = f.readlines()

with open("normal_01.txt", "r", encoding="utf-8") as f:
    normal_data = f.readlines()

# 合并数据
data = die_data + normal_data

# 标签
labels = [1] * len(die_data) + [0] * len(normal_data)

# 文本预处理
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)
# 训练模型
model = LogisticRegression()
model.fit(X_train, y_train)
# 测试模型
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.4f}")

test_data = ["今天好难过，一点都不开心"]

# 将测试数据转换为数值向量
X_test = vectorizer.transform(test_data)

# 使用模型进行预测
y_pred = model.predict(X_test)

# 打印预测结果
for i, text in enumerate(test_data):
    print(f"Text: {text}")
    print(f"Predicted Label: {y_pred[i]}")


