# 导入必要的库
import numpy as np
from PIL import Image
import onnxruntime as ort


# 定义预处理函数，用于将图片转换为模型所需的输入格式
def preprocess(image_path):
    input_shape = (1, 1, 64, 64)    # 模型输入期望的形状，这里是 (N, C, H, W)，N=batch size, C=channels, H=height, W=width
    img = Image.open(image_path).convert('L')    # 打开图像文件并将其转换为灰度图  1分
    img = img.resize((64, 64), Image.ANTIALIAS)    # 调整图像大小到模型输入所需的尺寸
    img_data = np.array(img, dtype=np.float32)    # 将PIL图像对象转换为numpy数组，并确保数据类型是float32
    # 调整数组的形状以匹配模型输入的形状
    img_data = np.expand_dims(img_data, axis=0)  # 添加 batch 维度
    img_data = np.expand_dims(img_data, axis=1)  # 添加 channel 维度
    assert img_data.shape == input_shape, f"Expected shape {input_shape}, but got {img_data.shape}"    # 确保最终的形状与模型输入要求的形状一致
    return img_data    # 返回预处理后的图像数据


# 定义情感类别与数字标签的映射表 3分
emotion_table = {____________}


# 加载模型 3分
ort_session = ____________    # 使用onnxruntime创建一个会话，用于加载并运行模型


# 加载本地图片并进行预处理 3分
input_data = ____________


# 准备输入数据，确保其符合模型输入的要求
ort_inputs = {ort_session.get_inputs()[0].name: input_data}    # ort_session.get_inputs()[0].name 是获取模型的第一个输入的名字


# 运行模型，进行预测 3分
ort_outs = ____________(None, ____________)


# 解码模型输出，找到预测概率最高的情感类别 3分
predicted_label = ____________(ort_outs[0])


# 根据预测的标签找到对应的情感名称 3分
predicted_emotion = ____________[predicted_label]


# 输出预测的情感
print(f"Predicted emotion: {predicted_emotion}")


