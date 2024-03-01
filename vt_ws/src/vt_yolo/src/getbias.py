'''
Author: wuyao sss
Date: 2024-03-01 11:11:30
LastEditors: EPAICAR EPAICAR@EPAICAR
LastEditTime: 2024-03-01 22:50:56
FilePath: /rqh/demo_py/getbias.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numba
import numpy as np
import time
import cv2
from multiprocessing import Pool
import threading
from queue import Queue
import concurrent.futures




def calculate_bottom_x(left, bottom_y):
    # bottom_x_left = int(left[0] * (bottom_y ** 2) + left[1] * bottom_y + left[2])
    return int(left[0] * (bottom_y ** 2) + left[1] * bottom_y + left[2])


'''
description: img.shape[0]---height deflaut:240
             img.shape[1]---weight deflaut:320
return {*}
'''
class GetAngle:
    def __init__(self):
        self.nwindows = 4
        self.margin = 100
        self.minpix = 100
        self.minLane = 100
        
        self.height = 240
        self.weight = 320
        self.midpoint = 160      # np.int32(img.shape[1]/2)  320
        self.window_height = 60  # np.int32(img.shape[0]/nwindows)  240
        self.bottom_y = 120      # int(self.img.shape[0]/2)
        self.h = [0,240]
        self.w = [0,320]
        
        

        self.window_ranges = self._calculate_window_ranges()
        # print(self.window_ranges)
        self.fit =[-100,-100,-100]

    def _calculate_window_ranges(self):
        window_ranges = []
        for window in range(self.nwindows):
            start = self.h[1] - int(self.h[0] + (self.h[1] - self.h[0]) * window / self.nwindows)
            end = self.h[1] - int(self.h[0] + (self.h[1] - self.h[0]) * (window + 1) / self.nwindows)
            window_ranges.append((start, end))
        return window_ranges

    def _roi_img(self,img):
        '''
        description: 
        return {*}   left_half, right_half
        '''        
        return img[:, :self.midpoint].copy(),  img[:, self.midpoint:].copy()
        # left_half = image[:, :self.midpoint//2]
        # right_half = image[:, self.midpoint//2:]

    def find_line(self, img_half, x_current,trans):
        '''
        description: trans 右车道线的补偿
        return {*}
        '''        
        nonzero_coords = cv2.findNonZero(img_half)
        fit =[-100,-100,-100]
        if nonzero_coords is not None:
            nonzero_coords = nonzero_coords[:, 0, :]  # 剥离多余的维度
            nonzeroy = nonzero_coords[:, 1]
            nonzerox = nonzero_coords[:, 0]
            lane_inds = []
            for window in range(self.nwindows):
                start, end = self.window_ranges[window]
                histogram = np.sum(img_half[end:start,0:160], axis=0)
                x_current = np.argmax(histogram) if np.argmax(histogram) > self.minLane else x_current
                
                win_y_high = start
                win_y_low = end

                win_x_low = x_current - self.margin
                win_x_high = x_current + self.margin
                good_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) &
                (nonzerox >= win_x_low) &  (nonzerox < win_x_high)).nonzero()[0]
                lane_inds.append(good_inds)
                if len(good_inds) > self.minpix:
                    x_current = np.int32(np.mean(nonzerox[good_inds]))
            
            lane_inds = np.concatenate(lane_inds)
            x = nonzerox[lane_inds] + trans
            y = nonzeroy[lane_inds] 
        try:
            fit = np.polyfit(y, x, 2)
            return fit
        except: 
            
            return fit
        




    def find_line_fit(self,img):
        left_lane_inds = []
        right_lane_inds = []

        leftx_current = self.w[0]
        rightx_current = self.w[1]



        nonzero_coords = cv2.findNonZero(img)
        nonzero_coords = nonzero_coords[:, 0, :]  # 剥离多余的维度
        nonzeroy = nonzero_coords[:, 1]
        nonzerox = nonzero_coords[:, 0]
        t0 = time.time()
        for window in range(self.nwindows):
            start, end = self.window_ranges[window]
            # print(start)
            # print(end)

            # histogram = cv2.calcHist([img[end:start, w[0]:w[1]]], [0], None, [256], [0, 256])        

            histogram = np.sum(img[end:start,self.w[0]:self.w[1]], axis=0)
            # histogram = calculate_histogram(img, end, start, w)

            leftx_current = np.argmax(histogram[:self.midpoint]) if np.argmax(histogram[:self.midpoint]) > self.minLane else leftx_current
            rightx_current = np.argmax(histogram[self.midpoint:]) + self.midpoint if np.argmax(histogram[self.midpoint:]) > self.minLane else rightx_current
            # rightx_current = np.argmax(histogram[self.midpoint:])  if np.argmax(histogram[self.midpoint:]) > self.minLane else rightx_current


            # Identify window boundaries in x and y (and right and left)
            win_y_low = end
            # print(win_y_low)
            win_y_high = start
            # if  start == win_y_high:
            #     print(win_y_high)

            win_xleft_low = leftx_current - self.margin
            win_xleft_high = leftx_current + self.margin
            win_xright_low = rightx_current - self.margin
            win_xright_high = rightx_current + self.margin

            good_left_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) &
            (nonzerox >= win_xleft_low) &  (nonzerox < win_xleft_high)).nonzero()[0]
            good_right_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) &
            (nonzerox >= win_xright_low) &  (nonzerox < win_xright_high)).nonzero()[0]
            # Append these indices to the lists
            left_lane_inds.append(good_left_inds)
            right_lane_inds.append(good_right_inds)
            # If you found > minpix pixels, recenter next window on their mean position
            if len(good_left_inds) > self.minpix:
                leftx_current = np.int32(np.mean(nonzerox[good_left_inds]))
            if len(good_right_inds) > self.minpix:
                rightx_current = np.int32(np.mean(nonzerox[good_right_inds]))
        t1 = time.time()
        # print("for:",(t1-t0)*1000)
        # Concatenate the arrays of indices
        left_lane_inds = np.concatenate(left_lane_inds)
        right_lane_inds = np.concatenate(right_lane_inds)

        # Extract left and right line pixel positions
        leftx = nonzerox[left_lane_inds]
        lefty = nonzeroy[left_lane_inds]
        rightx = nonzerox[right_lane_inds]
        righty = nonzeroy[right_lane_inds]

        # Fit a second order polynomial to each
        try:
            t0 = time.time()
            left_fit = np.polyfit(lefty, leftx, 2)
            right_fit = np.polyfit(righty, rightx, 2)
            t1 = time.time()
            # print("polyfit:",(t1-t0)*1000)
            # print(right_fit)
            
            return left_fit, right_fit
        except:
            # print(previous_right_fit)
            return [-100, -100, -100], [-100, -100, -100]
        

    
    def find_calculate(self,img, w, trans, bottom_y):
        line = self.find_line(img,w, trans)
        bottom_x = calculate_bottom_x(line, bottom_y)
        return bottom_x




    def get_angle_wrapper(self):
        img_l, img_r = self._roi_img(self.img.copy())
        # result_queue = Queue()

        # thread_left = threading.Thread(target=self.find_calculate, args=(img_l, 0, 0, self.bottom_y))
        # thread_right = threading.Thread(target=self.find_calculate, args=(img_r, 160, self.midpoint, self.bottom_y))
        # thread_left.start()
        # thread_right.start()

        # thread_left.join()
        # thread_right.join()

        # result_left = result_queue.get()
        # result_right = result_queue.get()


        with concurrent.futures.ProcessPoolExecutor() as executor:
            future_left = executor.submit(self.find_calculate, img_l, 0, 0, self.bottom_y)
            future_right = executor.submit(self.find_calculate, img_r, 160, self.midpoint, self.bottom_y)
            result_left = future_left.result()
            result_right = future_right.result()
        angle = int(result_left / 2 + result_right / 2) - self.midpoint

        print(angle)





    def get_angle(self, img):
        # img = self.img.copy()
        img_l, img_r = self._roi_img(img)

        left = self.find_line(img_l,0, 0)
        right = self.find_line(img_r, 160, self.midpoint)


        bottom_x_left = calculate_bottom_x(left, self.bottom_y)
        bottom_x_right = calculate_bottom_x(right, self.bottom_y)
        
        #可视化
        mid = 160
        angle = int(bottom_x_left / 2 + bottom_x_right / 2) - mid
        # print(angle)
        # cv2.line(img, (mid, 0), (mid,img.shape[0]), (0, 0, 255), thickness=10)
        # cv2.line(img,(bottom_x_left,self.bottom_y),(bottom_x_right,self.bottom_y),(255,0,0), thickness=10)
        # cv2.line(img, (mid, self.bottom_y), (int(bottom_x_left / 2 + bottom_x_right / 2), self.bottom_y), (0, 255, 0),
        #         thickness=10)
        
        # cv2.imwrite("../images/carlinrbias.jpg",img)
        
        angle = (bottom_x_left + bottom_x_right)/2 - mid

        return angle





if __name__ == '__main__':
    image = cv2.imread('../images/mask.jpg', cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(image, (240, 320), interpolation=cv2.INTER_AREA)
    gt = GetAngle()
    # print(image.shape)
    # print(type(image))
    
    total_time = 0
    num_iterations = 10
    num_skipped = 5

    for i in range(num_iterations):
        t0 = time.time()
        print(gt.get_angle(resized_image))
        # gt.get_angle_wrapper()
        t1 = time.time()
        elapsed_time = (t1 - t0) * 1000
        if i >= num_skipped:
            total_time += elapsed_time
        # print(elapsed_time)

    average_time = total_time / (num_iterations - num_skipped)
    print("Average time (after skipping first {}): {} ms".format(num_skipped, average_time))


