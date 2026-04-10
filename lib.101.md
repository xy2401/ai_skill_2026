# 人工智能训练师（三级）Python 核心类库快速入门指南 (lib.101)

本指南基于“二十题”代码答案总结，详细介绍了在考试中频繁使用的 Python 类库及核心函数。

---

## 1. 数据处理核心 (Pandas & Numpy)

### **Pandas (`import pandas as pd`)**
*用途：表格数据（CSV/Excel）的清洗、处理、统计。*

*   **`read_csv` / `read_excel`**: 读取外部数据。
*   **`data.head()`**: 查看数据前几行。
*   **`data.columns.to_list()`**: 获取列名列表。
*   **`isnull().sum()`**: **(常用)** 统计每列缺失值数量。
*   **`pd.to_numeric`**: **(必考)** 将列转换为数值类型，`errors='coerce'` 会将无法转换的值设为 NaN。
*   **`cut`**: **(必考)** 用于“分箱”或“离散化”。例如：将年龄划分为“青年”、“中年”、“老年”。
*   **`get_dummies`**: **(必考)** 独热编码（One-Hot Encoding）。将分类变量转换为 0/1 矩阵。
*   **`to_datetime`**: 将字符串转为日期格式。
*   **`isin()`**: 判断值是否在给定的列表中。
*   **`value_counts()`**: 统计某一列中每个值出现的次数。
*   **`groupby()`**: 分组操作。常配合 `mean()`, `sum()`, `count()`, `agg(['mean', 'count'])` 使用。
*   **`apply()`**: 对每一行或每一列执行自定义函数。
*   **`fillna()` / `dropna()`**: 处理缺失值。`dropna(subset=['col'])` 仅针对特定列删除。
*   **`ffill()` / `bfill()`**: 前向/后向填充缺失值。
*   **`drop(columns=['col'])`**: 删除指定列。
*   **`to_csv('file.csv', index=False)`**: 保存数据，通常不保存索引。`sep='\t'` 可保存为制表符分隔。

### **Numpy (`import numpy as np`)**
*用途：高性能数值计算、矩阵处理。*

*   **`array`**: 创建数组（矩阵）。
*   **`where(condition, x, y)`**: **(常用)** 条件赋值。
*   **`argmax`**: 返回数组中最大值的索引（常用于多分类结果解析）。
*   **`argsort`**: 返回数组排序后的索引（如：`[-5:][::-1]` 获取 Top-5 索引）。
*   **`expand_dims(img, axis=0)`**: **(常用)** 在指定维度增加一个轴，常用于增加 Batch 维度。
*   **`inf`**: 代表无穷大，常用于定义分箱的边界。
*   **`transpose`**: 矩阵转置。

---

## 2. 机器学习建模 (Scikit-Learn & XGBoost)

### **预处理 (`sklearn.preprocessing`)**
*   **`StandardScaler`**: 标准化。
*   **`MinMaxScaler`**: 归一化。
*   **`LabelEncoder`**: 标签编码。
*   **`fit_transform`**: 一步执行拟合与转换。

### **模型准备与评估 (`sklearn.model_selection` & `metrics`)**
*   **`train_test_split`**: **(必考)** 划分训练集和测试集。常用参数：`test_size=0.2`, `random_state=42`。
*   **`r2_score`**: 评估回归模型的拟合优度。
*   **`mean_squared_error (MSE)`**: 均方误差。
*   **`mean_absolute_error (MAE)`**: 平均绝对误差。

### **模型算法**
*   **`LinearRegression`**: 线性回归。
*   **`DecisionTreeRegressor`**: 决策树回归。
*   **`RandomForestRegressor`**: 随机森林回归。
*   **`XGBRegressor`**: **(热门)** XGBoost 算法。常用参数：`n_estimators`, `subsample`, `colsample_bytree`。

---

## 3. 图像处理与计算机视觉 (OpenCV & PIL)

### **OpenCV (`import cv2`)**
*   **`imread` / `imwrite`**: 读取和保存图像。
*   **`cvtColor`**: 颜色空间转换（`cv2.COLOR_BGR2RGB`）。
*   **`resize`**: 缩放图像至模型指定大小（如 `(224, 224)` 或 `(320, 240)`）。
*   **`rectangle`**: 在图上画框。

### **PIL (Pillow)**
*   **`Image.open`**: 读取图片。常用 `.convert('RGB')` 确保通道统一。

---

## 4. 可视化 (Matplotlib & Seaborn)

### **Matplotlib (`import matplotlib.pyplot as plt`)**
*   **`figure`**, **`subplot`**, **`scatter`**, **`legend`**。
*   **`FontProperties`**: 解决中文显示问题。

### **Seaborn (`import seaborn as sns`)**
*   **`boxplot`**: 箱线图。

---

## 5. 模型部署与工具 (ONNX & System)

### **ONNX Runtime (`import onnxruntime as ort`)**
*   **`InferenceSession`**: **(三级必考)** 加载 `.onnx` 模型并进行推理。
*   **`get_inputs()[0].name`**: 获取输入节点名称。
*   **`run([output_name], {input_name: data})`**: 模型推理。第一个参数为 `None` 时返回所有输出。

### **系统与持久化**
*   **`os.makedirs`**: 递归创建目录。
*   **`joblib.dump` / `joblib.load`**: **(必考)** 保存和加载训练好的模型文件。
*   **`time`**: 计算代码执行耗时。
*   **`scipy.special.softmax`**: 将推理结果转换为概率。

---

## 快速速查表 (Cheat Sheet)

| 任务 | 常用函数 |
| :--- | :--- |
| **数据清洗** | `data.dropna()`, `data.fillna()`, `data.isnull().sum()`, `pd.to_numeric()` |
| **特征转换** | `pd.get_dummies(data)`, `pd.cut(data['age'], bins)` |
| **数据划分** | `train_test_split(X, y, test_size=0.2, random_state=42)` |
| **模型训练** | `model.fit(X_train, y_train)` |
| **模型预测** | `y_pred = model.predict(X_test)` |
| **模型推理** | `session.run(None, {input_name: img})` |
| **图片预处理** | `cv2.resize(img, (224, 224))`, `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` |
| **保存模型** | `joblib.dump(model, 'model.pkl')` |
