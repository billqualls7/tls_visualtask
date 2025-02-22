// Generated by gencpp from file vt_msgs/CarLinebias.msg
// DO NOT EDIT!


#ifndef VT_MSGS_MESSAGE_CARLINEBIAS_H
#define VT_MSGS_MESSAGE_CARLINEBIAS_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace vt_msgs
{
template <class ContainerAllocator>
struct CarLinebias_
{
  typedef CarLinebias_<ContainerAllocator> Type;

  CarLinebias_()
    : bais(0.0)  {
    }
  CarLinebias_(const ContainerAllocator& _alloc)
    : bais(0.0)  {
  (void)_alloc;
    }



   typedef double _bais_type;
  _bais_type bais;





  typedef boost::shared_ptr< ::vt_msgs::CarLinebias_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vt_msgs::CarLinebias_<ContainerAllocator> const> ConstPtr;

}; // struct CarLinebias_

typedef ::vt_msgs::CarLinebias_<std::allocator<void> > CarLinebias;

typedef boost::shared_ptr< ::vt_msgs::CarLinebias > CarLinebiasPtr;
typedef boost::shared_ptr< ::vt_msgs::CarLinebias const> CarLinebiasConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vt_msgs::CarLinebias_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vt_msgs::CarLinebias_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::vt_msgs::CarLinebias_<ContainerAllocator1> & lhs, const ::vt_msgs::CarLinebias_<ContainerAllocator2> & rhs)
{
  return lhs.bais == rhs.bais;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::vt_msgs::CarLinebias_<ContainerAllocator1> & lhs, const ::vt_msgs::CarLinebias_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace vt_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::vt_msgs::CarLinebias_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vt_msgs::CarLinebias_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vt_msgs::CarLinebias_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vt_msgs::CarLinebias_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vt_msgs::CarLinebias_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vt_msgs::CarLinebias_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vt_msgs::CarLinebias_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b5f5aa12fa94be38b3fd420b3055f97e";
  }

  static const char* value(const ::vt_msgs::CarLinebias_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb5f5aa12fa94be38ULL;
  static const uint64_t static_value2 = 0xb3fd420b3055f97eULL;
};

template<class ContainerAllocator>
struct DataType< ::vt_msgs::CarLinebias_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vt_msgs/CarLinebias";
  }

  static const char* value(const ::vt_msgs::CarLinebias_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vt_msgs::CarLinebias_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 bais\n"
;
  }

  static const char* value(const ::vt_msgs::CarLinebias_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vt_msgs::CarLinebias_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.bais);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CarLinebias_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vt_msgs::CarLinebias_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vt_msgs::CarLinebias_<ContainerAllocator>& v)
  {
    s << indent << "bais: ";
    Printer<double>::stream(s, indent + "  ", v.bais);
  }
};

} // namespace message_operations
} // namespace ros

#endif // VT_MSGS_MESSAGE_CARLINEBIAS_H
