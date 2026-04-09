import pandas as pd
#读取一个Excel文件，并将读取到的数据存储在变量data中
data = __________
#打印出数据集的前5行
print(data.head())

#处理数据集中的缺失值
initial_row_count = __________   #处理前的数据行数
data = __________                #删除缺失值所在行
final_row_count = __________     #处理后的数据行数
print(f'处理后数据行数: {final_row_count}, 删除的行数: {initial_row_count - final_row_count}')

#删除重复行
data = __________

from sklearn.preprocessing import StandardScaler
numerical_features = ['4.您的月生活费○≦1,000元   ○1,001-2,000元   ○2,001-3,000元   ○≧3,001元']
scaler = StandardScaler()
data[numerical_features] = __________

#选择特征
selected_features = [__________]
X = __________

# 创建目标变量
y = __________

from sklearn.model_selection import train_test_split
# 数据划分（测试集取20%）
X_train, X_test, y_train, y_test = __________(__________, random_state=42)

# 合并处理后得数据，并将其保存（保存中不用额外创建索引）
cleaned_data = __________(__________, axis=1)
__________('2.1.2_cleaned_data.csv', __________)


