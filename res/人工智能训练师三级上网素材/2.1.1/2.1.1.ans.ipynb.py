import pandas as pd

# 加载数据集并显示数据集的前五行 1分
data = pd.read_csv('auto-mpg.csv')
print("数据集的前五行:")
print(data.head())

# 显示每一列的数据类型
print(data.dtypes)

# 检查缺失值并删除缺失值所在的行  2分
print("\n检查缺失值:")
print(data.isnull().sum())  
data = data.dropna()

# 将 'horsepower' 列转换为数值类型，并（删除）处理转换中的异常值 1分
data['horsepower'] = pd.to_numeric(data['horsepower'], errors='coerce')
data = data.dropna(subset=['horsepower'])

# 显示每一列的数据类型
print(data.horsepower.dtypes)

# 检查清洗后的缺失值
print("\n检查清洗后的缺失值:")
print(data.isnull().sum())

from sklearn.preprocessing import StandardScaler
# 对数值型数据进行标准化处理 1分
numerical_features = ['displacement', 'horsepower', 'weight', 'acceleration']
scaler = StandardScaler()
data[numerical_features] = scaler.fit_transform(data[numerical_features])

from sklearn.model_selection import train_test_split
# 选择特征、自变量和目标变量 2分
selected_features = ['cylinders','displacement','horsepower','weight','acceleration','model year','origin']
X = data[selected_features]
y = data['mpg']

# 划分数据集为训练集和测试集（训练集占8成） 1分
X_train, X_test, y_train, y_test =  train_test_split(X,y,train_size=0.8, random_state=42)


# 将特征和目标变量合并到一个数据框中
cleaned_data = X.copy()
cleaned_data['mpg'] = y

# 保存清洗和处理后的数据（不存储额外的索引号） 1分
cleaned_data.to_csv('2.1.1_cleaned_data.csv', index=False)

# 打印消息指示文件已保存
print("\n清洗后的数据已保存到 2.1.1_cleaned_data.csv")


