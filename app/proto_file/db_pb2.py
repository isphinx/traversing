# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: db.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='db.proto',
  package='',
  serialized_pb='\n\x08\x64\x62.proto\"*\n\x08Heads_DB\x12\x0c\n\x04head\x18\x01 \x03(\x05\x12\x10\n\x08now_head\x18\x02 \x01(\x05\"\xdf\x03\n\x07Mail_PB\x12\x0f\n\x07mail_id\x18\x01 \x01(\t\x12\x11\n\tsender_id\x18\x02 \x01(\x05\x12\x13\n\x0bsender_name\x18\x03 \x01(\t\x12\x13\n\x0bsender_icon\x18\x04 \x01(\x05\x12\x12\n\nreceive_id\x18\x05 \x01(\x05\x12\x14\n\x0creceive_name\x18\x06 \x01(\t\x12\r\n\x05title\x18\x07 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x08 \x01(\t\x12\x11\n\tmail_type\x18\t \x02(\x05\x12\x11\n\tsend_time\x18\n \x01(\x05\x12\x11\n\tis_readed\x18\x0b \x01(\x08\x12\r\n\x05prize\x18\x0c \x01(\t\x12\x11\n\tread_time\x18\r \x01(\t\x12\x11\n\tconfig_id\x18\x0e \x01(\x05\x12\x10\n\x08nickname\x18\x0f \x01(\t\x12\x12\n\nguild_name\x18\x10 \x01(\x0c\x12\x18\n\x10guild_person_num\x18\x11 \x01(\x05\x12\x13\n\x0bguild_level\x18\x12 \x01(\x05\x12\x10\n\x08guild_id\x18\x13 \x01(\x05\x12\x10\n\x08rune_num\x18\x14 \x01(\x05\x12\x10\n\x08pvp_rank\x18\x15 \x01(\x05\x12\x10\n\x08integral\x18\x18 \x01(\x05\x12\x0c\n\x04rank\x18\x19 \x01(\x05\x12\r\n\x05\x65\x66\x66\x65\x63\x18\x16 \x01(\x05\x12\x14\n\x0cis_got_prize\x18\x17 \x01(\x08\"F\n\x10WorldBossAwardDB\x12\x12\n\naward_type\x18\x01 \x01(\x05\x12\r\n\x05\x61ward\x18\x02 \x01(\x05\x12\x0f\n\x07rank_no\x18\x03 \x01(\x05\"\xf0\x01\n\nStamina_DB\x12\x17\n\x0copen_receive\x18\x01 \x01(\x05:\x01\x31\x12\x1c\n\x11get_stamina_times\x18\x02 \x01(\x05:\x01\x30\x12\x1c\n\x11\x62uy_stamina_times\x18\x03 \x01(\x05:\x01\x30\x12!\n\x16last_gain_stamina_time\x18\x04 \x01(\x05:\x01\x30\x12\x18\n\rlast_mail_day\x18\x05 \x01(\x05:\x01\x30\x12\x14\n\x0c\x63ontributors\x18\x06 \x03(\x05\x12 \n\x15last_buy_stamina_time\x18\x07 \x01(\x05:\x01\x30\x12\x18\n\rresource_type\x18\x08 \x01(\x05:\x01\x30\".\n\x0e\x41ll_Stamina_DB\x12\x1c\n\x07stamina\x18\x01 \x03(\x0b\x32\x0b.Stamina_DB')




_HEADS_DB = _descriptor.Descriptor(
  name='Heads_DB',
  full_name='Heads_DB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='Heads_DB.head', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='now_head', full_name='Heads_DB.now_head', index=1,
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
  serialized_start=12,
  serialized_end=54,
)


