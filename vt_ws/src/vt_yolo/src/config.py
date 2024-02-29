'''
Author: EPAICAR EPAICAR@EPAICAR
Date: 2024-02-14 17:20:04
LastEditors: EPAICAR EPAICAR@EPAICAR
LastEditTime: 2024-02-29 11:06:41
FilePath: /epaicar/tls_visualtask/vt_ws/src/vt_yolo/src/config.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import yaml

class YAMLParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cam_device = 0
        self.engine_file_path = "../model/yolov5n7.engine"
        self.ONCF_THRESH = 0.5
        self.IOU_THRESHOLD = 0.4
        self.categories = []

    def get_data(self):
        with open(self.file_path, 'r') as file:
            try:
                data = yaml.safe_load(file)
                self.cam_device = data["cam_device"]
                self.engine_file_path = data["engine_file_path"]
                self.CONF_THRESH = data["CONF_THRESH"]
                self.IOU_THRESHOLD = data["IOU_THRESHOLD"]
                self.categories = data["categories"]
                self.colorful = data["colorful"]
                
            except yaml.YAMLError as e:
                print(f"Error parsing YAML file: {e}")

if __name__ == '__main__':
    parser = YAMLParser('../config/yolov5_det.yaml')
    parser.get_data()
    print(len(parser.categories))
    print((parser.categories[0]))
