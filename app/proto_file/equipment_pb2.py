# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: equipment.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='equipment.proto',
  package='',
  serialized_pb='\n\x0f\x65quipment.proto\x1a\x0c\x63ommon.proto\"\'\n\x0cSetEquipment\x12\n\n\x02no\x18\x01 \x02(\x05\x12\x0b\n\x03num\x18\x02 \x01(\x05\"K\n\x11\x45nhanceDataFormat\x12\x11\n\tbefore_lv\x18\x01 \x01(\x05\x12\x10\n\x08\x61\x66ter_lv\x18\x02 \x01(\x05\x12\x11\n\tcost_coin\x18\x03 \x01(\x05\"\x97\x01\n\x0b\x45quipmentPB\x12\n\n\x02id\x18\x01 \x02(\t\x12\n\n\x02no\x18\x02 \x01(\x05\x12\x15\n\rstrengthen_lv\x18\x03 \x01(\x05\x12\x14\n\x0c\x61wakening_lv\x18\x04 \x01(\x05\x12\x16\n\x0enobbing_effect\x18\x07 \x01(\x05\x12\x0f\n\x07hero_no\x18\x05 \x01(\x05\x12\x1a\n\x03set\x18\x06 \x01(\x0b\x32\r.SetEquipment\"0\n\x14GetEquipmentsRequest\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12\n\n\x02id\x18\x02 \x01(\t\"U\n\x14GetEquipmentResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x1f\n\tequipment\x18\x02 \x03(\x0b\x32\x0c.EquipmentPB\"@\n\x17\x45nhanceEquipmentRequest\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x0b\n\x03num\x18\x03 \x01(\x05\"Z\n\x18\x45nhanceEquipmentResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12 \n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x12.EnhanceDataFormat\"%\n\x17\x43omposeEquipmentRequest\x12\n\n\x02no\x18\x01 \x02(\t\"S\n\x18\x43omposeEquipmentResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x19\n\x03\x65qu\x18\x02 \x01(\x0b\x32\x0c.EquipmentPB\"%\n\x17NobbingEquipmentRequest\x12\n\n\x02id\x18\x01 \x02(\t\"v\n\x18NobbingEquipmentResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x19\n\x03\x65qu\x18\x02 \x01(\x0b\x32\x0c.EquipmentPB\x12!\n\x03\x63gr\x18\x03 \x03(\x0b\x32\x14.CommonGameResources\"%\n\x17MeltingEquipmentRequest\x12\n\n\x02id\x18\x01 \x02(\t\"[\n\x18MeltingEquipmentResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12!\n\x03\x63gr\x18\x03 \x03(\x0b\x32\x14.CommonGameResources')




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
  serialized_start=33,
  serialized_end=72,
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
  serialized_start=74,
  serialized_end=149,
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
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=152,
  serialized_end=303,
)


_GETEQUIPMENTSREQUEST = _descriptor.Descriptor(
  name='GetEquipmentsRequest',
  full_name='GetEquipmentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GetEquipmentsRequest.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='GetEquipmentsRequest.id', index=1,
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
  serialized_start=305,
  serialized_end=353,
)


_GETEQUIPMENTRESPONSE = _descriptor.Descriptor(
  name='GetEquipmentResponse',
  full_name='GetEquipmentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='GetEquipmentResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipment', full_name='GetEquipmentResponse.equipment', index=1,
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
  serialized_start=355,
  serialized_end=440,
)


_ENHANCEEQUIPMENTREQUEST = _descriptor.Descriptor(
  name='EnhanceEquipmentRequest',
  full_name='EnhanceEquipmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EnhanceEquipmentRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='EnhanceEquipmentRequest.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num', full_name='EnhanceEquipmentRequest.num', index=2,
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
  serialized_start=442,
  serialized_end=506,
)


_ENHANCEEQUIPMENTRESPONSE = _descriptor.Descriptor(
  name='EnhanceEquipmentResponse',
  full_name='EnhanceEquipmentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='EnhanceEquipmentResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='EnhanceEquipmentResponse.data', index=1,
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
  serialized_start=508,
  serialized_end=598,
)


_COMPOSEEQUIPMENTREQUEST = _descriptor.Descriptor(
  name='ComposeEquipmentRequest',
  full_name='ComposeEquipmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='no', full_name='ComposeEquipmentRequest.no', index=0,
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
  serialized_start=600,
  serialized_end=637,
)


_COMPOSEEQUIPMENTRESPONSE = _descriptor.Descriptor(
  name='ComposeEquipmentResponse',
  full_name='ComposeEquipmentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='ComposeEquipmentResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equ', full_name='ComposeEquipmentResponse.equ', index=1,
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
  serialized_start=639,
  serialized_end=722,
)


_NOBBINGEQUIPMENTREQUEST = _descriptor.Descriptor(
  name='NobbingEquipmentRequest',
  full_name='NobbingEquipmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='NobbingEquipmentRequest.id', index=0,
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
  serialized_start=724,
  serialized_end=761,
)


