;; Auto-generated. Do not edit!


(when (boundp 'vt_msgs::CarLinebias)
  (if (not (find-package "VT_MSGS"))
    (make-package "VT_MSGS"))
  (shadow 'CarLinebias (find-package "VT_MSGS")))
(unless (find-package "VT_MSGS::CARLINEBIAS")
  (make-package "VT_MSGS::CARLINEBIAS"))

(in-package "ROS")
;;//! \htmlinclude CarLinebias.msg.html


(defclass vt_msgs::CarLinebias
  :super ros::object
  :slots (_bais ))

(defmethod vt_msgs::CarLinebias
  (:init
   (&key
    ((:bais __bais) 0.0)
    )
   (send-super :init)
   (setq _bais (float __bais))
   self)
  (:bais
   (&optional __bais)
   (if __bais (setq _bais __bais)) _bais)
  (:serialization-length
   ()
   (+
    ;; float64 _bais
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _bais
       (sys::poke _bais (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _bais
     (setq _bais (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get vt_msgs::CarLinebias :md5sum-) "b5f5aa12fa94be38b3fd420b3055f97e")
(setf (get vt_msgs::CarLinebias :datatype-) "vt_msgs/CarLinebias")
(setf (get vt_msgs::CarLinebias :definition-)
      "float64 bais

")



(provide :vt_msgs/CarLinebias "b5f5aa12fa94be38b3fd420b3055f97e")


