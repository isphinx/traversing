# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pvp_rank.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import stage_pb2
import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pvp_rank.proto',
  package='',
  serialized_pb='\n\x0epvp_rank.proto\x1a\x0bstage.proto\x1a\x0c\x63ommon.proto\"\x94\x01\n\tRankItems\x12\x10\n\x08nickname\x18\x01 \x02(\t\x12\x0c\n\x04rank\x18\x02 \x02(\x05\x12\r\n\x05level\x18\x03 \x02(\x05\x12\n\n\x02\x61p\x18\x04 \x02(\x05\x12\x10\n\x08hero_ids\x18\x05 \x03(\x05\x12\x13\n\x0bhero_levels\x18\x06 \x03(\x05\x12\x0f\n\x07head_no\x18\x07 \x02(\x05\x12\x14\n\x0c\x63haracter_id\x18\x08 \x02(\x05\"\\\n\x12PlayerRankResponse\x12\x1e\n\nrank_items\x18\x01 \x03(\x0b\x32\n.RankItems\x12\x13\n\x0bplayer_rank\x18\x02 \x01(\x05\x12\x11\n\tpvp_score\x18\x03 \x01(\x05\"H\n\x0fPvpFightRequest\x12\x16\n\x0e\x63hallenge_rank\x18\x01 \x02(\x05\x12\x0e\n\x06lineup\x18\x02 \x03(\x05\x12\r\n\x05skill\x18\x03 \x01(\x05\"B\n\x0fPvpFightRevenge\x12\x10\n\x08\x62lack_id\x18\x01 \x02(\x05\x12\x0e\n\x06lineup\x18\x02 \x03(\x05\x12\r\n\x05skill\x18\x03 \x01(\x05\"U\n\x10PvpFightOvercome\x12\x14\n\x0c\x63haracter_id\x18\x01 \x02(\x05\x12\x0c\n\x04type\x18\x02 \x02(\x05\x12\x0e\n\x06lineup\x18\x03 \x03(\x05\x12\r\n\x05skill\x18\x04 \x01(\x05\"+\n\x14PvpPlayerInfoRequest\x12\x13\n\x0bplayer_rank\x18\x01 \x02(\x05\"\x1d\n\x0cResetPvpTime\x12\r\n\x05times\x18\x01 \x02(\x05\"\xe5\x02\n\x10PvpFightResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x18\n\x03red\x18\x02 \x03(\x0b\x32\x0b.BattleUnit\x12\x19\n\x04\x62lue\x18\x03 \x03(\x0b\x32\x0b.BattleUnit\x12\x11\n\tred_skill\x18\x04 \x01(\x05\x12\x17\n\x0fred_skill_level\x18\x05 \x01(\x05\x12\x12\n\nblue_skill\x18\x06 \x01(\x05\x12\x18\n\x10\x62lue_skill_level\x18\x07 \x01(\x05\x12\x14\n\x0c\x66ight_result\x18\x08 \x01(\x08\x12\r\n\x05seed1\x18\t \x01(\x05\x12\r\n\x05seed2\x18\n \x01(\x05\x12$\n\x04gain\x18\x0b \x01(\x0b\x32\x16.GameResourcesResponse\x12\x10\n\x08top_rank\x18\x0c \x01(\x05\x12%\n\x05\x61ward\x18\r \x01(\x0b\x32\x16.GameResourcesResponse\x12\x11\n\trank_incr\x18\x0e \x01(\x05')




_RANKITEMS = _descriptor.Descriptor(
  name='RankItems',
  full_name='RankItems',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nickname', full_name='RankItems.nickname', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='RankItems.rank', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='RankItems.level', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ap', full_name='RankItems.ap', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_ids', full_name='RankItems.hero_ids', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_levels', full_name='RankItems.hero_levels', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='head_no', full_name='RankItems.head_no', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='character_id', full_name='RankItems.character_id', index=7,
      number=8, type=5, cpp_type=1, label=2,
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
  serialized_start=46,
  serialized_end=194,
)


_PLAYERRANKRESPONSE = _descriptor.Descriptor(
  name='PlayerRankResponse',
  full_name='PlayerRankResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rank_items', full_name='PlayerRankResponse.rank_items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_rank', full_name='PlayerRankResponse.player_rank', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_score', full_name='PlayerRankResponse.pvp_score', index=2,
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
  serialized_start=196,
  serialized_end=288,
)


_PVPFIGHTREQUEST = _descriptor.Descriptor(
  name='PvpFightRequest',
  full_name='PvpFightRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge_rank', full_name='PvpFightRequest.challenge_rank', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lineup', full_name='PvpFightRequest.lineup', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skill', full_name='PvpFightRequest.skill', index=2,
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
  serialized_start=290,
  serialized_end=362,
)


