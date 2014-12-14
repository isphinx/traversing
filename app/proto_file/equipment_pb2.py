# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: equipment.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='equipment.proto',
  package='',
  serialized_pb='\n\x0f\x65quipment.proto\"\'\n\x0cSetEquipment\x12\n\n\x02no\x18\x01 \x02(\x05\x12\x0b\n\x03num\x18\x02 \x01(\x05\"K\n\x11\x45nhanceDataFormat\x12\x11\n\tbefore_lv\x18\x01 \x01(\x05\x12\x10\n\x08\x61\x66ter_lv\x18\x02 \x01(\x05\x12\x11\n\tcost_coin\x18\x03 \x01(\x05\"\xb9\x01\n\x0b\x45quipmentPB\x12\n\n\x02id\x18\x01 \x02(\t\x12\n\n\x02no\x18\x02 \x01(\x05\x12\x15\n\rstrengthen_lv\x18\x03 \x01(\x05\x12\x14\n\x0c\x61wakening_lv\x18\x04 \x01(\x05\x12\x16\n\x0enobbing_effect\x18\x07 \x01(\x05\x12\x0f\n\x07hero_no\x18\x05 \x01(\x05\x12\x1a\n\x03set\x18\x06 \x01(\x0b\x32\r.SetEquipment\x12 \n\x04\x64\x61ta\x18\x08 \x03(\x0b\x32\x12.EnhanceDataFormat')




_SETEQUIPMENT = _descriptor.Descriptor(
  name='SetEquipment',
  full_name='SetEquipment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='no', full_name='SetEquipment.no', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num', full_name='SetEquipment.num', index=1,
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
  serialized_start=19,
  serialized_end=58,
)


_ENHANCEDATAFORMAT = _descriptor.Descriptor(
  name='EnhanceDataFormat',
  full_name='EnhanceDataFormat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='before_lv', full_name='EnhanceDataFormat.before_lv', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='after_lv', full_name='EnhanceDataFormat.after_lv', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cost_coin', full_name='EnhanceDataFormat.cost_coin', index=2,
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
  serialized_start=60,
  serialized_end=135,
)


_EQUIPMENTPB = _descriptor.Descriptor(
  name='EquipmentPB',
  full_name='EquipmentPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EquipmentPB.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='no', full_name='EquipmentPB.no', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strengthen_lv', full_name='EquipmentPB.strengthen_lv', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='awakening_lv', full_name='EquipmentPB.awakening_lv', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nobbing_effect', full_name='EquipmentPB.nobbing_effect', index=4,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_no', full_name='EquipmentPB.hero_no', index=5,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set', full_name='EquipmentPB.set', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='EquipmentPB.data', index=7,
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
  serialized_start=138,
  serialized_end=323,
)

_EQUIPMENTPB.fields_by_name['set'].message_type = _SETEQUIPMENT
_EQUIPMENTPB.fields_by_name['data'].message_type = _ENHANCEDATAFORMAT
DESCRIPTOR.message_types_by_name['SetEquipment'] = _SETEQUIPMENT
DESCRIPTOR.message_types_by_name['EnhanceDataFormat'] = _ENHANCEDATAFORMAT
DESCRIPTOR.message_types_by_name['EquipmentPB'] = _EQUIPMENTPB

class SetEquipment(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SETEQUIPMENT

  # @@protoc_insertion_point(class_scope:SetEquipment)

class EnhanceDataFormat(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENHANCEDATAFORMAT

  # @@protoc_insertion_point(class_scope:EnhanceDataFormat)

class EquipmentPB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EQUIPMENTPB

  # @@protoc_insertion_point(class_scope:EquipmentPB)


# @@protoc_insertion_point(module_scope)
