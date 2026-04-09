# Pandas 核心高频考点精讲（Python 数据分析必考）
我把这些**必考、常用**的 Pandas 方法，用**最易懂的方式+实战代码**讲透，直接背会、练会就能应对考试/工作！

---

## 一、先记住：Pandas 核心对象
```python
import pandas as pd
# DataFrame = 二维表格（行+列，像 Excel）
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [22, 35, 58],
    "性别": ["男", "女", "男"],
    "成绩": [85, None, 92]
})
```

---

## 二、逐个精讲必考方法
### 1. `pd.cut()` —— 连续值分箱（**必考**）
**作用**：把数字（如年龄、分数）划分成区间/类别
```python
# 定义区间：0-30青年，30-50中年，50-100老年
bins = [0, 30, 50, 100]
labels = ["青年", "中年", "老年"]

# 新增一列：年龄分组
df["年龄分组"] = pd.cut(df["年龄"], bins=bins, labels=labels)
```
✅ 输出：张三=青年，李四=中年，王五=老年

---

### 2. `pd.get_dummies()` —— 独热编码（**必考**）
**作用**：把文字分类（性别、城市）转成 0/1 数字，给机器学习用
```python
# 对【性别】列做独热编码
df_dummy = pd.get_dummies(df, columns=["性别"])
```
✅ 效果：性别列 → 性别_男、性别_女 两列，是=1，不是=0

---

### 3. 读取文件：`read_csv` / `read_excel`
```python
# 读取 CSV
df = pd.read_csv("数据.csv")

# 读取 Excel（需要安装 openpyxl）
df = pd.read_excel("数据.xlsx")
```

---

### 4. `pd.to_datetime()` —— 转日期格式
```python
# 把字符串日期 转成 可计算的日期格式
df["日期"] = pd.to_datetime(df["日期"])
# 可以直接算天数差、年月筛选
```

---

### 5. `value_counts()` —— 统计频次（超级常用）
```python
# 统计男女各多少人
df["性别"].value_counts()

# 统计年龄分组的人数
df["年龄分组"].value_counts()
```

---

### 6. `groupby()` —— 分组统计（面试/考试高频）
```python
# 按性别分组，算平均年龄
df.groupby("性别")["年龄"].mean()

# 按性别分组，算总分
df.groupby("性别")["成绩"].sum()
```

---

### 7. `apply()` —— 自定义函数处理数据
```python
# 定义函数：成绩≥60及格，否则不及格
def check_pass(score):
    return "及格" if score >= 60 else "不及格"

# 对成绩列应用函数
df["是否及格"] = df["成绩"].apply(check_pass)
```

---

### 8. 缺失值处理：`fillna()` / `dropna()`
```python
# 1. 填充缺失值（用 0 填充）
df["成绩"] = df["成绩"].fillna(0)

# 2. 删除有缺失值的行
df = df.dropna()
```

---

# 三、极简速记口诀（直接背）
1. **连续值分段** → `cut`
2. **文字转0/1** → `get_dummies`
3. **统计人数** → `value_counts`
4. **分组计算** → `groupby`
5. **自定义处理** → `apply`
6. **缺值处理** → `fillna/dropna`

---

### 总结
1. 这 9 个方法是 Pandas **100% 必考/必用**核心
2. 代码直接复制运行，改改数据就能用
3. 不懂的地方，我可以**逐行讲解、出练习题、帮你改错**

你需要我：
✅ 出一套 Pandas 测试题？
✅ 还是把这些代码整合为一个完整可运行的 demo？