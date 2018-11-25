# -*- coding: utf-8 -*-
import pandas as pd  # 导入pandas库
import numpy as np  # 导入numpy库
from sklearn.preprocessing import Imputer  # 导入sklearn.preprocessing中的Imputer库
####################################################################


####################################################################
# 3.4 解决样本类别分布不均衡的问题
import pandas as pd
from imblearn.over_sampling import SMOTE  # 过抽样处理库SMOTE
from imblearn.under_sampling import RandomUnderSampler  # 欠抽样处理库RandomUnderSampler
from sklearn.svm import SVC  # SVM中的分类算法SVC
from imblearn.ensemble import EasyEnsemble  # 简单集成方法EasyEnsemble

# 导入数据文件
# 导入相关库
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
import pandas as pd
import jieba.analyse
import  pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer  # 基于TF-IDF的词频转向量库

# 3.10 离散化，对连续运营数据做逻辑分层
# 读取自然语言文件
fn = open('text.txt',encoding="utf-8")
string_lines = fn.readlines()
fn.close()

# 中文分词
seg_list = []  # 建立空列表，用于存储所有分词结果
for string_line in string_lines:  # 读取每行数据
    each_list = jieba.cut(string_line)  # 返回每行的分词结果
    seg_list.append(each_list)  # 分词结果添加到结果列表
for i in range(5):  # 打印输出第一行的前5条数据
    print (seg_list[1][i])

# word to vector
stop_words = [u'\n', u'/', u'“', u'”', u'的', u'，', u'和', u'是', u'随着', u'对于', u'对', u'等', u'能', u'都', u'。', u'、',
              u'中', u'与', u'在', u'其']  # 自定义要去除的无用词
vectorizer = TfidfVectorizer(stop_words=stop_words, tokenizer=jieba.cut)  # 创建词向量模型
X = vectorizer.fit_transform(string_lines)  # 将文本数据转换为向量空间模型
vector = vectorizer.get_feature_names()  # 获得词向量
vector_value = X.toarray()  # 获得词向量值
vector_pd = pd.DataFrame(vector_value, columns=vector)  # 创建用于展示的数据框
print (vector_pd.head(1))  # 打印输出第一条数据
