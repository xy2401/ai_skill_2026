import pandas as pd

# 加载数据集并显示数据集的前五行 1分
data = __________
print("数据集的前五行:")
print(__________)

# 显示每一列的数据类型
print(data.dtypes)

# 检查缺失值并删除缺失值所在的行  2分
print("\n检查缺失值:")
print(__________.__________.__________)  
data = __________

# 将 'horsepower' 列转换为数值类型，并（删除）处理转换中的异常值 1分
data['horsepower'] = __________(data['horsepower'], errors='coerce')
data = __________

# 显示每一列的数据类型
print(data.horsepower.dtypes)

# 检查清洗后的缺失值
print("\n检查清洗后的缺失值:")
print(data.isnull().sum())

from sklearn.preprocessing import StandardScaler
# 对数值型数据进行标准化处理 1分
numerical_features = ['displacement', 'horsepower', 'weight', 'acceleration']
scaler = StandardScaler()
data[numerical_features] = __________

from sklearn.model_selection import train_test_split
# 选择特征、自变量和目标变量 2分
selected_features = __________
X = __________
y = __________

# 划分数据集为训练集和测试集（训练集占8成） 1分
X_train, X_test, y_train, y_test = __________(__________, random_state=42)


# 将特征和目标变量合并到一个数据框中
cleaned_data = X.copy()
cleaned_data['mpg'] = y

# 保存清洗和处理后的数据（不存储额外的索引号） 1分
__________('2.1.1_cleaned_data.csv', __________)

# 打印消息指示文件已保存
print("\n清洗后的数据已保存到 2.1.1_cleaned_data.csv")


