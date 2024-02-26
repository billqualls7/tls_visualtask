
(cl:in-package :asdf)

(defsystem "vt_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Box" :depends-on ("_package_Box"))
    (:file "_package_Box" :depends-on ("_package"))
    (:file "CarLinebias" :depends-on ("_package_CarLinebias"))
    (:file "_package_CarLinebias" :depends-on ("_package"))
    (:file "Yoloutput" :depends-on ("_package_Yoloutput"))
    (:file "_package_Yoloutput" :depends-on ("_package"))
  ))