import onnxruntime
import numpy as np
from PIL import Image


# 加载ONNX模型  2分
ort_session = onnxruntime.InferenceSession('mnist.onnx')


# 加载图像 2分
image = Image.open('img_test.png').convert('L')  # 转为灰度图


#图像预处理 
image = image.resize((28, 28))  # 调整大小为MNIST模型的输入尺寸2分
image_array = np.array(image, dtype=np.float32)  # 转为numpy数组2分
image_array = np.expand_dims(image_array, axis=0)  # 添加batch维度2分
image_array = np.expand_dims(image_array, axis=0)  # 添加通道维度2分


#返回模型输入列表 2分
ort_inputs = {ort_session.get_inputs()[0].name: image_array}
# 执行预测 2分
ort_outs = ort_session.run(None, ort_inputs)


# 获取预测结果 2分
predicted_class = np.argmax(ort_outs[0])


# 输出预测结果
print(f"Predicted class: {predicted_class}")
