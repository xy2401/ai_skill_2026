import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
from sklearn.metrics import mean_squared_error, r2_score
import xgboost as xgb

# 加载数据集
df = pd.read_csv('fitness analysis.csv')

# 显示前五行数据
print(df.head())

# 去除所有字符串字段的前后空格
#df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)


# 检查和清理列名
df.columns = df.columns.str.strip()

# 选择相关特征进行建模
X = df[['Your gender', 'How important is exercise to you ?', 'How healthy do you consider yourself?']]
X = pd.get_dummies(X)  # 将分类变量转为数值变量

# 将年龄段转为数值变量
y = df['Your age'].apply(lambda x: int(x.split(' ')[0]))  # 假设年龄段为整数

# 将数据集划分为训练集和测试集（测试集占比20%）
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

# 创建随机森林回归模型（创建的决策树的数量为100）
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
# 训练随机森林回归模型
rf_model.fit(X_train,y_train)

# 保存训练好的模型
with open('2.2.3_model.pkl', 'wb') as model_file:
    pickle.dump(rf_model,model_file)

# 进行结果预测
y_pred = rf_model.predict(X_test)
results_df = pd.DataFrame(y_pred, columns=['预测结果'])
results_df.to_csv('2.2.3_results.txt', index=False)

# 使用测试工具对模型进行测试，并记录测试结果
train_score = rf_model.score(X_train, y_train)   #训练集分数
test_score = rf_model.score(X_test,y_test)    #测试集分数
mse = mean_squared_error(y_test, y_pred)  #均方误差
r2 = r2_score(y_test, y_pred)  #决定系数
with open('2.2.3_report.txt', 'w') as report_file:
    report_file.write(f'训练集得分: {train_score}\n')
    report_file.write(f'测试集得分: {test_score}\n')
    report_file.write(f'均方误差(MSE): {mse}\n')
    report_file.write(f'决定系数(R^2): {r2}\n')

# 运用工具分析算法中错误案例产生的原因并进行纠正
# 初始化XGBoost回归模型（构建100棵树）
xgb_model = xgb.XGBRegressor(n_estimators=100, random_state=42)
# 训练XGBoost回归模型
xgb_model.fit(X_train,y_train)
# 使用XGBoost回归模型在测试集上进行结果预测
y_pred_xgb = xgb_model.predict(X_test)

results_df_xgb = pd.DataFrame(y_pred_xgb, columns=['预测结果'])
results_df_xgb.to_csv('2.2.3_results_xgb.txt', index=False)

with open('2.2.3_report_xgb.txt', 'w') as xgb_report_file:
    xgb_report_file.write(f'XGBoost训练集得分: {xgb_model.score(X_train,y_train)}\n')
    xgb_report_file.write(f'XGBoost测试集得分: {xgb_model.score(X_test,y_test)}\n')
    xgb_report_file.write(f'XGBoost均方误差(MSE): {mean_squared_error(y_test,y_pred_xgb)}\n')
    xgb_report_file.write(f'XGBoost决定系数(R^2): {r2_score(y_test, y_pred_xgb)}\n')


