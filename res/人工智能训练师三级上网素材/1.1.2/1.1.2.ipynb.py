import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 读取数据集 2分
data = _____________


# 1. 传感器数据统计
# 对传感器类型进行分组，并计算每个组的数据数量和平均值 3分
sensor_stats = _____________(_____________)['Value']._____________
# 输出结果
print("传感器数据数量和平均值:")
print(sensor_stats)


# 2. 按位置统计温度和湿度数据
# 筛选出温度和湿度数据，然后按位置和传感器类型分组，计算每个组的平均值 2分
location_stats = data[data['SensorType']._____________._____________['Value'].mean().unstack()
# 输出结果
print("每个位置的温度和湿度数据平均值:")
print(location_stats)


# 3. 数据清洗和异常值处理
# 标记异常值 3分
data['is_abnormal'] = _____________(
    ((_____________) & ((data['Value'] < -10) | (data['Value'] > 50))) |
    ((_____________) & ((data['Value'] < 0) | (data['Value'] > 100))),
    True, False
)
# 输出异常值数量 2分
print("异常值数量:", data['is_abnormal']._____________)
# 填补缺失值
# 使用前向填充和后向填充的方法填补缺失值 4分
data['Value']._____________(_____________, inplace=True)
data['Value']._____________(_____________, inplace=True)
# 保存清洗后的数据
# 删除用于标记异常值的列，并将清洗后的数据保存到新的CSV文件中 4分
cleaned_data = _____________(_____________=['is_abnormal'])
_____________('cleaned_sensor_data.csv', _____________)
print("数据清洗完成，已保存为 'cleaned_sensor_data.csv'")
