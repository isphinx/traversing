# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hero.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hero.proto',
  package='',
  serialized_pb='\n\nhero.proto\"0\n\x06LinkPB\x12\x0f\n\x07link_no\x18\x01 \x02(\x05\x12\x15\n\ris_activation\x18\x02 \x01(\x08\"2\n\x08RuntType\x12\x11\n\trunt_type\x18\x01 \x02(\x05\x12\x13\n\x04runt\x18\x02 \x03(\x0b\x32\x05.Runt\"(\n\x04Runt\x12\x0f\n\x07runt_po\x18\x01 \x02(\x05\x12\x0f\n\x07runt_id\x18\x02 \x02(\x05\"\xa2\x01\n\x06HeroPB\x12\x0f\n\x07hero_no\x18\x01 \x02(\x05\x12\r\n\x05level\x18\x02 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x03 \x01(\x05\x12\x13\n\x0b\x62reak_level\x18\x04 \x01(\x05\x12\x0e\n\x06refine\x18\x05 \x01(\x05\x12\x10\n\x08is_guard\x18\x06 \x01(\x08\x12\x16\n\x05links\x18\x07 \x03(\x0b\x32\x07.LinkPB\x12\x1c\n\trunt_type\x18\x08 \x03(\x0b\x32\t.RuntType')




_LINKPB = _descriptor.Descriptor(
  name='LinkPB',
  full_name='LinkPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='link_no', full_name='LinkPB.link_no', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_activation', full_name='LinkPB.is_activation', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_end=62,
)


_RUNTTYPE = _descriptor.Descriptor(
  name='RuntType',
  full_name='RuntType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='runt_type', full_name='RuntType.runt_type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='runt', full_name='RuntType.runt', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=64,
  serialized_end=114,
)


_RUNT = _descriptor.Descriptor(
  name='Runt',
  full_name='Runt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='runt_po', full_name='Runt.runt_po', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='runt_id', full_name='Runt.runt_id', index=1,
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
  serialized_start=116,
  serialized_end=156,
)


_HEROPB = _descriptor.Descriptor(
  name='HeroPB',
  full_name='HeroPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_no', full_name='HeroPB.hero_no', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='HeroPB.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='HeroPB.exp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='break_level', full_name='HeroPB.break_level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refine', full_name='HeroPB.refine', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_guard', full_name='HeroPB.is_guard', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='links', full_name='HeroPB.links', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='runt_type', full_name='HeroPB.runt_type', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=159,
  serialized_end=321,
)

_RUNTTYPE.fields_by_name['runt'].message_type = _RUNT
_HEROPB.fields_by_name['links'].message_type = _LINKPB
_HEROPB.fields_by_name['runt_type'].message_type = _RUNTTYPE
DESCRIPTOR.message_types_by_name['LinkPB'] = _LINKPB
DESCRIPTOR.message_types_by_name['RuntType'] = _RUNTTYPE
DESCRIPTOR.message_types_by_name['Runt'] = _RUNT
DESCRIPTOR.message_types_by_name['HeroPB'] = _HEROPB

class LinkPB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LINKPB

  # @@protoc_insertion_point(class_scope:LinkPB)

class RuntType(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNTTYPE

  # @@protoc_insertion_point(class_scope:RuntType)

class Runt(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNT

  # @@protoc_insertion_point(class_scope:Runt)

class HeroPB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROPB

  # @@protoc_insertion_point(class_scope:HeroPB)


# @@protoc_insertion_point(module_scope)
