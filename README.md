# 视觉任务部署方案
```bash
## 打开终端输入命令
cd ~/.tls && ./check_vtenv.sh
## 若环境通过测试则会打印pytorch cuda TensorRT测试信息及当前系统版本
PyTorch CUDA in Python3 version:1.10.0+cu10.2
TensorRT version: 8.2.1.8
epaicar_for_jetpack4.6.1_20240102
```

查看系统版本，在终端输入 sysver

```bash
epaicar@EPAIcar:~$ sysver
epaicar_for_jetpack4.6.1_20240102
```

当前部署方案所需环境基于版本号为20240102

VSCode远程开发请使用1.85及以前的版本，新版本不支持远程连接该系统

- [ ] USB3.0 摄像头畸变矫正

  

## 目录结构

```bash
├── dataset
│   └── yolov5_seg				## SEG数据集示例
├── pic                         ## 存放方案流程相关图片
├── README.md					## 第一次必看
├── Unet						## Unet-3.4
│   ├── cofig
│   ├── dataset
│   ├── demo
│   ├── params
│   ├── pre_model
│   ├── README.md				## Unet-3.4第一次必看
│   ├── run
│   ├── src
│   ├── torch2trt
│   └── unets
├── vt_ws						## ROS 工作空间
│   ├── build
│   ├── devel
│   └── src
├── yolov5_6.0					## yolov5_6.0 
│   ├── tensorrtx
│   └── yolov5-6.0
└── yolov5_seg					## yolov5_7.0 
    ├── deploy			        ## yolov5_7.0 部署脚本（jetson平台）
    └── yolov5_train			## yolov5_7.0 训练脚本
```

## YOLOv5-7.0
请将tls_visualtask/yolov5_seg/yolov5_train代码整体拷贝到具有**英伟达显卡**的设备上为模型训练做准备

EPAICAR同样可以训练模型，且相关环境依赖已经准备完毕。该机器人作为低功耗嵌入式设备不建议用于模型训练

**请使用labelme进行YOLOv5-7.0-seg数据集标注**

**每次转换模型请修改tls_visualtask/yolov5_seg/deploy/src/config.h**

