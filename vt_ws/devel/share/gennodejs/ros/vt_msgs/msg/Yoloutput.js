// Auto-generated. Do not edit!

// (in-package vt_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Box = require('./Box.js');

//-----------------------------------------------------------

class Yoloutput {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.classification = null;
      this.score = null;
      this.boxes = null;
    }
    else {
      if (initObj.hasOwnProperty('classification')) {
        this.classification = initObj.classification
      }
      else {
        this.classification = '';
      }
      if (initObj.hasOwnProperty('score')) {
        this.score = initObj.score
      }
      else {
        this.score = 0.0;
      }
      if (initObj.hasOwnProperty('boxes')) {
        this.boxes = initObj.boxes
      }
      else {
        this.boxes = new Box();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Yoloutput
    // Serialize message field [classification]
    bufferOffset = _serializer.string(obj.classification, buffer, bufferOffset);
    // Serialize message field [score]
    bufferOffset = _serializer.float64(obj.score, buffer, bufferOffset);
    // Serialize message field [boxes]
    bufferOffset = Box.serialize(obj.boxes, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Yoloutput
    let len;
    let data = new Yoloutput(null);
    // Deserialize message field [classification]
    data.classification = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [score]
    data.score = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [boxes]
    data.boxes = Box.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.classification.length;
    return length + 44;
  }

  static datatype() {
    // Returns string type for a message object
    return 'vt_msgs/Yoloutput';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9855b3e6d4943fe13cec77d13b1c419b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string classification
    float64 score
    
    Box boxes
    ================================================================================
    MSG: vt_msgs/Box
    float64 x1
    float64 x2
    float64 y1
    float64 y2
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Yoloutput(null);
    if (msg.classification !== undefined) {
      resolved.classification = msg.classification;
    }
    else {
      resolved.classification = ''
    }

    if (msg.score !== undefined) {
      resolved.score = msg.score;
    }
    else {
      resolved.score = 0.0
    }

    if (msg.boxes !== undefined) {
      resolved.boxes = Box.Resolve(msg.boxes)
    }
    else {
      resolved.boxes = new Box()
    }

    return resolved;
    }
};

module.exports = Yoloutput;
