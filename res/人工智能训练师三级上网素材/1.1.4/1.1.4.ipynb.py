import pandas
import numpy as np
import matplotlib.pyplot as plt

# 1. 数据采集
# 从本地文件中读取数据  2分
data =  _______________________________
print("数据采集完成，已加载到DataFrame中")

# 打印数据的前5条记录  2分
print(________________________________)


# 2. 数据清洗与预处理
# 处理缺失值（删除）  2分
data = ________________________________

# 数据类型转换
data________________ = ________________(int)   # Age数据类型转换为int 2分
data________________ = ________________(float) # PurchaseAmount数据类型转换为float  2分
data________________ = ________________(int)   # ReviewScore数据类型转换为int 2分

# 处理异常值  2分
data = data[(________________.________________(18, 70)) & 
            (data['PurchaseAmount'] > 0) & 
            (________________.________________(1, 5))]

# 数据标准化
data['PurchaseAmount'] = (data['PurchaseAmount'] - ________________) / ________________  # PurchaseAmount数据标准化 2分
data['ReviewScore'] = (data['ReviewScore'] - ________________) / ________________        # ReviewScore数据标准化 2分

# 保存清洗后的数据  1分
________________('cleaned_user_behavior_data.csv', index=False)
print("数据清洗完成，已保存为 'cleaned_user_behavior_data.csv'")


# 3. 数据统计
# 统计每个购买类别的用户数 2分
purchase_category_counts = ________________.________________
print("每个购买类别的用户数:\n", purchase_category_counts)

# 统计不同性别的平均购买金额 2分
gender_purchase_amount_mean = ________________(________________)['PurchaseAmount'].mean()
print("不同性别的平均购买金额:\n", gender_purchase_amount_mean)

# 统计不同年龄段的用户数 2分
bins = [18, 26, 36, 46, 56, 66, np.inf]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
data['AgeGroup'] = pandas.________________(________________, right=False)
age_group_counts = data['AgeGroup'].value_counts().sort_index()
print("不同年龄段的用户数:\n", age_group_counts)