_NOBBINGEQUIPMENTRESPONSE = _descriptor.Descriptor(
  name='NobbingEquipmentResponse',
  full_name='NobbingEquipmentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='NobbingEquipmentResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equ', full_name='NobbingEquipmentResponse.equ', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cgr', full_name='NobbingEquipmentResponse.cgr', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=763,
  serialized_end=881,
)


_MELTINGEQUIPMENTREQUEST = _descriptor.Descriptor(
  name='MeltingEquipmentRequest',
  full_name='MeltingEquipmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MeltingEquipmentRequest.id', index=0,
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
  serialized_start=883,
  serialized_end=920,
)


_MELTINGEQUIPMENTRESPONSE = _descriptor.Descriptor(
  name='MeltingEquipmentResponse',
  full_name='MeltingEquipmentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='MeltingEquipmentResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cgr', full_name='MeltingEquipmentResponse.cgr', index=1,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=922,
  serialized_end=1013,
)

_EQUIPMENTPB.fields_by_name['set'].message_type = _SETEQUIPMENT
_GETEQUIPMENTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_GETEQUIPMENTRESPONSE.fields_by_name['equipment'].message_type = _EQUIPMENTPB
_ENHANCEEQUIPMENTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_ENHANCEEQUIPMENTRESPONSE.fields_by_name['data'].message_type = _ENHANCEDATAFORMAT
_COMPOSEEQUIPMENTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_COMPOSEEQUIPMENTRESPONSE.fields_by_name['equ'].message_type = _EQUIPMENTPB
_NOBBINGEQUIPMENTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_NOBBINGEQUIPMENTRESPONSE.fields_by_name['equ'].message_type = _EQUIPMENTPB
_NOBBINGEQUIPMENTRESPONSE.fields_by_name['cgr'].message_type = common_pb2._COMMONGAMERESOURCES
_MELTINGEQUIPMENTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_MELTINGEQUIPMENTRESPONSE.fields_by_name['cgr'].message_type = common_pb2._COMMONGAMERESOURCES
DESCRIPTOR.message_types_by_name['SetEquipment'] = _SETEQUIPMENT
DESCRIPTOR.message_types_by_name['EnhanceDataFormat'] = _ENHANCEDATAFORMAT
DESCRIPTOR.message_types_by_name['EquipmentPB'] = _EQUIPMENTPB
DESCRIPTOR.message_types_by_name['GetEquipmentsRequest'] = _GETEQUIPMENTSREQUEST
DESCRIPTOR.message_types_by_name['GetEquipmentResponse'] = _GETEQUIPMENTRESPONSE
DESCRIPTOR.message_types_by_name['EnhanceEquipmentRequest'] = _ENHANCEEQUIPMENTREQUEST
DESCRIPTOR.message_types_by_name['EnhanceEquipmentResponse'] = _ENHANCEEQUIPMENTRESPONSE
DESCRIPTOR.message_types_by_name['ComposeEquipmentRequest'] = _COMPOSEEQUIPMENTREQUEST
DESCRIPTOR.message_types_by_name['ComposeEquipmentResponse'] = _COMPOSEEQUIPMENTRESPONSE
DESCRIPTOR.message_types_by_name['NobbingEquipmentRequest'] = _NOBBINGEQUIPMENTREQUEST
DESCRIPTOR.message_types_by_name['NobbingEquipmentResponse'] = _NOBBINGEQUIPMENTRESPONSE
DESCRIPTOR.message_types_by_name['MeltingEquipmentRequest'] = _MELTINGEQUIPMENTREQUEST
DESCRIPTOR.message_types_by_name['MeltingEquipmentResponse'] = _MELTINGEQUIPMENTRESPONSE

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

class GetEquipmentsRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETEQUIPMENTSREQUEST

  # @@protoc_insertion_point(class_scope:GetEquipmentsRequest)

class GetEquipmentResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETEQUIPMENTRESPONSE

  # @@protoc_insertion_point(class_scope:GetEquipmentResponse)

class EnhanceEquipmentRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENHANCEEQUIPMENTREQUEST

  # @@protoc_insertion_point(class_scope:EnhanceEquipmentRequest)

class EnhanceEquipmentResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENHANCEEQUIPMENTRESPONSE

  # @@protoc_insertion_point(class_scope:EnhanceEquipmentResponse)

class ComposeEquipmentRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMPOSEEQUIPMENTREQUEST

  # @@protoc_insertion_point(class_scope:ComposeEquipmentRequest)

class ComposeEquipmentResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMPOSEEQUIPMENTRESPONSE

  # @@protoc_insertion_point(class_scope:ComposeEquipmentResponse)

class NobbingEquipmentRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NOBBINGEQUIPMENTREQUEST

  # @@protoc_insertion_point(class_scope:NobbingEquipmentRequest)

class NobbingEquipmentResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NOBBINGEQUIPMENTRESPONSE

  # @@protoc_insertion_point(class_scope:NobbingEquipmentResponse)

class MeltingEquipmentRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MELTINGEQUIPMENTREQUEST

  # @@protoc_insertion_point(class_scope:MeltingEquipmentRequest)

class MeltingEquipmentResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MELTINGEQUIPMENTRESPONSE

  # @@protoc_insertion_point(class_scope:MeltingEquipmentResponse)


# @@protoc_insertion_point(module_scope)
