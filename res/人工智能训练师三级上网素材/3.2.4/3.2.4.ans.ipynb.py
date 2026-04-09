import onnxruntime as ort
import numpy as np
import scipy.special
from PIL import Image


# 预处理图像
def preprocess_image(image, resize_size=256, crop_size=224, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]):
    image = image.resize((resize_size, resize_size), Image.BILINEAR)
    w, h = image.size
    left = (w - crop_size) / 2
    top = (h - crop_size) / 2
    image = image.crop((left, top, left + crop_size, top + crop_size))
    image = np.array(image).astype(np.float32)
    image = image / 255.0
    image = (image - mean) / std
    image = np.transpose(image, (2, 0, 1))
    image = image.reshape((1,) + image.shape)
    return image


# 加载模型  2分
session = ort.InferenceSession ('flower-detection.onnx')


# 加载类别标签 2分
with open('labels.txt') as f:
    labels = [line.strip() for line in f.readlines()]


# 获取模型输入和输出的名称
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name


# 加载图片  2分
image = Image.open('flower_test.png').convert('RGB')


# 预处理图片  2分
processed_image = preprocess_image(image)


# 确保输入数据是 float32 类型
processed_image = processed_image.astype(np.float32)


# 进行图片识别  2分
output = session.run([output_name], {input_name: processed_image})[0]


# 应用 softmax 函数获取识别分类后的准确率  2分
accuracy = scipy.special.softmax(output, axis=-1)


# 获取预测的类别索引
predicted_idx =  np.argmax(accuracy[0])


# 获取预测的准确值（转换为百分比）
prob_percentage =  accuracy[0,predicted_idx]*100
 

# 获取预测的类别标签
predicted_label = labels[predicted_idx]


# 输出预测结果，包含百分比形式的概率
print(f"Predicted class: {predicted_label}, Accuracy: {prob_percentage:.2f}%")
