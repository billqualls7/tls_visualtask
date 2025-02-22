'''
Author: EPAICAR EPAICAR@EPAICAR
Date: 2024-02-28 16:46:41
LastEditors: EPAICAR EPAICAR@EPAICAR
LastEditTime: 2024-03-01 22:33:59
FilePath: /epaicar/tls_visualtask/vt_ws/src/vt_yolo/src/yolov5_seg_node.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#!/usr/bin/env python3

from yolov5_seg_trt import plot_one_box
from yolov5_seg_trt import YoLov5TRT
import ctypes
import rospy
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
import cv2
from config import YAMLParser
from vt_msgs.msg import Yoloutput
from vt_msgs.msg import CarLinebias

import time
from videocapture import USBCamera
import numpy as np

from getbias import GetAngle
'''
description: result_boxes [x1, y1] 是矩形框的左上角坐标，而 [x2, y2] 是矩形框的右下角坐标
img_size height:240 weight:320
return {*}
'''
class YOLO_Seg_Node:
    def __init__(self, parser):
        PLUGIN_LIBRARY = "../lib/libyoloplugins.so"
        ctypes.CDLL(PLUGIN_LIBRARY)


        self.yolo_pub = rospy.Publisher('yolo/carlinebias', CarLinebias, queue_size=10)
        self.yolo_msgs = CarLinebias()
        self.usbcam = USBCamera(parser.cam_device, half_img=True)

        # self.usbcam.cap.update_resolution(self.set_w, self.set_h)

        self.colorful = parser.colorful

        self.img_heigh = self.usbcam.usb_camera_read().shape[0]
        self.img_width = self.usbcam.usb_camera_read().shape[1]

        self.yolov5_wrapper = YoLov5TRT(parser.engine_file_path)
        self.yolov5_wrapper.CONF_THRESH = parser.CONF_THRESH
        self.yolov5_wrapper.IOU_THRESHOLD = parser.IOU_THRESHOLD

        self.gt = GetAngle()



    def infer(self):
        frame = self.usbcam.usb_camera_read()

        # print(frame.shape)
        # frame = cv2.imread('../images/21.jpg')
        # frame = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_AREA)
        # self.img_heigh = resized_image.shape[0]
        # self.img_width = resized_image.shape[1]
        result_masks = []
        start = time.time()

        result_masks = self.yolov5_wrapper.infer(frame)

        
        end = time.time()
        use_time = end - start
        print('infer time->{:.2f}ms'.format(use_time * 1000))
        
        if result_masks.any():
        
            start = time.time()
            mask = self.draw_mask_one(result_masks)

            self.yolo_msgs.bais = self.gt.get_angle(mask)
            
            end = time.time()
            use_time = end - start
            print('masks time->{:.2f}ms'.format(use_time * 1000))
            self.yolo_pub.publish(self.yolo_msgs)

            cv2.imwrite("../images/mask.jpg", mask)
        cv2.imwrite("../images/cam.jpg", frame)

    
    def draw_mask_one(self,masks):
        '''
        description: Draw mask without color
        return : mask
        ''' 
        if len(masks) == 0:
            return 

        # result_image = np.max(masks, axis=0).astype(np.uint8)* 255
        return np.max(masks, axis=0).astype(np.uint8)* 255
    
    def draw_mask_rgb(self, masks, colors_, im_src, alpha=0.5):    
        """
        description: Draw mask on image color 暂时没移植过来
        param: 
            masks  : result_mask
            colors_: color to draw mask
            im_src : original image
            alpha  : scale between original  image and mask
        return:
            no return
        """
        if len(masks) == 0:
            return
        masks = np.asarray(masks, dtype=np.uint8)
        masks = np.ascontiguousarray(masks.transpose(1, 2, 0))
        masks = np.asarray(masks, dtype=np.float32)
        colors_ = np.asarray(colors_, dtype=np.float32)
        s = masks.sum(2, keepdims=True).clip(0, 1)
        masks = (masks @ colors_).clip(0, 255)
        im_src[:] = masks * alpha + im_src * (1 - s * alpha)

    def draw_mask(self, masks, colors_, im_src):
        if self.colorful:
            self.draw_mask_one(masks)
        else: self.draw_mask_rgb(masks, colors_, im_src)





    
if __name__ == '__main__':
    try:
        rospy.init_node('YOLOV5_Seg_Node', anonymous=True)
        rospy.loginfo("YOLOV5_Seg_Node...")
        parser = YAMLParser('../config/yolov5_seg.yaml')
        parser.get_data()
        PLUGIN_LIBRARY = "../lib/libyoloplugins.so"
        ctypes.CDLL(PLUGIN_LIBRARY)
        
        yolo = YOLO_Seg_Node(parser)
        while not rospy.is_shutdown():
            start = time.time()
            yolo.infer()
            end = time.time()
            use_time = end - start
            print('all time->{:.2f}ms'.format(use_time * 1000))
        
        yolo.usbcam.usb_camera_close()
    except rospy.ROSInterruptException:
        pass

