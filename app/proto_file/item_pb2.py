# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: item.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='item.proto',
  package='proto_file.item',
  serialized_pb='\n\nitem.proto\x12\x0fproto_file.item\")\n\x04Item\x12\x0f\n\x07item_no\x18\x01 \x02(\x05\x12\x10\n\x08item_num\x18\x02 \x02(\x05\"4\n\rItemsResponse\x12#\n\x04item\x18\x01 \x03(\x0b\x32\x15.proto_file.item.Item')




_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='proto_file.item.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_no', full_name='proto_file.item.Item.item_no', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_num', full_name='proto_file.item.Item.item_num', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=31,
  serialized_end=72,
)


_ITEMSRESPONSE = _descriptor.Descriptor(
  name='ItemsResponse',
  full_name='proto_file.item.ItemsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='proto_file.item.ItemsResponse.item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=74,
  serialized_end=126,
)

_ITEMSRESPONSE.fields_by_name['item'].message_type = _ITEM
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['ItemsResponse'] = _ITEMSRESPONSE

class Item(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEM

  # @@protoc_insertion_point(class_scope:proto_file.item.Item)

class ItemsResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMSRESPONSE

  # @@protoc_insertion_point(class_scope:proto_file.item.ItemsResponse)


# @@protoc_insertion_point(module_scope)