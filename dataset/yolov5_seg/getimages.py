import os
import shutil

source_folder = '/home/epaicar/tls_visualtask/dataset/yolov5_seg/labelme'
destination_folder = '/home/epaicar/tls_visualtask/dataset/yolov5_seg/images'



if(not os.path.exists(destination_folder)):
    os.mkdir(destination_folder)
# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith('.jpg'):
        # 构建源文件路径和目标文件路径
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        # 复制文件
        shutil.copy(source_file, destination_file)
