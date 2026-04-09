import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE

# 加载数据
data = pd.read_csv('finance数据集.csv')

# 显示前五行的数据
print(data.head())

# 选择自变量和因变量
X = data.drop(['SeriousDlqin2yrs', 'Unnamed: 0'], axis=1)
y = data['SeriousDlqin2yrs']

# 分割训练集和测试集（测试集20%）
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

# 训练Logistic回归模型（最大迭代次数为1000次）
model = LogisticRegression(max_iter=1000)
#训练 Logistic 回归模型
model.fit(X_train,y_train)

# 保存模型
with open('2.2.1_model.pkl', 'wb') as file:
    pickle.dump(model,file)

# 预测并保存结果
y_pred = model.predict(X_test)
pd.DataFrame(y_pred, columns=['预测结果']).to_csv('2.2.1_results.txt', index=False)

# 生成测试报告
report = classification_report(y_test, y_pred, zero_division=1)
with open('2.2.1_report.txt', 'w') as file:
    file.write(report)

# 分析测试结果
accuracy = (y_test==y_pred).mean()
print(f"模型准确率: {accuracy:.2f}")

# 处理数据不平衡
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# 重新训练模型
model.fit(X_resampled, y_resampled)
# 重新预测
y_pred_resampled =  model.predict(X_test)

# 保存新结果
pd.DataFrame(y_pred_resampled, columns=['预测结果']).to_csv('2.2.1_results_xg.txt', index=False)

# 生成新的测试报告
report_resampled = classification_report(y_test, y_pred_resampled, zero_division=1)
with open('2.2.1_report_xg.txt', 'w') as file:
    file.write(report_resampled)

# 分析新的测试结果
accuracy_resampled = (y_test==y_pred_resampled).mean()
print(f"重新采样后的模型准确率: {accuracy_resampled:.2f}")


