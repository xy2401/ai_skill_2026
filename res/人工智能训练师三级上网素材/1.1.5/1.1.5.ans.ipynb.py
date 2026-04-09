import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 数据采集
# 从本地文件中读取数据  2分
data = pd.read_csv('vehicle_traffic_data.csv')
print("数据采集完成，已加载到DataFrame中")

# 打印数据的前5条记录 2分
print(data.head())


# 2. 数据清洗与预处理
# 处理缺失值（删除）  2分
data = data.dropna()

# 数据类型转换
data['Age']= data['Age'].astype(int)       #Age数据类型转换为int 1分
data['Speed']= data['Speed'].astype(float)     #Speed数据类型转换为float 1分
data['TravelDistance'] = data['TravelDistance'].astype(float)     #TravelDistance数据类型转换为float 1分
data['TravelTime'] = data['TravelTime'].astype(float)     #TravelTime数据类型转换为float 1分

# 处理异常值  2分
data = data[(data['Age'].between(18, 70))  & 
            (data['Speed'].between(0, 200)) & 
            (data['TravelDistance'].between(1, 1000)) & 
            (data['TravelTime'].between(1, 1440))]

# 保存清洗后的数据  1分
data.to_csv('cleaned_vehicle_traffic_data.csv', index=False)
print("数据清洗完成，已保存为 'cleaned_vehicle_traffic_data.csv'")


# 3. 数据合理性审核
# 审核字段合理性 1分
unreasonable_data = data[~((data['Age'].between(18, 70)) & 
                           (data['Speed'].between(0, 200)) & 
                           (data['TravelDistance'].between(1, 1000)) & 
                           (data['TravelTime'].between(1, 1440)))]
print("不合理的数据:\n", unreasonable_data)

# 4. 数据统计
# 统计每种交通事件的发生次数  2分
traffic_event_counts = data['TrafficEvent'].value_counts()
print("每种交通事件的发生次数:\n", traffic_event_counts)

# 统计不同性别的平均车速、行驶距离和行驶时间  2分
gender_stats = data.groupby('Gender').agg({'Speed':'mean','TravelDistance':'mean','TravelTime':'mean'})
print("不同性别的平均车速、行驶距离和行驶时间:\n", gender_stats)

# 统计不同年龄段的驾驶员数  5分
age_bins = [18, 26, 36, 46, 56, 66, np.inf]
age_labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
data['AgeGroup'] = pd.cut(data['Age'],bins=age_bins,labels=age_labels, right=False)
age_group_counts = data['AgeGroup'].value_counts()
print("不同年龄段的驾驶员数:\n", age_group_counts)
