import pandas as pd
import numpy as np
import pickle as pkl


# 读取txt文件，转为pandas.core.frame.DataFrame
df = pd.read_csv('.\\originData\\sms_with_label.txt', sep='\t', header=None, names=['Label', 'Content'])


# 交换Label与Content列
df = df[['Content', 'Label']]




# 去除缺失值，去除重复项
df = df.dropna(how='all').reset_index(drop=True)  # 删除所有值为NaN的行
df = df.drop_duplicates(subset=['Content'], keep=False)  # 删除内容重复的行


# 保存为.pickle
with open('.\\data\\sms_data.pickle', 'wb') as f:
    pkl.dump(df, f)

# 分开正负样本
# neg = df[df['Label'] == 0]
# pos = df[df['Label'] == 1]
groups = df.groupby(df.Label)
neg = groups.get_group(0)
pos = groups.get_group(1)
# neg_per = "{:.2%}".format(len(neg)/len(df))
# pos_per = "{:.2%}".format(len(pos)/len(df))
# print("Negative: Length={len}, Proportion={per}".format(len=len(neg), per=neg_per))
# print("Positive: Length={len}, Proportion={per}".format(len=len(pos), per=pos_per))


# 样本均衡，采取欠抽样(数据集大，不会丢失太多信息)
# 欠抽样（也叫下采样、under-sampling）方法通过减少分类中多数类样本的样本数量来实现样本均衡，最直接的方法是随机地去掉一些多数类样本来减小多数类的规模，缺点是会丢失多数类样本中的一些重要信息。
# 1:1不一定好，偏离现实
neg_new = neg.sample(frac=1.0, replace=False).sample(frac=0.006).reset_index(drop=True)  # 按100%的比例(无放回,默认)抽样即达到打乱数据的效果，重置index，按比例随机采样
pos_new = pos.sample(frac=1.0, replace=False).sample(frac=0.05).reset_index(drop=True)
# neg_new_per = "{:.2%}".format(len(neg_new)/len(df))
# neg_new_per = "{:.2%}".format(len(pos_new)/len(df))
# print("Negative: Length={len}, Proportion={per}".format(len=len(neg_new), per=neg_new_per))
# print("Positive: Length={len}, Proportion={per}".format(len=len(pos_new), per=pos_new_per))


# 生成训练集、验证集、测试集
train = pd.concat([neg_new, pos_new]).sample(frac=1.0).reset_index(drop=True)  # 训练集样本均衡
# print("训练集Shape: {train_shape}".format(train_shape=train.shape))
# print("原数据Shape: {df_shape}".format(df_shape=df.shape))
df_remains = pd.concat([df, train]).drop_duplicates(['Content', 'Label'], keep=False).reset_index(drop=True)  # keep=False 表示删除所有重复项
# print("剩余数据Shape: {diff_shape}".format(diff_shape=df_remains.shape))
# if df.shape[0]-df_remains.shape[0] == train.shape[0]:
#     print("true")
# else:
#     print("False")
valid_per = float("{:.4f}".format(len(train)/3/len(df_remains)))
valid = df_remains.sample(frac=valid_per)
# print("验证集Shape: {valid_shape}".format(valid_shape=valid.shape))
test = pd.concat([df_remains, valid]).drop_duplicates(['Content', 'Label'], keep=False).sample(frac=valid_per).reset_index(drop=True)
# print("测试集Shape:{test_shape}".format(test_shape=test.shape))
#
# print("{:0f}".format(train.shape[0]/valid.shape[0]))
# print("{:0f}".format(train.shape[0]/test.shape[0]))
# print("{:0f}".format(valid.shape[0]/test.shape[0]))


# 生成适应数据集 https://colab.research.google.com/drive/17O3_eJ9atT4ZUw3qc2brBBg1xizkzPoD#scrollTo=hM8M7k0gKk5H
df_small = (train, test)
with open('.\\data\\sms_data_small.pickle', 'wb') as f:
    pkl.dump(df_small, f)