_PVPFIGHTREVENGE = _descriptor.Descriptor(
  name='PvpFightRevenge',
  full_name='PvpFightRevenge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='black_id', full_name='PvpFightRevenge.black_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lineup', full_name='PvpFightRevenge.lineup', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skill', full_name='PvpFightRevenge.skill', index=2,
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
  serialized_start=364,
  serialized_end=430,
)


_PVPFIGHTOVERCOME = _descriptor.Descriptor(
  name='PvpFightOvercome',
  full_name='PvpFightOvercome',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='character_id', full_name='PvpFightOvercome.character_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='PvpFightOvercome.type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lineup', full_name='PvpFightOvercome.lineup', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skill', full_name='PvpFightOvercome.skill', index=3,
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
  serialized_start=432,
  serialized_end=517,
)


_PVPPLAYERINFOREQUEST = _descriptor.Descriptor(
  name='PvpPlayerInfoRequest',
  full_name='PvpPlayerInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_rank', full_name='PvpPlayerInfoRequest.player_rank', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=519,
  serialized_end=562,
)


_RESETPVPTIME = _descriptor.Descriptor(
  name='ResetPvpTime',
  full_name='ResetPvpTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='times', full_name='ResetPvpTime.times', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=564,
  serialized_end=593,
)


_PVPFIGHTRESPONSE = _descriptor.Descriptor(
  name='PvpFightResponse',
  full_name='PvpFightResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='PvpFightResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='red', full_name='PvpFightResponse.red', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blue', full_name='PvpFightResponse.blue', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='red_skill', full_name='PvpFightResponse.red_skill', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='red_skill_level', full_name='PvpFightResponse.red_skill_level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blue_skill', full_name='PvpFightResponse.blue_skill', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blue_skill_level', full_name='PvpFightResponse.blue_skill_level', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fight_result', full_name='PvpFightResponse.fight_result', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed1', full_name='PvpFightResponse.seed1', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed2', full_name='PvpFightResponse.seed2', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='PvpFightResponse.gain', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='top_rank', full_name='PvpFightResponse.top_rank', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='award', full_name='PvpFightResponse.award', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank_incr', full_name='PvpFightResponse.rank_incr', index=13,
      number=14, type=5, cpp_type=1, label=1,
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
  serialized_start=596,
  serialized_end=953,
)

_PLAYERRANKRESPONSE.fields_by_name['rank_items'].message_type = _RANKITEMS
_PVPFIGHTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_PVPFIGHTRESPONSE.fields_by_name['red'].message_type = stage_pb2._BATTLEUNIT
_PVPFIGHTRESPONSE.fields_by_name['blue'].message_type = stage_pb2._BATTLEUNIT
_PVPFIGHTRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
_PVPFIGHTRESPONSE.fields_by_name['award'].message_type = common_pb2._GAMERESOURCESRESPONSE
DESCRIPTOR.message_types_by_name['RankItems'] = _RANKITEMS
DESCRIPTOR.message_types_by_name['PlayerRankResponse'] = _PLAYERRANKRESPONSE
DESCRIPTOR.message_types_by_name['PvpFightRequest'] = _PVPFIGHTREQUEST
DESCRIPTOR.message_types_by_name['PvpFightRevenge'] = _PVPFIGHTREVENGE
DESCRIPTOR.message_types_by_name['PvpFightOvercome'] = _PVPFIGHTOVERCOME
DESCRIPTOR.message_types_by_name['PvpPlayerInfoRequest'] = _PVPPLAYERINFOREQUEST
DESCRIPTOR.message_types_by_name['ResetPvpTime'] = _RESETPVPTIME
DESCRIPTOR.message_types_by_name['PvpFightResponse'] = _PVPFIGHTRESPONSE

class RankItems(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RANKITEMS

  # @@protoc_insertion_point(class_scope:RankItems)

class PlayerRankResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PLAYERRANKRESPONSE

  # @@protoc_insertion_point(class_scope:PlayerRankResponse)

class PvpFightRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PVPFIGHTREQUEST

  # @@protoc_insertion_point(class_scope:PvpFightRequest)

class PvpFightRevenge(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PVPFIGHTREVENGE

  # @@protoc_insertion_point(class_scope:PvpFightRevenge)

class PvpFightOvercome(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PVPFIGHTOVERCOME

  # @@protoc_insertion_point(class_scope:PvpFightOvercome)

class PvpPlayerInfoRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PVPPLAYERINFOREQUEST

  # @@protoc_insertion_point(class_scope:PvpPlayerInfoRequest)

class ResetPvpTime(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESETPVPTIME

  # @@protoc_insertion_point(class_scope:ResetPvpTime)

class PvpFightResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PVPFIGHTRESPONSE

  # @@protoc_insertion_point(class_scope:PvpFightResponse)


# @@protoc_insertion_point(module_scope)
