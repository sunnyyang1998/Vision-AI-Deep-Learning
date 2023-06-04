import cv2
import tensorflow as tf
import pyautogui

# 加载模型
model = tf.saved_model.load('faster_rcnn_resnet101_v1_800x1333_coco17_gpu-8/saved_model')

# 设置视频捕捉
cap = cv2.VideoCapture(0)  # 0表示摄像头设备号，如果有多个摄像头可以尝试不同的编号

# 定义准星颜色
crosshair_color = (0, 255, 0)  # Green color

while True:
    # 读取视频帧
    ret, frame = cap.read()

    if not ret:
        break

    # 将帧大小调整为模型所需的大小
    resized_frame = cv2.resize(frame, (800, 1333))

    # 预处理图像
    input_image = tf.expand_dims(resized_frame, axis=0)
    input_image = input_image / 255.0

    # 目标检测
    detections = model(input_image)

    # 处理检测结果
    for detection in detections:
        # 提取目标框的坐标和类别信息
        bbox = detection['bbox']
        class_id = detection['class_id']

        # 绘制矩形框和类别标签
        x, y, w, h = bbox
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, class_id, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # 绘制轮廓标注
        mask = detection['mask']
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contours, -1, (0, 0, 255), 2)

        # 显示类别标签
        label = f"Class: {class_id}"
        cv2.putText(frame, label, (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # 绘制准星
    screen_width, screen_height = pyautogui.size()
    crosshair_x = int(screen_width / 2)
    crosshair_y = int(screen_height / 2)
    crosshair_radius = 20
    cv2.circle(frame, (crosshair_x, crosshair_y), crosshair_radius, crosshair_color, 2)

    # 显示帧
    cv2.imshow('Game Frame', frame)

    # 按下'q'键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
