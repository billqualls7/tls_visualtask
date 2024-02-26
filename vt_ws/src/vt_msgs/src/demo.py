'''
Author: EPAICAR EPAICAR@EPAICAR
Date: 2024-02-14 21:31:09
LastEditors: EPAICAR EPAICAR@EPAICAR
LastEditTime: 2024-02-14 21:37:40
FilePath: /epaicar/tls_visualtask/vt_ws/src/vt_msgs/src/demo.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import rospy
from vt_msgs.msg import Yoloutput

yolo_msg = Yoloutput()
yolo_msg.classification = '0'
yolo_msg.boxes.top = '1.1'
