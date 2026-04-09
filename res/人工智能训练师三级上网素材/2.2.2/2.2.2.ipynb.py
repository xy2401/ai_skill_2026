import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pickle
from sklearn.ensemble import RandomForestRegressor

# 加载数据集
df = __________

# 显示前五行数据
print(__________)

# 处理缺失值
# 将 'horsepower' 列中的所有值转换为数值类型
df['horsepower'] = __________(__________, errors='coerce')
# 删除包含缺失值的行
df = __________

# 选择相关特征进行建模（定义自变量（返回一个DataFrame）和因变量）
X = __________
y = __________

# 将数据集划分为训练集和测试集（测试集占比20%）
X_train, X_test, y_train, y_test = __________(__________, random_state=42)

# 创建包含标准化和线性回归的管道
pipeline = __________([('scaler', __________),('linreg', __________)])

# 训练模型
__________

# 保存训练好的模型
with open('2.2.2_model.pkl', 'wb') as model_file:
    pickle.__________

# 预测并保存结果
y_pred = __________
results_df = pd.DataFrame(y_pred, columns=['预测结果'])
__________('2.2.2_results.txt', index=False)

# 测试模型
with open('2.2.2_report.txt', 'w') as results_file:
    results_file.write(f'训练集得分: {pipeline.score(X_train, y_train)}\n')
    results_file.write(f'测试集得分: {pipeline.score(X_test, y_test)}\n')

# 创建随机森林回归模型实例（创建的决策树的数量为100）
rf_model = __________(__________, random_state=42)
# 训练随机森林回归模型
__________

# 使用随机森林模型进行预测
y_pred_rf = __________

# 保存新的结果
results_rf_df = pd.DataFrame(y_pred_rf, columns=['预测结果'])
__________('2.2.2_results_rf.txt', index=False)

# 测试模型并保存得分
with open('2.2.2_report_rf.txt', 'w') as results_rf_file:
    results_rf_file.write(f'训练集得分: {rf_model.score(X_train, y_train)}\n')
    results_rf_file.write(f'测试集得分: {rf_model.score(X_test, y_test)}\n')




