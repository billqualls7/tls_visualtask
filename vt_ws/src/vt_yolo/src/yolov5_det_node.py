#!/usr/bin/env python3
'''
Author: EPAICAR EPAICAR@EPAICAR
Date: 2024-02-13 20:09:47
LastEditors: EPAICAR EPAICAR@EPAICAR
LastEditTime: 2024-02-26 22:21:30
FilePath: /epaicar/tls_visualtask/vt_ws/src/vt_yolo/src/yolov5_det_node.py
Description: 
'''
from yolov5_det_trt import plot_one_box
from yolov5_det_trt import YoLov5TRT
import ctypes
import rospy
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
import cv2
from config import YAMLParser
from vt_msgs.msg import Yoloutput
import time
from videocapture import USBCamera


'''
description: result_boxes [x1, y1] 是矩形框的左上角坐标，而 [x2, y2] 是矩形框的右下角坐标
return {*}
'''
class YOLO_Det_Node:
    def __init__(self, parser):
        PLUGIN_LIBRARY = "../lib/libyoloplugins.so"
        ctypes.CDLL(PLUGIN_LIBRARY)


        self.yolo_pub = rospy.Publisher('yolo/output', Yoloutput, queue_size=10)
        self.yolo_pub_img = rospy.Publisher('yolo/CompressedImage', Yoloutput, queue_size=10)
        self.yolo_msgs = Yoloutput()
        self.usbcam = USBCamera(parser.cam_device)

        self.yolov5_wrapper = YoLov5TRT(parser.engine_file_path)
        self.yolov5_wrapper.CONF_THRESH = parser.CONF_THRESH
        self.yolov5_wrapper.IOU_THRESHOLD = parser.IOU_THRESHOLD

    def infer(self):
        frame = self.usbcam.usb_camera_read()
        result_boxes, result_scores, result_classid = self.yolov5_wrapper.infer(frame)
        for j in range(len(result_boxes)):
            classification = parser.categories[int(result_classid[j])]
            score = result_scores[j]
            box = result_boxes[j]
            plot_one_box(
                box,
                frame,
                label="{}:{:.2f}".format(
                classification, 
                score),
            )
            self.yolo_msgs.classification = classification
            self.yolo_msgs.score = score
            self.yolo_msgs.boxes.x1 = box[0]
            self.yolo_msgs.boxes.y1 = box[1]
            self.yolo_msgs.boxes.x2 = box[2]
            self.yolo_msgs.boxes.y2 = box[3]
            self.yolo_pub.publish(self.yolo_msgs)

        # cv2.imwrite("../images/demo.jpg", frame)

 





    
if __name__ == '__main__':
    try:
        rospy.init_node('YOLOV5_Det_Node', anonymous=True)
        rospy.loginfo("YOLOV5_Det_Node...")
        parser = YAMLParser('../config/yolov5_det.yaml')
        parser.get_data()
        PLUGIN_LIBRARY = "../lib/libyoloplugins.so"
        ctypes.CDLL(PLUGIN_LIBRARY)
        
        yolo = YOLO_Det_Node(parser)
        while not rospy.is_shutdown():
            # start = time.time()
            yolo.infer()
            # end = time.time()
            # use_time = end - start
            # print('all time->{:.2f}ms'.format(use_time * 1000))
        

    except rospy.ROSInterruptException:
        pass