_MAIL_PB = _descriptor.Descriptor(
  name='Mail_PB',
  full_name='Mail_PB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail_id', full_name='Mail_PB.mail_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender_id', full_name='Mail_PB.sender_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender_name', full_name='Mail_PB.sender_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender_icon', full_name='Mail_PB.sender_icon', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receive_id', full_name='Mail_PB.receive_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receive_name', full_name='Mail_PB.receive_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='Mail_PB.title', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='Mail_PB.content', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mail_type', full_name='Mail_PB.mail_type', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_time', full_name='Mail_PB.send_time', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_readed', full_name='Mail_PB.is_readed', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prize', full_name='Mail_PB.prize', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_time', full_name='Mail_PB.read_time', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config_id', full_name='Mail_PB.config_id', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='Mail_PB.nickname', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_name', full_name='Mail_PB.guild_name', index=15,
      number=16, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_person_num', full_name='Mail_PB.guild_person_num', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_level', full_name='Mail_PB.guild_level', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_id', full_name='Mail_PB.guild_id', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rune_num', full_name='Mail_PB.rune_num', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_rank', full_name='Mail_PB.pvp_rank', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='integral', full_name='Mail_PB.integral', index=21,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='Mail_PB.rank', index=22,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='effec', full_name='Mail_PB.effec', index=23,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_got_prize', full_name='Mail_PB.is_got_prize', index=24,
      number=23, type=8, cpp_type=7, label=1,
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
  serialized_start=57,
  serialized_end=536,
)


_WORLDBOSSAWARDDB = _descriptor.Descriptor(
  name='WorldBossAwardDB',
  full_name='WorldBossAwardDB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='award_type', full_name='WorldBossAwardDB.award_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='award', full_name='WorldBossAwardDB.award', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank_no', full_name='WorldBossAwardDB.rank_no', index=2,
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
  serialized_start=538,
  serialized_end=608,
)


_STAMINA_DB = _descriptor.Descriptor(
  name='Stamina_DB',
  full_name='Stamina_DB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='open_receive', full_name='Stamina_DB.open_receive', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_stamina_times', full_name='Stamina_DB.get_stamina_times', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buy_stamina_times', full_name='Stamina_DB.buy_stamina_times', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_gain_stamina_time', full_name='Stamina_DB.last_gain_stamina_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_mail_day', full_name='Stamina_DB.last_mail_day', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contributors', full_name='Stamina_DB.contributors', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_buy_stamina_time', full_name='Stamina_DB.last_buy_stamina_time', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='Stamina_DB.resource_type', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=611,
  serialized_end=851,
)


_ALL_STAMINA_DB = _descriptor.Descriptor(
  name='All_Stamina_DB',
  full_name='All_Stamina_DB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stamina', full_name='All_Stamina_DB.stamina', index=0,
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
  serialized_start=853,
  serialized_end=899,
)

_ALL_STAMINA_DB.fields_by_name['stamina'].message_type = _STAMINA_DB
DESCRIPTOR.message_types_by_name['Heads_DB'] = _HEADS_DB
DESCRIPTOR.message_types_by_name['Mail_PB'] = _MAIL_PB
DESCRIPTOR.message_types_by_name['WorldBossAwardDB'] = _WORLDBOSSAWARDDB
DESCRIPTOR.message_types_by_name['Stamina_DB'] = _STAMINA_DB
DESCRIPTOR.message_types_by_name['All_Stamina_DB'] = _ALL_STAMINA_DB

class Heads_DB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEADS_DB

  # @@protoc_insertion_point(class_scope:Heads_DB)

class Mail_PB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_PB

  # @@protoc_insertion_point(class_scope:Mail_PB)

class WorldBossAwardDB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLDBOSSAWARDDB

  # @@protoc_insertion_point(class_scope:WorldBossAwardDB)

class Stamina_DB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAMINA_DB

  # @@protoc_insertion_point(class_scope:Stamina_DB)

class All_Stamina_DB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ALL_STAMINA_DB

  # @@protoc_insertion_point(class_scope:All_Stamina_DB)


# @@protoc_insertion_point(module_scope)
