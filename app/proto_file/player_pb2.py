# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: player.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='player.proto',
  package='',
  serialized_pb='\n\x0cplayer.proto\":\n\tFinancePB\x12\x0c\n\x04\x63oin\x18\x01 \x01(\x05\x12\x0c\n\x04gold\x18\x02 \x01(\x05\x12\x11\n\thero_soul\x18\x03 \x01(\x05\":\n\x08PlayerPB\x12\x11\n\tplayer_id\x18\x01 \x02(\x03\x12\x1b\n\x07\x66inance\x18\x02 \x01(\x0b\x32\n.FinancePB')




_FINANCEPB = _descriptor.Descriptor(
  name='FinancePB',
  full_name='FinancePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coin', full_name='FinancePB.coin', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='FinancePB.gold', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_soul', full_name='FinancePB.hero_soul', index=2,
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
  serialized_start=16,
  serialized_end=74,
)


_PLAYERPB = _descriptor.Descriptor(
  name='PlayerPB',
  full_name='PlayerPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='PlayerPB.player_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finance', full_name='PlayerPB.finance', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=76,
  serialized_end=134,
)

_PLAYERPB.fields_by_name['finance'].message_type = _FINANCEPB
DESCRIPTOR.message_types_by_name['FinancePB'] = _FINANCEPB
DESCRIPTOR.message_types_by_name['PlayerPB'] = _PLAYERPB

class FinancePB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FINANCEPB

  # @@protoc_insertion_point(class_scope:FinancePB)

class PlayerPB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PLAYERPB

  # @@protoc_insertion_point(class_scope:PlayerPB)


# @@protoc_insertion_point(module_scope)