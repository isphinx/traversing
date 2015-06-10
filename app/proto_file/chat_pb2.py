# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='',
  serialized_pb='\n\nchat.proto\"Y\n\x0e\x43hatObjectInfo\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\x11\n\tvip_level\x18\x03 \x01(\x05\x12\x16\n\x0eguild_position\x18\x04 \x01(\x05\"4\n\x12LoginToChatRequest\x12\x1e\n\x05owner\x18\x01 \x02(\x0b\x32\x0f.ChatObjectInfo\"\xb5\x01\n\x14\x43hatConectingRequest\x12\x1e\n\x05owner\x18\x01 \x02(\x0b\x32\x0f.ChatObjectInfo\x12\x0f\n\x07\x63hannel\x18\x02 \x02(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x02(\t\x12\x1e\n\x05other\x18\x04 \x01(\x0b\x32\x0f.ChatObjectInfo\x12\x10\n\x08guild_id\x18\x05 \x01(\x05\x12\x11\n\tvip_level\x18\x06 \x01(\x05\x12\x16\n\x0eguild_position\x18\x07 \x01(\x05\"C\n\x0c\x43hatResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x11\n\tresult_no\x18\x02 \x01(\x05\x12\x10\n\x08gag_time\x18\x03 \x01(\x05\"e\n\x13\x63hatMessageResponse\x12\x0f\n\x07\x63hannel\x18\x01 \x02(\x05\x12\x1e\n\x05owner\x18\x02 \x02(\x0b\x32\x0f.ChatObjectInfo\x12\x0f\n\x07\x63ontent\x18\x03 \x02(\t\x12\x0c\n\x04time\x18\x04 \x01(\x05')




_CHATOBJECTINFO = _descriptor.Descriptor(
  name='ChatObjectInfo',
  full_name='ChatObjectInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ChatObjectInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='ChatObjectInfo.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip_level', full_name='ChatObjectInfo.vip_level', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_position', full_name='ChatObjectInfo.guild_position', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=14,
  serialized_end=103,
)


_LOGINTOCHATREQUEST = _descriptor.Descriptor(
  name='LoginToChatRequest',
  full_name='LoginToChatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='LoginToChatRequest.owner', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=105,
  serialized_end=157,
)


_CHATCONECTINGREQUEST = _descriptor.Descriptor(
  name='ChatConectingRequest',
  full_name='ChatConectingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='ChatConectingRequest.owner', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='ChatConectingRequest.channel', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='ChatConectingRequest.content', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='other', full_name='ChatConectingRequest.other', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_id', full_name='ChatConectingRequest.guild_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip_level', full_name='ChatConectingRequest.vip_level', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_position', full_name='ChatConectingRequest.guild_position', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=160,
  serialized_end=341,
)


_CHATRESPONSE = _descriptor.Descriptor(
  name='ChatResponse',
  full_name='ChatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ChatResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_no', full_name='ChatResponse.result_no', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gag_time', full_name='ChatResponse.gag_time', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=343,
  serialized_end=410,
)


_CHATMESSAGERESPONSE = _descriptor.Descriptor(
  name='chatMessageResponse',
  full_name='chatMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='chatMessageResponse.channel', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owner', full_name='chatMessageResponse.owner', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='chatMessageResponse.content', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='chatMessageResponse.time', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=412,
  serialized_end=513,
)

_LOGINTOCHATREQUEST.fields_by_name['owner'].message_type = _CHATOBJECTINFO
_CHATCONECTINGREQUEST.fields_by_name['owner'].message_type = _CHATOBJECTINFO
_CHATCONECTINGREQUEST.fields_by_name['other'].message_type = _CHATOBJECTINFO
_CHATMESSAGERESPONSE.fields_by_name['owner'].message_type = _CHATOBJECTINFO
DESCRIPTOR.message_types_by_name['ChatObjectInfo'] = _CHATOBJECTINFO
DESCRIPTOR.message_types_by_name['LoginToChatRequest'] = _LOGINTOCHATREQUEST
DESCRIPTOR.message_types_by_name['ChatConectingRequest'] = _CHATCONECTINGREQUEST
DESCRIPTOR.message_types_by_name['ChatResponse'] = _CHATRESPONSE
DESCRIPTOR.message_types_by_name['chatMessageResponse'] = _CHATMESSAGERESPONSE

class ChatObjectInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHATOBJECTINFO

  # @@protoc_insertion_point(class_scope:ChatObjectInfo)

class LoginToChatRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGINTOCHATREQUEST

  # @@protoc_insertion_point(class_scope:LoginToChatRequest)

class ChatConectingRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHATCONECTINGREQUEST

  # @@protoc_insertion_point(class_scope:ChatConectingRequest)

class ChatResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHATRESPONSE

  # @@protoc_insertion_point(class_scope:ChatResponse)

class chatMessageResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHATMESSAGERESPONSE

  # @@protoc_insertion_point(class_scope:chatMessageResponse)


# @@protoc_insertion_point(module_scope)
