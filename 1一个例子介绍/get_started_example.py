#-*- coding: utf-8 -*-
# 导入库
import re
import numpy
from sklearn import linear_model
from matplotlib import pyplot as plt

# 导入数据
fn = open('data.txt', 'r')
all_data = fn.readlines()
fn.close()

# 数据预处理
x = []
y = []
for single_data in all_data:
    tmp_data = re.split('\t|\n', single_data)
    x.append(float(tmp_data[0]))
    y.append(float(tmp_data[1]))

x = numpy.array(x).reshape([-1, 1])
y = numpy.array(y).reshape([-1, 1])


print(x)
# 数据分析展示
plt.scatter(x, y)
plt.show()

# 数据建模
model = linear_model.LinearRegression()
model.fit(x, y)

# 模型评估
model_coef = model.coef_
model_intercept = model.intercept_
r2 = model.score(x, y)

# 销售预测
new_x = 84610
pre_y = model.predict(new_x)
print (pre_y)
