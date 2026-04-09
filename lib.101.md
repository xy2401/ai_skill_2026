# 人工智能训练师（三级）Python 核心类库快速入门指南 (lib.101)

本指南基于“二十题”代码答案总结，详细介绍了在考试中频繁使用的 Python 类库及核心函数。

---

## 1. 数据处理核心 (Pandas & Numpy)

### **Pandas (`import pandas as pd`)**
*用途：表格数据（CSV/Excel）的清洗、处理、统计。*

*   **`read_csv` / `read_excel`**: 读取外部数据。
*   **`DataFrame`**: Pandas 的核心对象，代表一张二维表。
*   **`cut`**: **(必考)** 用于“分箱”或“离散化”。例如：将年龄（连续值）划分为“青年”、“中年”、“老年”。
*   **`get_dummies`**: **(必考)** 独热编码（One-Hot Encoding）。将分类变量（如“性别”）转换为 0/1 矩阵，供机器学习模型使用。
*   **`to_datetime`**: 将字符串转为日期格式，便于计算日期差。
*   **`value_counts()`**: 统计某一列中每个值出现的次数（如：统计男女比例）。
*   **`groupby()`**: 分组操作。常配合 `mean()`, `sum()`, `count()` 使用。
*   **`apply()`**: 对每一行或每一列执行自定义函数。
*   **`fillna()` / `dropna()`**: 处理缺失值（填充或删除）。

### **Numpy (`import numpy as np`)**
*用途：高性能数值计算、矩阵处理。*

*   **`array`**: 创建数组（矩阵）。
*   **`where(condition, x, y)`**: **(常用)** 条件赋值。如果满足条件则设为 x，否则设为 y。
*   **`argmax`**: 返回数组中最大值的索引（常用于多分类结果解析）。
*   **`expand_dims`**: 在指定维度增加一个轴（如：将 (224, 224, 3) 的图片变为 (1, 224, 224, 3) 准备输入模型）。
*   **`inf`**: 代表无穷大，常用于定义分箱的边界。
*   **`transpose`**: 矩阵转置（如：调整图像通道顺序 [H, W, C] -> [C, H, W]）。

---

## 2. 机器学习建模 (Scikit-Learn & XGBoost)

### **预处理 (`sklearn.preprocessing`)**
*   **`StandardScaler`**: 标准化。将数据转换为均值为 0，方差为 1。
*   **`MinMaxScaler`**: 归一化。将数据压缩到 [0, 1] 区间（对神经网络或 SVM 很有用）。
*   **`LabelEncoder`**: 标签编码。将字符串标签转换为数字 (0, 1, 2...)。

### **模型准备与评估 (`sklearn.model_selection` & `metrics`)**
*   **`train_test_split`**: **(必考)** 将数据集划分为训练集和测试集（通常比例 8:2 或 7:3）。
*   **`r2_score`**: 评估回归模型的拟合优度（越接近 1 越好）。
*   **`mean_squared_error (MSE)`**: 均方误差。
*   **`mean_absolute_error (MAE)`**: 平均绝对误差。

### **模型算法**
*   **`LinearRegression`**: 线性回归。
*   **`DecisionTreeRegressor`**: 决策树回归。
*   **`RandomForestRegressor`**: 随机森林回归（通常比单棵决策树更稳健）。
*   **`XGBRegressor`**: **(热门)** XGBoost 算法，常用于竞赛或实际生产中。

---

## 3. 图像处理与计算机视觉 (OpenCV & PIL)

### **OpenCV (`import cv2`)**
*   **`imread` / `imwrite`**: 读取和保存图像。
*   **`cvtColor`**: 颜色空间转换。最常见的是 `cv2.COLOR_BGR2RGB`（OpenCV 默认 BGR，Matplotlib/模型通常需 RGB）。
*   **`resize`**: 缩放图像至模型指定大小（如 224x224）。
*   **`rectangle`**: 在图上画框（用于目标检测结果展示）。

### **PIL (Pillow)**
*   **`Image.open`**: 读取图片。简单处理时常用。

---

## 4. 可视化 (Matplotlib & Seaborn)

### **Matplotlib (`import matplotlib.pyplot as plt`)**
*   **`figure`**: 创建画布。
*   **`subplot`**: 在一个画布上画多个子图。
*   **`scatter`**: 散点图（常用于查看两个变量的关系）。
*   **`legend`**: 显示图例。
*   **`FontProperties`**: **(解决中文显示)** 用于加载中文字体文件，否则标题里的中文会变方框。

### **Seaborn (`import seaborn as sns`)**
*   **`boxplot`**: 箱线图。展示数据分布、中位数及异常值的利器。

---

## 5. 模型部署与工具 (ONNX & System)

### **ONNX Runtime**
*   **`InferenceSession`**: **(三级必考)** 用于加载 `.onnx` 模型并进行推理（Inference）。这是一种跨框架的模型运行方式。

### **系统与持久化**
*   **`os.makedirs`**: 递归创建目录。
*   **`joblib` / `pickle`**: **(必考)** 保存和加载训练好的模型文件（`.pkl` 或 `.joblib`）。
*   **`time`**: 用于计算代码执行耗时（如：统计单张图片推理时间）。

---

## 快速速查表 (Cheat Sheet)

| 任务 | 常用函数 |
| :--- | :--- |
| **数据清洗** | `data.dropna()`, `data.fillna()`, `data.drop_duplicates()` |
| **特征转换** | `pd.get_dummies(data)`, `pd.cut(data['age'], bins)` |
| **数据划分** | `train_test_split(X, y, test_size=0.2)` |
| **模型训练** | `model.fit(X_train, y_train)` |
| **模型预测** | `y_pred = model.predict(X_test)` |
| **图片预处理** | `cv2.resize(img, (224, 224))`, `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` |
| **保存模型** | `joblib.dump(model, 'model.pkl')` |
