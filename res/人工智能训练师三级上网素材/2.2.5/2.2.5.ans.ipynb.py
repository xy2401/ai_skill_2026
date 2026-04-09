import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import pickle
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 加载数据集
df = pd.read_csv('fitness analysis.csv')

# 显示前五行数据
print(df.head())

# 选择相关特征进行建模
X = df[['Your gender ', 'How important is exercise to you ?', 'How healthy do you consider yourself?']]
X = pd.get_dummies(X)  # 将分类变量转为数值变量

# 设置目标变量
y = df['daily_steps']  

# 将数据集划分为训练集和测试集（测试集占20%）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建并训练决策树回归模型
dt_model = DecisionTreeRegressor(random_state=42)
# 训练决策树回归模型
dt_model.fit(X_train,y_train)

# 保存训练好的模型
with open('2.2.5_model.pkl', 'wb') as model_file:
    pickle.dump(dt_model,model_file)

# 进行预测
y_pred = dt_model.predict(X_test)

# 将结果保存到文本文件中
results = pd.DataFrame({'实际值': y_test, '预测值': y_pred})
results_filename = '2.2.5_results.txt'
results.to_csv(results_filename, index=False, sep='\t')  

# 将测试结果保存到报告文件中
report_filename = '2.2.5_report.txt'
with open(report_filename, 'w') as f:
    f.write(f'均方误差: {mean_squared_error(y_test,y_pred)}\n')
    f.write(f'平均绝对误差: {mean_absolute_error(y_test,y_pred)}\n')
    f.write(f'决定系数: {r2_score(y_test,y_pred)}\n')


