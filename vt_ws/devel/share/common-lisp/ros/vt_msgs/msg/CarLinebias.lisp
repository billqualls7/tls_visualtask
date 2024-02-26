; Auto-generated. Do not edit!


(cl:in-package vt_msgs-msg)


;//! \htmlinclude CarLinebias.msg.html

(cl:defclass <CarLinebias> (roslisp-msg-protocol:ros-message)
  ((bais
    :reader bais
    :initarg :bais
    :type cl:float
    :initform 0.0))
)

(cl:defclass CarLinebias (<CarLinebias>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CarLinebias>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CarLinebias)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vt_msgs-msg:<CarLinebias> is deprecated: use vt_msgs-msg:CarLinebias instead.")))

(cl:ensure-generic-function 'bais-val :lambda-list '(m))
(cl:defmethod bais-val ((m <CarLinebias>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vt_msgs-msg:bais-val is deprecated.  Use vt_msgs-msg:bais instead.")
  (bais m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CarLinebias>) ostream)
  "Serializes a message object of type '<CarLinebias>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'bais))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CarLinebias>) istream)
  "Deserializes a message object of type '<CarLinebias>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'bais) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CarLinebias>)))
  "Returns string type for a message object of type '<CarLinebias>"
  "vt_msgs/CarLinebias")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CarLinebias)))
  "Returns string type for a message object of type 'CarLinebias"
  "vt_msgs/CarLinebias")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CarLinebias>)))
  "Returns md5sum for a message object of type '<CarLinebias>"
  "b5f5aa12fa94be38b3fd420b3055f97e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CarLinebias)))
  "Returns md5sum for a message object of type 'CarLinebias"
  "b5f5aa12fa94be38b3fd420b3055f97e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CarLinebias>)))
  "Returns full string definition for message of type '<CarLinebias>"
  (cl:format cl:nil "float64 bais~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CarLinebias)))
  "Returns full string definition for message of type 'CarLinebias"
  (cl:format cl:nil "float64 bais~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CarLinebias>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CarLinebias>))
  "Converts a ROS message object to a list"
  (cl:list 'CarLinebias
    (cl:cons ':bais (bais msg))
))
