// Auto-generated. Do not edit!

// (in-package vt_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class CarLinebias {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.bais = null;
    }
    else {
      if (initObj.hasOwnProperty('bais')) {
        this.bais = initObj.bais
      }
      else {
        this.bais = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CarLinebias
    // Serialize message field [bais]
    bufferOffset = _serializer.float64(obj.bais, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CarLinebias
    let len;
    let data = new CarLinebias(null);
    // Deserialize message field [bais]
    data.bais = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'vt_msgs/CarLinebias';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b5f5aa12fa94be38b3fd420b3055f97e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 bais
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CarLinebias(null);
    if (msg.bais !== undefined) {
      resolved.bais = msg.bais;
    }
    else {
      resolved.bais = 0.0
    }

    return resolved;
    }
};

module.exports = CarLinebias;
