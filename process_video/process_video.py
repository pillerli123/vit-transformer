import cv2
import numpy as np
from mrcnn import model as modellib
from mrcnn import visualize
from mrcnn.config import Config

# 自定义配置类，用于设置模型的配置参数
class CustomConfig(Config):
    NAME = "custom"
    IMAGES_PER_GPU = 1
    GPU_COUNT = 1
    NUM_CLASSES = 1 + 1  # 要分割的对象类别数（包括背景）

# 创建 Mask R-CNN 模型
model = modellib.MaskRCNN(mode="inference", config=CustomConfig(), model_dir="./")

# 加载预训练权重
model.load_weights('path_to_model_weights.h5')  # 替换为实际的模型权重路径

# 打开视频文件
video_path = 'path_to_video_file.mp4'  # 替换为实际的视频文件路径
cap = cv2.VideoCapture(video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("无法打开视频文件")
    exit()

# 获取视频的基本信息
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 创建视频编写器以保存分割后的视频
output_path = 'D:\\python\\Final paper\\snake_game_gui\\10\\output (2).avi'  # 替换为实际的输出视频文件路径
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 可根据需要更改编码器
output = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# 逐帧读取视频并进行分割
while True:
    # 逐帧读取视频
    ret, frame = cap.read()

    # 如果无法读取帧，退出循环
    if not ret:
        break

    # 运行模型进行实例分割
    results = model.detect([frame], verbose=0)

    # 获取分割结果
    r = results[0]
    masks = r['masks']
    class_ids = r['class_ids']

    # 在原始帧上可视化分割结果
    visualize.display_instances(frame, r['rois'], masks, class_ids, ['背景', '目标类别'], ax=None)

    # 将分割结果应用于原始帧
    segmented_frame = visualize.apply_mask(frame, masks, color=(0, 255, 0), alpha=0.5)

    # 将分割后的帧写入输出视频
    output.write(segmented_frame)

    # 显示分割后的帧（可选）
    cv2.imshow('Segmented Frame', segmented_frame)

    # 按下'q'键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放视频文件和视频编写器
cap.release()
output.release()
cv2.destroyAllWindows()
