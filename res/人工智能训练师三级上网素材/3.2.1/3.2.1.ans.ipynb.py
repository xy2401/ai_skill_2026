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


# 模型加载 2分
session = ort.InferenceSession('resnet.onnx')


# 加载类别标签
labels_path = 'labels.txt'
with open(labels_path) as f:
  labels = [line.strip() for line in f.readlines()]


# 获取模型输入和输出的名称
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name


# 加载图片 2分
image =Image.open('img_test.jpg').convert('RGB')


# 预处理图片 2分
processed_image = preprocess_image(image)


# 确保输入数据是 float32 类型
processed_image = processed_image.astype(np.float32)


# 进行图片识别 2分
output = session.run([output_name], {input_name: processed_image})[0]


# 应用 softmax 函数获取概率 2分
probabilities = scipy.special.softmax(output, axis=-1)


# 获取最高的5个概率和对应的类别索引 3分
top5_idx = np.argsort( (probabilities[0])[-5:][::-1])
top5_prob = probabilities[0][top5_idx]


# 打印结果
print("Top 5 predicted classes:")
for i in range(5):
  print(f"{i+1}: {labels[top5_idx[i]]} - Probability: {top5_prob[i]}")
