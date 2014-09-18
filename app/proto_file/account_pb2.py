# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='account.proto',
  package='',
  serialized_pb='\n\raccount.proto\"\x19\n\nAccountKey\x12\x0b\n\x03key\x18\x01 \x02(\t\"2\n\x0f\x41\x63\x63ountResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\'\n\x13\x41\x63\x63ountLoginRequest\x12\x10\n\x08passport\x18\x01 \x02(\t')




_ACCOUNTKEY = _descriptor.Descriptor(
  name='AccountKey',
  full_name='AccountKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='AccountKey.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=17,
  serialized_end=42,
)


_ACCOUNTRESPONSE = _descriptor.Descriptor(
  name='AccountResponse',
  full_name='AccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='AccountResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='AccountResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=44,
  serialized_end=94,
)


_ACCOUNTLOGINREQUEST = _descriptor.Descriptor(
  name='AccountLoginRequest',
  full_name='AccountLoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='passport', full_name='AccountLoginRequest.passport', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=96,
  serialized_end=135,
)

DESCRIPTOR.message_types_by_name['AccountKey'] = _ACCOUNTKEY
DESCRIPTOR.message_types_by_name['AccountResponse'] = _ACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['AccountLoginRequest'] = _ACCOUNTLOGINREQUEST

class AccountKey(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACCOUNTKEY

  # @@protoc_insertion_point(class_scope:AccountKey)

class AccountResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACCOUNTRESPONSE

  # @@protoc_insertion_point(class_scope:AccountResponse)

class AccountLoginRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACCOUNTLOGINREQUEST

  # @@protoc_insertion_point(class_scope:AccountLoginRequest)


# @@protoc_insertion_point(module_scope)
