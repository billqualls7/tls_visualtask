# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "vt_msgs: 3 messages, 0 services")

set(MSG_I_FLAGS "-Ivt_msgs:/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(vt_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg" NAME_WE)
add_custom_target(_vt_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "vt_msgs" "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg" ""
)

get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Yoloutput.msg" NAME_WE)
add_custom_target(_vt_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "vt_msgs" "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Yoloutput.msg" "vt_msgs/Box"
)

get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/CarLinebias.msg" NAME_WE)
add_custom_target(_vt_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "vt_msgs" "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/CarLinebias.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/CarLinebias.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vt_msgs
)
_generate_msg_cpp(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Yoloutput.msg"
  "${MSG_I_FLAGS}"
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vt_msgs
)
_generate_msg_cpp(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vt_msgs
)

### Generating Services

### Generating Module File
_generate_module_cpp(vt_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vt_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(vt_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(vt_msgs_generate_messages vt_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_cpp _vt_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Yoloutput.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_cpp _vt_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/CarLinebias.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_cpp _vt_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vt_msgs_gencpp)
add_dependencies(vt_msgs_gencpp vt_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vt_msgs_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/CarLinebias.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vt_msgs
)
_generate_msg_eus(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Yoloutput.msg"
  "${MSG_I_FLAGS}"
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vt_msgs
)
_generate_msg_eus(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vt_msgs
)

### Generating Services

### Generating Module File
_generate_module_eus(vt_msgs
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vt_msgs
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(vt_msgs_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(vt_msgs_generate_messages vt_msgs_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_eus _vt_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Yoloutput.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_eus _vt_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/CarLinebias.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_eus _vt_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vt_msgs_geneus)
add_dependencies(vt_msgs_geneus vt_msgs_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vt_msgs_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/CarLinebias.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vt_msgs
)
_generate_msg_lisp(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Yoloutput.msg"
  "${MSG_I_FLAGS}"
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vt_msgs
)
_generate_msg_lisp(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vt_msgs
)

### Generating Services

### Generating Module File
_generate_module_lisp(vt_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vt_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(vt_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(vt_msgs_generate_messages vt_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_lisp _vt_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Yoloutput.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_lisp _vt_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/CarLinebias.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_lisp _vt_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vt_msgs_genlisp)
add_dependencies(vt_msgs_genlisp vt_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vt_msgs_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/CarLinebias.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/vt_msgs
)
_generate_msg_nodejs(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Yoloutput.msg"
  "${MSG_I_FLAGS}"
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/vt_msgs
)
_generate_msg_nodejs(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/vt_msgs
)

### Generating Services

### Generating Module File
_generate_module_nodejs(vt_msgs
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/vt_msgs
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(vt_msgs_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(vt_msgs_generate_messages vt_msgs_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_nodejs _vt_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Yoloutput.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_nodejs _vt_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/CarLinebias.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_nodejs _vt_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vt_msgs_gennodejs)
add_dependencies(vt_msgs_gennodejs vt_msgs_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vt_msgs_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/CarLinebias.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vt_msgs
)
_generate_msg_py(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Yoloutput.msg"
  "${MSG_I_FLAGS}"
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vt_msgs
)
_generate_msg_py(vt_msgs
  "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vt_msgs
)

### Generating Services

### Generating Module File
_generate_module_py(vt_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vt_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(vt_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(vt_msgs_generate_messages vt_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Box.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_py _vt_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/Yoloutput.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_py _vt_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/epaicar/tls_visualtask/vt_ws/src/vt_msgs/msg/CarLinebias.msg" NAME_WE)
add_dependencies(vt_msgs_generate_messages_py _vt_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vt_msgs_genpy)
add_dependencies(vt_msgs_genpy vt_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vt_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vt_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vt_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(vt_msgs_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vt_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vt_msgs
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(vt_msgs_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vt_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vt_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(vt_msgs_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/vt_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/vt_msgs
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(vt_msgs_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vt_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vt_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vt_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(vt_msgs_generate_messages_py std_msgs_generate_messages_py)
endif()
