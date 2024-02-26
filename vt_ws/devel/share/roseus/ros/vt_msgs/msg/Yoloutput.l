;; Auto-generated. Do not edit!


(when (boundp 'vt_msgs::Yoloutput)
  (if (not (find-package "VT_MSGS"))
    (make-package "VT_MSGS"))
  (shadow 'Yoloutput (find-package "VT_MSGS")))
(unless (find-package "VT_MSGS::YOLOUTPUT")
  (make-package "VT_MSGS::YOLOUTPUT"))

(in-package "ROS")
;;//! \htmlinclude Yoloutput.msg.html


(defclass vt_msgs::Yoloutput
  :super ros::object
  :slots (_classification _score _boxes ))

(defmethod vt_msgs::Yoloutput
  (:init
   (&key
    ((:classification __classification) "")
    ((:score __score) 0.0)
    ((:boxes __boxes) (instance vt_msgs::Box :init))
    )
   (send-super :init)
   (setq _classification (string __classification))
   (setq _score (float __score))
   (setq _boxes __boxes)
   self)
  (:classification
   (&optional __classification)
   (if __classification (setq _classification __classification)) _classification)
  (:score
   (&optional __score)
   (if __score (setq _score __score)) _score)
  (:boxes
   (&rest __boxes)
   (if (keywordp (car __boxes))
       (send* _boxes __boxes)
     (progn
       (if __boxes (setq _boxes (car __boxes)))
       _boxes)))
  (:serialization-length
   ()
   (+
    ;; string _classification
    4 (length _classification)
    ;; float64 _score
    8
    ;; vt_msgs/Box _boxes
    (send _boxes :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _classification
       (write-long (length _classification) s) (princ _classification s)
     ;; float64 _score
       (sys::poke _score (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; vt_msgs/Box _boxes
       (send _boxes :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _classification
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _classification (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _score
     (setq _score (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; vt_msgs/Box _boxes
     (send _boxes :deserialize buf ptr-) (incf ptr- (send _boxes :serialization-length))
   ;;
   self)
  )

(setf (get vt_msgs::Yoloutput :md5sum-) "9855b3e6d4943fe13cec77d13b1c419b")
(setf (get vt_msgs::Yoloutput :datatype-) "vt_msgs/Yoloutput")
(setf (get vt_msgs::Yoloutput :definition-)
      "string classification
float64 score

Box boxes
================================================================================
MSG: vt_msgs/Box
float64 x1
float64 x2
float64 y1
float64 y2
")



(provide :vt_msgs/Yoloutput "9855b3e6d4943fe13cec77d13b1c419b")


