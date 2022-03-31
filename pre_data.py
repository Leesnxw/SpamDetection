import pandas as pd
import pickle as pkl

# 读取txt文件，转为pandas.core.frame.DataFrame
data = pd.read_csv('.\\originData\\sms_with_label.txt', sep='\t', header=None, names=['Label', 'Content'])
# print(type(data))
# print(data)

# 交换Label与Content列
data = data[['Content', 'Label']]
# print(data)


# 预览pickle文件内容
def view_pkl(fpath):
    file = open(fpath, 'rb')
    info = pkl.load(file)
    print(info)


# 保存为.pickle
data_path = '.\\data\\sms_data.pickle'
with open(data_path, 'wb') as f:
    pkl.dump(data, f)
view_pkl(data_path)


# 预览pickle文件内容
# f_path = 'D:\\Documents\\dianping_train_test.pickle'
# file = open(f_path, 'rb')
# info = pkl.load(file)
# print(info)
# print(type(info))
# print(len(info))
#
# print(info[0])  # [1600 rows x 2 columns] -train data
# print(info[-1])  # [400 rows x 2 columns] -test data
# print(type(info[-1]))  # pandas.core.frame.DataFrame