训练目录文件夹如下所示，详见[Release v7.0 - YOLOv5 SOTA Realtime Instance Segmentation · ultralytics/yolov5 (github.com)](https://github.com/ultralytics/yolov5/releases/tag/v7.0)

```bash
├── benchmarks.py
├── classify
├── CONTRIBUTING.md
├── data
├── detect.py
├── export.py
├── gen_wts.py
├── getimages.py				## 从labelme导出的数据集提取出图片
├── hubconf.py
├── json2txt.py					## 从labelme导出的数据集转为YOLOV5-7.0-SEG专用数据集格式
├── LICENSE
├── models
├── mydata						## 自己的训练参数
├── README.md
├── requirements.txt
├── segment
├── setup.cfg
├── train.py
├── tutorial.ipynb
├── utils
├── val.py
├── yolov5n.pt					## 官方预训练det模型
├── yolov5n7-seg.pt             ## 官方预训练seg模型
├── yolov5n7-seg.wts
├── yolov5n7.wts
├── yolov5n-seg.pt
└── yolov5-seg.wts


```

根据自己选择的训练设备的硬件条件选择合适的CUDA和PyTorch版本 [PyTorch](https://pytorch.org/)

安装环境依赖，打开终端进入yolov5_train目录 pip install -r requirements.txt

```bash
(myconda) root@qMox2r:/mnt/yolov5_train# pip install -r requirements.txt 
```

**本文涉及所有训练过程均在服务器上完成**




## YOLO部署方案流程（yolov5-7.0）

### Seg

#### 模型训练（seg）

测试环境python segment/predict.py --weight yolov5n-seg.pt --data data/images/bus.jpg 

```bash
(myconda) root@qMox2r:/mnt/yolov5_train# python segment/predict.py --weight yolov5n-seg.pt --data data/images/bus.jpg 
segment/predict: weights=['yolov5n-seg.pt'], source=data/images, data=data/images/bus.jpg, imgsz=[640, 640], conf_thres=0.25, iou_thres=0.45, max_det=1000, device=, view_img=False, save_txt=False, save_conf=False, save_crop=False, nosave=False, classes=None, agnostic_nms=False, augment=False, visualize=False, update=False, project=runs/predict-seg, name=exp, exist_ok=False, line_thickness=3, hide_labels=False, hide_conf=False, half=False, dnn=False, vid_stride=1, retina_masks=False
YOLOv5 🚀 v7.0-0-g915bbf29 Python-3.8.12 torch-1.11.0+cu113 CUDA:0 (NVIDIA GeForce RTX 2080 Ti, 11020MiB)

Fusing layers... 
YOLOv5n-seg summary: 224 layers, 1986637 parameters, 0 gradients, 7.1 GFLOPs
image 1/2 /mnt/yolov5_train/data/images/bus.jpg: 640x480 4 persons, 1 bus, 1 skateboard, 18.2ms
image 2/2 /mnt/yolov5_train/data/images/zidane.jpg: 384x640 2 persons, 1 tie, 18.9ms
Speed: 0.4ms pre-process, 18.6ms inference, 1.5ms NMS per image at shape (1, 3, 640, 640)
Results saved to runs/predict-seg/exp2
```

打开文件夹runs/predict-seg/exp2，效果如

![image-20240212092351681](/tls_visualtask/pic/image-20240212092351681.png)

##### 0.数据集准备

##### 1.训练

```bash
python segment/train.py --epochs 300 --data mydata/carline-seg.yaml --weight yolov5n7-seg.pt --img 640 --cfg mydata/yolov5n-seg.yaml --hyp mydata/hyp.scratch-low.yaml
```




#### 模型转换（seg）

将训练结束之后得到的模型拷贝到/home/epaicar/tls_visualtask/yolov5_seg/yolov5_train

yolov5n7-seg.pt 自己训练的模型 .pt后缀

yolov5n7-seg.wts 转换的模型.wts后缀

转换环境与部署环境有所不同，为避免环境冲突，转换环境移植到了unet环境当中并兼容Unet环境

```bash
cd tls_visualtask/yolov5_seg/yolov5_train/
unet gen_wts.py -w yolov5n7-seg.pt -o yolov5n7-seg.wts
```

```bash
## 转换正确会输出以下信息
Generating .wts for detect model
Loading yolov5n7-seg.pt
YOLOv5 🚀 v7.0-0-g915bbf29 Python-3.6.15 torch-1.10.0 CPU

Writing into yolov5n7-seg.wts
```

修改tls_visualtask/yolov5_seg/deploy/src/config.h

根据自身数据集情况去做调整

```cpp
#define USE_FP16  // set USE_INT8 or USE_FP16 or USE_FP32 jetson nano不支持INT8
// Detection model and Segmentation model' number of classes
constexpr static int kNumClass = 80;

```



```bash
cd ~/tls_visualtask/yolov5_seg/deploy/
ls
```

检测是否有build文件夹

如果没有，则创建build文件夹，将上一步生成的wts文件拷贝进build文件夹中，进行编译并生成engine文件

```bash
 mkdir build
 cd build/
 cp ~/tls_visualtask/yolov5_seg/yolov5_train/yolov5n7-seg.wts .
 cmake ..
 make -j4
 ./yolov5_seg -s yolov5n7-seg.wts yolov5n7-seg.engine n
```

模型转换成功终端如下所示，其中yolov5n7-seg.engine转换后的模型.engine后缀

转换过程需要几分钟，请耐心等待

```bash
epaicar@EPAIcar:~/tls_visualtask/yolov5_seg/deploy/build$ ./yolov5_seg -s yolov5n7-seg.wts yolov5n7-seg.engine n

Loading weights: yolov5n7-seg.wts
Building engine, please wait for a while...
Build engine successfully!
```



每次修改deploy中**非python程序**之后，最好重新编译并删除之前的engine文件，重新生成

```bash
 cd ~/tls_visualtask/yolov5_seg/deploy/build/
 make -j4
 rm yolov5n7-seg.engine
 ./yolov5_seg -s yolov5n7-seg.wts yolov5n7-seg.engine n
```

【注意】：这里需要注意的是seg模型和det模型使用的是同一个参数文件进行模型导出，当两个模型的数据集种类不一样时，在每次导出之前都需要修改参数文件并且重新编译整个工程，然后再执行模型转换脚本



### Det

#### 模型训练（Det）

训练自己的数据集

进入**mydata**文件夹，有三个参数文件

```bash
hyp.scratch-low.yaml  mydataset.yaml  yolov5n.yaml
```

hyp.scratch-low.yaml 在第一次训练的时候不用更改，以第一次训练的模型为参考若不满意则自行进行微调

mydataset.yaml

```yaml
path: /dataset/YOLO/dashbord 数据集所在根目录 该目录下需要有训练集、验证集、测试集
train: train/ # 
val: validation/ #
test: test/

# Classes 数据集类别
names:
 0: pointer
 1: digital
```
![dataset](/tls_visualtask/pic/dataset.png)

yolov5n.yaml 将nc更改成自己数据集类别数量

```yaml
# YOLOv5 🚀 by Ultralytics, GPL-3.0 license

# Parameters
nc: 2  # number of classes
```

进入yolov5_train文件夹目录执行训练指令，训练结束之后根据终端提示找到训练完成的模型best.pt

```bash
python train.py --weights yolov5n7.pt --cfg mydata/yolov5n.yaml --data mydata/dashbord.yaml --hyp mydata/hyp.scratch-low.yaml
```

模型一般保存在yolov5_train/runs/train/exp/weights



#### 模型转换（Det）

将训练结束之后得到的模型拷贝到/home/epaicar/tls_visualtask/yolov5_seg/yolov5_train

yolov5n7.pt 自己训练的模型 .pt后缀

yolov5n7.wts 转换的模型.wts后缀

转换环境与部署环境有所不同，为避免环境冲突，转换环境移植到了unet环境当中并兼容Unet环境

```bash
cd ~/tls_visualtask/yolov5_seg/yolov5_train/
unet gen_wts.py -w yolov5n7.pt -o yolov5n7.wts
```

```bash
## 转换正确会输出以下信息
Generating .wts for detect model
Loading yolov5n7.pt
YOLOv5 🚀 v7.0-0-g915bbf29 Python-3.6.15 torch-1.10.0 CPU

Writing into yolov5n7.wts
```

修改tls_visualtask/yolov5_seg/deploy/src/config.h

根据自身数据集情况去做调整

```c++
#define USE_FP16  // set USE_INT8 or USE_FP16 or USE_FP32 jetson nano不支持INT8
// Detection model and Segmentation model' number of classes
constexpr static int kNumClass = 80;

```



检测是否有build文件夹

```bash
cd ~/tls_visualtask/yolov5_seg/deploy/
ls
```

如果没有，则创建build文件夹，将上一步生成的wts文件拷贝进build文件夹中，进行编译并生成engine文件

```bash
 mkdir build
 cd build/
 cp ~/tls_visualtask/yolov5_seg/yolov5_train/yolov5n7.wts .
 cmake ..
 make -j4
 ./yolov5_det -s yolov5n7.wts yolov5n7.engine n
```

模型转换成功终端如下所示，其中yolov5n7.engine转换后的模型.engine后缀

转换过程需要几分钟，请耐心等待

```bash
epaicar@EPAIcar:~/tls_visualtask/yolov5_seg/deploy/build$ ./yolov5_det -s yolov5n7.wts yolov5n7.engine n

Loading weights: yolov5n7.wts
Building engine, please wait for a while...
Build engine successfully!
```

每次修改deploy中**非python程序**之后，最好重新编译并删除之前的engine文件，重新生成

```bash
 cd ~/tls_visualtask/yolov5_seg/deploy/build/
 make -j4
 rm yolov5n7.engine
 ./yolov5_det -s yolov5n7.wts yolov5n7.engine n
```

【注意】：这里需要注意的是seg模型和det模型使用的是同一个参数文件进行模型导出，当两个模型的数据集种类不一样时，在每次导出之前都需要修改参数文件并且重新编译整个工程，然后再执行模型转换脚本



#### ROS

将生成的engine文件拷贝到tls_visualtask/vt_ws/src/vt_yolo/model

```bash
cp yolov5n7.engine ~/tls_visualtask/vt_ws/src/vt_yolo/model/
```

修改推理配置文件tls_visualtask/vt_ws/src/vt_yolo/config/yolov5_det.yaml

```yaml
cam_device: 0  										#摄像头设备号

engine_file_path: "../model/dashboard.engine"    	#序列文件路径

CONF_THRESH: 0.5									#置信度
IOU_THRESHOLD: 0.4									#IOU阈值

categories: ["pointer", "digital"]      			#与mydata/mydataset.yaml中顺序保持一致
```

 打开终端

```bash
roscore
```

另外打开一个终端

```bash
roscd vt_yolo/src/
python3 yolov5_det_node.py
```

相关话题 /yolo/output



指令合集

```bash
## 激活unet环境
setconda unet
```



# 常见问题（Q&A）

```bash
[TRT] [E] 3: [builderConfig.cpp::canRunOnDLA::382] Error Code 3: API Usage Error (Parameter check failed at: optimizer/api/builderConfig.cpp::canRunOnDLA::382, condition: dlaEngineCount > 0
```

Jetson Nano 模型转换报错，这个报错的意思是Nano硬件上没有搭载DLA加速器，可忽略该错误

```bash
[W] Using an engine plan file across different models of devices is not recommended and is likely to affect performance or even cause errors.
```

只要确保engine文件的生成和当前执行推理任务的机器人是同一个机器人即可忽略该警告
