'''
Author: Wuyao 1955416359@qq.com
Date: 2023-04-28 09:08:49
LastEditors: Wuyao 1955416359@qq.com
LastEditTime: 2024-01-19 18:56:28
FilePath: \wyUnet\mysrc\make_dataset.py
Description: 制作数据集
'''
import os
import random
import shutil
from tqdm import tqdm
import time
# 设置原始数据集所在的目录和新的训练/验证/测试集目录
globalpath = "F:/Code/UnetV3/dataset/"


orig = globalpath+"orignialDataset/"
train = globalpath+"trainDataset/"
val = globalpath+"valDataset/"
test = globalpath+"testDataset/"
datapath = [train, val, test]

img = 'JPEGImages/'
label = 'SegmentationClass/'

folder_paths = []
jpeg_images_paths = []
segmentation_class_paths = []

for data_dir in datapath:
    folder_path = os.path.join(globalpath, data_dir)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"创建文件夹：{folder_path}")     
    jpeg_images_folder = os.path.join(folder_path, img)

    if not os.path.exists(jpeg_images_folder):
        os.makedirs(jpeg_images_folder)
        print(f"创建文件夹：{jpeg_images_folder}")
    jpeg_images_paths.append(jpeg_images_folder)    

    segmentation_class_folder = os.path.join(folder_path, label)
    if not os.path.exists(segmentation_class_folder):
        os.makedirs(segmentation_class_folder)
        print(f"创建文件夹：{segmentation_class_folder}")
    segmentation_class_paths.append(segmentation_class_folder)


# 将数据集文件名列表进行随机排序
filenames = os.listdir(orig+img)
random.shuffle(filenames)
# 将数据集按照7:2:1的比例分成训练集、验证集和测试集
train_size = int(0.7 * len(filenames))
val_size = int(0.2 * len(filenames))
test_size = len(filenames) - train_size - val_size

train_filenames = filenames[:train_size]
val_filenames = filenames[train_size:train_size+val_size]
test_filenames = filenames[train_size+val_size:]

# 创建进度条对象
pbar = tqdm(total=len(filenames))

# 将文件拷贝到新的目录中
for filename in train_filenames:
    src = os.path.join(orig+img, filename)
    src_lable = os.path.join(orig+label, filename)
    dst_img = os.path.join(jpeg_images_paths[0], filename)
    dst_lable = os.path.join(segmentation_class_paths[0], filename)
    shutil.copyfile(src, dst_img)
    shutil.copyfile(src_lable, dst_lable)
    pbar.update(1)

for filename in val_filenames:
    src = os.path.join(orig+img, filename)
    src_lable = os.path.join(orig+label, filename)
    dst_img = os.path.join(jpeg_images_paths[1], filename)
    dst_lable = os.path.join(segmentation_class_paths[1], filename)
    shutil.copyfile(src, dst_img)
    shutil.copyfile(src_lable, dst_lable)
    pbar.update(1)

for filename in test_filenames:
    src = os.path.join(orig+img, filename)
    src_lable = os.path.join(orig+label, filename)
    dst_img = os.path.join(jpeg_images_paths[2], filename)
    dst_lable = os.path.join(segmentation_class_paths[2], filename)
    shutil.copyfile(src, dst_img)
    shutil.copyfile(src_lable, dst_lable)
    pbar.update(1)


# 关闭进度条
pbar.close()