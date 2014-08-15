# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shop.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='shop.proto',
  package='',
  serialized_pb='\n\nshop.proto\x1a\x0c\x63ommon.proto\"&\n\x0bShopRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0b\n\x03num\x18\x02 \x01(\x05\"{\n\x0cShopResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\'\n\x07\x63onsume\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\x12$\n\x04gain\x18\x03 \x01(\x0b\x32\x16.GameResourcesResponse')




_SHOPREQUEST = _descriptor.Descriptor(
  name='ShopRequest',
  full_name='ShopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ShopRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num', full_name='ShopRequest.num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=28,
  serialized_end=66,
)


_SHOPRESPONSE = _descriptor.Descriptor(
  name='ShopResponse',
  full_name='ShopResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='ShopResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume', full_name='ShopResponse.consume', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='ShopResponse.gain', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=68,
  serialized_end=191,
)

_SHOPRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_SHOPRESPONSE.fields_by_name['consume'].message_type = common_pb2._GAMERESOURCESRESPONSE
_SHOPRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
DESCRIPTOR.message_types_by_name['ShopRequest'] = _SHOPREQUEST
DESCRIPTOR.message_types_by_name['ShopResponse'] = _SHOPRESPONSE

class ShopRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHOPREQUEST

  # @@protoc_insertion_point(class_scope:ShopRequest)

class ShopResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHOPRESPONSE

  # @@protoc_insertion_point(class_scope:ShopResponse)


# @@protoc_insertion_point(module_scope)
