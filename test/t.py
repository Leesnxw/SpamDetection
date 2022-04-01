import pandas as pd

data = {

    'A': [1, 3, 3, 3],
    'B': [0, 1, 2, 0],
    'C': [4, 5, 4, 4],
    'D': [3, 3, 3, 3]
}
df = pd.DataFrame(data=data)
# 去除所有重复项，对于B列来说两个0是重复项
print(df)
# df = df.drop_duplicates(subset=['B'], keep=False)
# # 简写，省去subset参数
# # df.drop_duplicates(['B'],keep=False)
# print(df)

data_1 = {

    'A': [1, 3],
    'B': [0, 1],
    'C': [4, 5],
    'D': [3, 3]
}

df_1 = pd.DataFrame(data=data_1)
print(df_1)

df = pd.concat([df, df_1])
print(df)
df = df.drop_duplicates(['A', 'B', 'C', 'D'], keep=False)
print(df)

# file = open('.\\originData\\sms_with_label.txt', 'r+', encoding='UTF-8')
# lines = file.readlines()
# print(lines[0])
#
# for line in lines:
#     line.strip()