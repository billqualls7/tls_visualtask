'''
Author: wuyao sss
Date: 2024-03-01 11:11:30
LastEditors: EPAICAR EPAICAR@EPAICAR
LastEditTime: 2024-03-01 22:50:56
FilePath: /rqh/demo_py/getbias.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
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
        self.minpix = 30
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

        temp_xy = []
        mutation = False
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
                    y_current = np.int32(np.mean(nonzeroy[good_inds]))
                    # k = y_current/x_current
                    temp_xy.append((x_current, y_current))
                    
                    # print(k)
                    cv2.circle(img_half, (x_current, y_current), radius=5, color=(0, 0, 0), thickness=-1)
                    # 
            print("=================")

            temp_xy_len = len(temp_xy)
            if  temp_xy_len< 3:
                print('\033[31m no lines \033[0m')   
            else:
                for i in range(temp_xy_len-1):
                    A = temp_xy[0]
                    B = temp_xy[1]
                    k = (A[1]-B[1])/(A[0]-B[0])
                    del temp_xy[0]
                    if i == 0:
                        last_k = k
                        # print("k", k)

                        continue

                    error = abs(k-last_k)
                    last_k = k
                    
                    # print(A)
                    # print("error", error)
                    # print("k", k)

                    if error > 10:    #阈值
                        print("突变了")
                        mutation = True
                if not mutation:    # 如果没有突变
                    lane_inds = np.concatenate(lane_inds)
                    x = nonzerox[lane_inds] + trans
                    y = nonzeroy[lane_inds] 
                    fit = np.polyfit(y, x, 2)
                    
                    return fit, mutation
                else:
                    return [-1,-1,-1], mutation


                    # print(k)



        # try:
        #     fit = np.polyfit(y, x, 2)
        #     return fit
        # except: 
            
        #     return fit
        




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

            if win_xleft_high > self.midpoint:
                temp = win_xleft_high - self.midpoint
                win_xleft_high = win_xleft_high - temp
                win_xleft_low = win_xleft_low - temp
                print('change_left')  
            if win_xright_low <self.midpoint:
                temp = self.midpoint - win_xright_low
                win_xright_low += temp
                win_xright_high += temp  
                print("change_right")

            
            good_left_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) &
            (nonzerox >= win_xleft_low) &  (nonzerox < win_xleft_high)).nonzero()[0]
            good_right_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) &
            (nonzerox >= win_xright_low) &  (nonzerox < win_xright_high)).nonzero()[0]
            # Append these indices to the lists
            left_lane_inds.append(good_left_inds)
            right_lane_inds.append(good_right_inds)
            # If you found > minpix pixels, recenter next window on their mean position
            if len(good_left_inds) > self.minpix:#指定的阈值 minpix
                leftx_current = np.int32(np.mean(nonzerox[good_left_inds]))
                lefty_current = np.int32(np.mean(nonzeroy[good_left_inds]))
                
                # left_cnt+=1
                # if left_cnt >=2:
                left_can = 1#标志位，表示可以进一步搜索车道线
            print('minpix(right):'+str(len(good_right_inds)))
            if len(good_right_inds) > self.minpix:
                rightx_current = np.int32(np.mean(nonzerox[good_right_inds]))
                # right_cnt+=1
                # if right_cnt >=2:
                right_can = 1
        print('left_can:'+str(left_can))  
        print('right_can:'+str(right_can))
        # Concatenate the arrays of indices
        left_lane_inds = np.concatenate(left_lane_inds)#left_lane_inds 是一个列表，其中包含了每个窗口内找到的左车道线的非零像素点的索引数组
        print(left_lane_inds)
        right_lane_inds = np.concatenate(right_lane_inds)
        print(right_lane_inds)
        # Extract left and right line pixel positions
        leftx = nonzerox[left_lane_inds]#leftx 和 lefty 是左车道线的非零像素点在 x 和 y 方向上的坐标。
        lefty = nonzeroy[left_lane_inds]
        rightx = nonzerox[right_lane_inds]
        righty = nonzeroy[right_lane_inds]

        if left_can == 1 and right_can == 1:
            left_fit = np.polyfit(lefty, leftx, 2)#则分别使用 np.polyfit() 函数拟合左右车道线的二次多项式曲线，并返回拟合系数 left_fit 和 right_fit
            right_fit = np.polyfit(righty, rightx, 2)
            return left_fit, right_fit,left_can,right_can
        elif left_can == 1 and right_can == 0:
            left_fit = np.polyfit(lefty, leftx, 2)
            return left_fit, [0, 0, 0],left_can,right_can
        elif left_can == 0 and right_can == 1:
            right_fit = np.polyfit(righty, rightx, 2)
            return [0, 0, 0], right_fit,left_can,right_can
        elif left_can == 0 and right_can == 0:
            return [0, 0, 0], [0, 0, 0] ,left_can,right_can
        

    
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
        mid = 160
        img_l, img_r = self._roi_img(img)

        left, left_mutation= self.find_line(img_l,0, 0)
        # cv2.imwrite("../images/img_l.jpg",img_l)
        right, right_mutation= self.find_line(img_r, 160, self.midpoint)
        # cv2.imwrite("../images/img_r.jpg",img_r)

        if (not left_mutation) and (not right_mutation):
            bottom_x_left = calculate_bottom_x(left, self.bottom_y)
            bottom_x_right = calculate_bottom_x(right, self.bottom_y)
            angle = (bottom_x_left + bottom_x_right)/2 - mid
            return angle
        elif left_mutation:
            print("left_mutation 朝着发生突变的方向转弯，自行补充逻辑")
            pass
        elif right_mutation:
            print("right_mutation 朝着发生突变的方向转弯，自行补充逻辑")

            pass

        



        
        #可视化
        # mid = 160
        # angle = int(bottom_x_left / 2 + bottom_x_right / 2) - mid
        # # print(angle)
        # # cv2.line(img, (mid, 0), (mid,img.shape[0]), (0, 0, 255), thickness=10)
        # # cv2.line(img,(bottom_x_left,self.bottom_y),(bottom_x_right,self.bottom_y),(255,0,0), thickness=10)
        # # cv2.line(img, (mid, self.bottom_y), (int(bottom_x_left / 2 + bottom_x_right / 2), self.bottom_y), (0, 255, 0),
        # #         thickness=10)
        
        # # cv2.imwrite("../images/carlinrbias.jpg",img)
        
        # angle = (bottom_x_left + bottom_x_right)/2 - mid

        # return angle





if __name__ == '__main__':
    image = cv2.imread('../images/resized_image2.jpg', cv2.IMREAD_GRAYSCALE)
    # image = cv2.imread('../images/resized_img.jpg')
    resized_image = cv2.resize(image, (320, 240), interpolation=cv2.INTER_AREA)
    # cv2.imwrite("../images/resized_image3.jpg",resized_image)
    
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


