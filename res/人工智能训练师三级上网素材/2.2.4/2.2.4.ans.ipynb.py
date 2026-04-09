import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from xgboost import XGBRegressor

# 加载数据集
data = pd.read_excel('大学生低碳生活行为的影响因素数据集.xlsx')

# 显示数据集的前五行
print(data.head())
print(data.columns.to_list()) # 显示数据集的列名列表

# 删除不必要的列并处理分类变量
data_cleaned = data.drop(columns=['序号', '所用时间'])  # 删除不必要的列
data_cleaned = pd.get_dummies(data_cleaned, drop_first=True)  # 将分类变量转换为哑变量/指示变量

# 定义目标变量和特征
target = '5.您进行过绿色低碳的相关生活方式吗?'  # 确保这是目标变量

# 定义自变量和因变量
X = data_cleaned.drop(columns=[target])
y = data_cleaned[target]

# 将数据拆分为训练集和测试集（测试集占20%）
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

# 初始化线性回归模型
model = LinearRegression()
# 训练线性回归模型
model.fit(X_train,y_train)

# 保存训练好的模型
model_filename = '2.2.4_model.pkl'
joblib.dump(model, model_filename)

# 进行预测
y_pred = model.predict(X_test)

# 将结果保存到文本文件中
results = pd.DataFrame({'实际值': y_test, '预测值': y_pred})
results_filename = '2.2.4_results.txt'
results.to_csv(results_filename, index=False, sep='\t')  # 使用制表符分隔值保存到文本文件

# 将测试结果保存到报告文件中
report_filename = '2.2.4_report.txt'
with open(report_filename, 'w') as f:
    f.write(f'均方误差: {mean_squared_error(y_test,y_pred)}\n')
    f.write(f'决定系数: {r2_score(y_test,y_pred)}\n')
    
# 分析并纠正错误（示例：使用XGBoost）
# 初始化XGBoost模型（设定树的数量为1000，学习率为0.05，每棵树的最大深度为5，）
xgb_model = XGBRegressor(n_estimators=1000, subsample=0.8, colsample_bytree=0.8)
# 训练XGBoost模型
xgb_model.fit(X_train,y_train)

# 使用XGBoost模型进行预测
y_pred_xg = xgb_model.predict(X_test)

# 将XGBoost结果保存到文本文件中
results_xg_filename = '2.2.4_results_xg.txt'
results_xg = pd.DataFrame({'实际值': y_test, '预测值': y_pred_xg})
results_xg.to_csv(results_xg_filename, index=False, sep='\t')  # 使用制表符分隔值保存到文本文件

# 将XGBoost测试结果保存到报告文件中
report_filename_xgb = '2.2.4_report_xgb.txt'
with open(report_filename_xgb, 'w') as f:
    f.write(f'均方误差: {mean_squared_error(y_test,y_pred_xg)}\n')
    f.write(f'决定系数: {r2_score(y_test,y_pred_xg)}\n')


