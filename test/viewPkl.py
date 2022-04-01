import pickle

# 预览pickle文件内容
print(pickle.load(open('.\\data\\sms_data.pickle', 'rb')))
print(pickle.load(open('.\\data\\sms_data_small.pickle', 'rb')))
