; Auto-generated. Do not edit!


(cl:in-package vt_msgs-msg)


;//! \htmlinclude Yoloutput.msg.html

(cl:defclass <Yoloutput> (roslisp-msg-protocol:ros-message)
  ((classification
    :reader classification
    :initarg :classification
    :type cl:string
    :initform "")
   (score
    :reader score
    :initarg :score
    :type cl:float
    :initform 0.0)
   (boxes
    :reader boxes
    :initarg :boxes
    :type vt_msgs-msg:Box
    :initform (cl:make-instance 'vt_msgs-msg:Box)))
)

(cl:defclass Yoloutput (<Yoloutput>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Yoloutput>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Yoloutput)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vt_msgs-msg:<Yoloutput> is deprecated: use vt_msgs-msg:Yoloutput instead.")))

(cl:ensure-generic-function 'classification-val :lambda-list '(m))
(cl:defmethod classification-val ((m <Yoloutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vt_msgs-msg:classification-val is deprecated.  Use vt_msgs-msg:classification instead.")
  (classification m))

(cl:ensure-generic-function 'score-val :lambda-list '(m))
(cl:defmethod score-val ((m <Yoloutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vt_msgs-msg:score-val is deprecated.  Use vt_msgs-msg:score instead.")
  (score m))

(cl:ensure-generic-function 'boxes-val :lambda-list '(m))
(cl:defmethod boxes-val ((m <Yoloutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vt_msgs-msg:boxes-val is deprecated.  Use vt_msgs-msg:boxes instead.")
  (boxes m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Yoloutput>) ostream)
  "Serializes a message object of type '<Yoloutput>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'classification))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'classification))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'score))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'boxes) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Yoloutput>) istream)
  "Deserializes a message object of type '<Yoloutput>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'classification) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'classification) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'score) (roslisp-utils:decode-double-float-bits bits)))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'boxes) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Yoloutput>)))
  "Returns string type for a message object of type '<Yoloutput>"
  "vt_msgs/Yoloutput")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Yoloutput)))
  "Returns string type for a message object of type 'Yoloutput"
  "vt_msgs/Yoloutput")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Yoloutput>)))
  "Returns md5sum for a message object of type '<Yoloutput>"
  "9855b3e6d4943fe13cec77d13b1c419b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Yoloutput)))
  "Returns md5sum for a message object of type 'Yoloutput"
  "9855b3e6d4943fe13cec77d13b1c419b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Yoloutput>)))
  "Returns full string definition for message of type '<Yoloutput>"
  (cl:format cl:nil "string classification~%float64 score~%~%Box boxes~%================================================================================~%MSG: vt_msgs/Box~%float64 x1~%float64 x2~%float64 y1~%float64 y2~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Yoloutput)))
  "Returns full string definition for message of type 'Yoloutput"
  (cl:format cl:nil "string classification~%float64 score~%~%Box boxes~%================================================================================~%MSG: vt_msgs/Box~%float64 x1~%float64 x2~%float64 y1~%float64 y2~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Yoloutput>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'classification))
     8
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'boxes))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Yoloutput>))
  "Converts a ROS message object to a list"
  (cl:list 'Yoloutput
    (cl:cons ':classification (classification msg))
    (cl:cons ':score (score msg))
    (cl:cons ':boxes (boxes msg))
))
