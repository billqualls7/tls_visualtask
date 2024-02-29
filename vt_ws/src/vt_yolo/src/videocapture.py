'''
Author: EPAICAR EPAICAR@EPAICAR
Date: 2024-02-22 22:16:47
LastEditors: EPAICAR EPAICAR@EPAICAR
LastEditTime: 2024-02-28 16:51:53
FilePath: /epaicar/tls_visualtask/vt_ws/src/vt_yolo/src/videocapture.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
import queue
import threading
import time
import rospy 
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
# 自定义无缓存读视频类
class VideoCapture:
    """Customized VideoCapture, always read latest frame """
    
    def __init__(self, camera_id):
        # "camera_id" is a int type id or string name
        self.cap = cv2.VideoCapture(camera_id)
        self.q = queue.Queue(maxsize=3)
        self.stop_threads = False    # to gracefully close sub-thread
        th = threading.Thread(target=self._reader)
        th.daemon = True             # 设置工作线程为后台运行
        th.start()

    # 实时读帧，只保存最后一帧
    def _reader(self):
        while not self.stop_threads:
            ret, frame = self.cap.read()
            if not ret:
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait() 
                except queue.Empty:
                    pass
            self.q.put(frame)

    def read(self):
        return self.q.get()
    
    def terminate(self):
        self.stop_threads = True
        self.cap.release()
'''
description: use web-video-server 
tls_visualtask/vt_ws/src/vt_yolo/launch/web_video.launch 
set IP address
http://192.168.1.11:8080/stream?topic=/usb_camera/image_raw&type=ros_compressed
return {*}
'''
class USBCamera:
    def __init__(self,video_device):
        self.video_device = video_device
        self.image_pub_compressed = rospy.Publisher('usb_camera/image_raw/compressed', CompressedImage, queue_size=10) # 发布压缩图像消息
        self.image_pub = rospy.Publisher('usb_camera/image_raw', Image, queue_size=10)
        self.cap = VideoCapture(self.video_device)    
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)

    def usb_camera_read(self):
        
        return self.cap.read()

    def usb_camera_publisher(self):
        
        time = rospy.Time.now()
        
        bridge = CvBridge()
        ros_image = bridge.cv2_to_imgmsg(self.frame, encoding="bgr8")
        gray_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY) 
        compressed_image = bridge.cv2_to_compressed_imgmsg(gray_frame, dst_format='jpeg')
        compressed_image.header.stamp = time
        ros_image.header.stamp = time
        self.image_pub_compressed.publish(compressed_image)
        self.image_pub.publish(ros_image)



        
if __name__ == "__main__":        
    # 测试自定义VideoCapture类
    cap = VideoCapture(0)
    while True:
        t0 = time.time()
        frame = cap.read()
        t1 = time.time()
        print('cam time->{:.2f}ms'.format((t1-t0 )* 1000))
        # time.sleep(0.05)   # 模拟耗时操作，单位：秒   
        # cv2.imshow("frame", frame)
        if chr(cv2.waitKey(1)&255) == 'q':  # 按 q 退出
            cap.terminate()
            break

