import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 加载模型
model = tf.saved_model.load('faster_rcnn_resnet101_v1_800x1333_coco17_gpu-8/saved_model')

# 创建图片生成器
validation_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

validation_data_dir = './validationData'
validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(800, 1333),
    batch_size=20,
    class_mode='categorical'
)

# 评估模型
test_loss, test_acc = model.evaluate(validation_generator, steps=50)
print('Test Accuracy:', test_acc)

# 绘制混淆矩阵
Y_pred = model.predict(validation_generator)
y_pred = np.argmax(Y_pred, axis=1)

cm = confusion_matrix(validation_generator.classes, y_pred)

plt.figure(figsize=(10,10))
sns.heatmap(cm, annot=True, fmt=".0f", linewidths=.5, square=True, cmap='Blues_r')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.title('Confusion Matrix', size=15)

report = classification_report(validation_generator.classes, y_pred, target_names=['Class 0', 'Class 1'])
print(report)
