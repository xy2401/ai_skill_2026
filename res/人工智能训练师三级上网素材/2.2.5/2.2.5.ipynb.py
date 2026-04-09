import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import pickle
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 加载数据集
df = __________

# 显示前五行数据
print(__________)

# 选择相关特征进行建模
X = df[['Your gender ', 'How important is exercise to you ?', 'How healthy do you consider yourself?']]
X = __________(X)  # 将分类变量转为数值变量

# 设置目标变量
y = __________  

# 将数据集划分为训练集和测试集（测试集占20%）
X_train, X_test, y_train, y_test = __________(__________, random_state=42)

# 创建并训练决策树回归模型
__________ = __________(random_state=42)
# 训练决策树回归模型
__________

# 保存训练好的模型
with open('2.2.5_model.pkl', 'wb') as model_file:
    pickle.__________

# 进行预测
y_pred = __________

# 将结果保存到文本文件中
results = pd.DataFrame({'实际值': y_test, '预测值': y_pred})
results_filename = '2.2.5_results.txt'
__________(__________, index=False, sep='\t')  

# 将测试结果保存到报告文件中
report_filename = '2.2.5_report.txt'
with open(__________) as f:
    f.write(f'均方误差: {__________}\n')
    f.write(f'平均绝对误差: {__________}\n')
    f.write(f'决定系数: {__________}\n')


