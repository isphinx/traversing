# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: world_boss.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2
import stage_pb2
import line_up_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='world_boss.proto',
  package='',
  serialized_pb='\n\x10world_boss.proto\x1a\x0c\x63ommon.proto\x1a\x0bstage.proto\x1a\rline_up.proto\"\x1d\n\nPvbRequest\x12\x0f\n\x07\x62oss_id\x18\x01 \x02(\t\"\x9e\x01\n\x0bPvbRankItem\x12\x10\n\x08nickname\x18\x01 \x02(\t\x12\r\n\x05level\x18\x02 \x02(\x05\x12\x10\n\x08now_head\x18\x03 \x02(\x05\x12\x11\n\tdemage_hp\x18\x04 \x02(\x05\x12%\n\x0cline_up_info\x18\x05 \x01(\x0b\x32\x0f.LineUpResponse\x12\x11\n\tplayer_id\x18\x06 \x01(\x05\x12\x0f\n\x07rank_no\x18\x07 \x01(\x05\"O\n\rLuckyHeroAttr\x12\x11\n\tattr_type\x18\x01 \x02(\x05\x12\x17\n\x0f\x61ttr_value_type\x18\x02 \x02(\x05\x12\x12\n\nattr_value\x18\x03 \x02(\x02\"K\n\rLuckyHeroItem\x12\x0b\n\x03pos\x18\x01 \x02(\x05\x12\x0f\n\x07hero_no\x18\x02 \x02(\x05\x12\x1c\n\x04\x61ttr\x18\x03 \x03(\x0b\x32\x0e.LuckyHeroAttr\"\x8a\x03\n\x15PvbBeforeInfoResponse\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\x12#\n\x0blucky_heros\x18\x02 \x03(\x0b\x32\x0e.LuckyHeroItem\x12\x17\n\x0f\x64\x65\x62uff_skill_no\x18\x05 \x01(\x05\x12 \n\nrank_items\x18\x06 \x03(\x0b\x32\x0c.PvbRankItem\x12$\n\x0elast_shot_item\x18\x07 \x01(\x0b\x32\x0c.PvbRankItem\x12\x13\n\x0bopen_or_not\x18\x08 \x01(\x08\x12\x0f\n\x07hp_left\x18\t \x01(\x05\x12\x11\n\tdemage_hp\x18\n \x01(\x05\x12\x0f\n\x07rank_no\x18\x0b \x01(\x05\x12\x13\n\x0b\x66ight_times\x18\x0c \x01(\x05\x12\x17\n\x0flast_fight_time\x18\r \x01(\x05\x12\x1a\n\x12\x65ncourage_coin_num\x18\x0e \x01(\x05\x12\x1a\n\x12\x65ncourage_gold_num\x18\x0f \x01(\x05\x12\x19\n\x11gold_reborn_times\x18\x10 \x01(\x05\x12\x0e\n\x06hp_max\x18\x11 \x01(\x05\"8\n\x14PvbPlayerInfoRequest\x12\x0f\n\x07rank_no\x18\x01 \x02(\x05\x12\x0f\n\x07\x62oss_id\x18\x02 \x01(\t\"S\n\x15\x45ncourageHerosRequest\x12\x14\n\x0c\x66inance_type\x18\x01 \x02(\x05\x12\x13\n\x0b\x66inance_num\x18\x02 \x02(\x05\x12\x0f\n\x07\x62oss_id\x18\x03 \x01(\t\"U\n\x0fPvbStartRequest\x12\x0f\n\x07\x62oss_id\x18\x04 \x01(\t\x12\x0e\n\x06lineup\x18\x01 \x03(\x05\x12\x14\n\x0cunparalleled\x18\x02 \x01(\x05\x12\x0b\n\x03\x66id\x18\x03 \x01(\x05\"\xcf\x01\n\x10PvbFightResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x18\n\x03red\x18\x02 \x03(\x0b\x32\x0b.BattleUnit\x12\x19\n\x04\x62lue\x18\x03 \x03(\x0b\x32\x0b.BattleUnit\x12\x16\n\x0ered_best_skill\x18\x04 \x01(\x05\x12\x1c\n\x14red_best_skill_level\x18\x05 \x01(\x05\x12\x14\n\x0c\x66ight_result\x18\x06 \x01(\x08\x12\r\n\x05seed1\x18\x07 \x01(\x05\x12\r\n\x05seed2\x18\x08 \x01(\x05\"S\n\x10MineBossResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x0f\n\x07\x62oss_id\x18\x02 \x02(\t\x12\x10\n\x08stage_id\x18\x03 \x02(\x05\"n\n\x10PvbAwardResponse\x12\x0f\n\x07is_over\x18\x01 \x02(\x08\x12\x12\n\naward_type\x18\x02 \x01(\x05\x12$\n\x04gain\x18\x03 \x01(\x0b\x32\x16.GameResourcesResponse\x12\x0f\n\x07rank_no\x18\x04 \x01(\x05')




_PVBREQUEST = _descriptor.Descriptor(
  name='PvbRequest',
  full_name='PvbRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boss_id', full_name='PvbRequest.boss_id', index=0,
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
  serialized_start=62,
  serialized_end=91,
)


_PVBRANKITEM = _descriptor.Descriptor(
  name='PvbRankItem',
  full_name='PvbRankItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nickname', full_name='PvbRankItem.nickname', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='PvbRankItem.level', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='now_head', full_name='PvbRankItem.now_head', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demage_hp', full_name='PvbRankItem.demage_hp', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_up_info', full_name='PvbRankItem.line_up_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='PvbRankItem.player_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank_no', full_name='PvbRankItem.rank_no', index=6,
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
  serialized_start=94,
  serialized_end=252,
)


_LUCKYHEROATTR = _descriptor.Descriptor(
  name='LuckyHeroAttr',
  full_name='LuckyHeroAttr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attr_type', full_name='LuckyHeroAttr.attr_type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attr_value_type', full_name='LuckyHeroAttr.attr_value_type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attr_value', full_name='LuckyHeroAttr.attr_value', index=2,
      number=3, type=2, cpp_type=6, label=2,
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
  serialized_start=254,
  serialized_end=333,
)


_LUCKYHEROITEM = _descriptor.Descriptor(
  name='LuckyHeroItem',
  full_name='LuckyHeroItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos', full_name='LuckyHeroItem.pos', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_no', full_name='LuckyHeroItem.hero_no', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attr', full_name='LuckyHeroItem.attr', index=2,
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
  serialized_start=335,
  serialized_end=410,
)


_PVBBEFOREINFORESPONSE = _descriptor.Descriptor(
  name='PvbBeforeInfoResponse',
  full_name='PvbBeforeInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='PvbBeforeInfoResponse.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lucky_heros', full_name='PvbBeforeInfoResponse.lucky_heros', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debuff_skill_no', full_name='PvbBeforeInfoResponse.debuff_skill_no', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank_items', full_name='PvbBeforeInfoResponse.rank_items', index=3,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_shot_item', full_name='PvbBeforeInfoResponse.last_shot_item', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_or_not', full_name='PvbBeforeInfoResponse.open_or_not', index=5,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hp_left', full_name='PvbBeforeInfoResponse.hp_left', index=6,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demage_hp', full_name='PvbBeforeInfoResponse.demage_hp', index=7,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank_no', full_name='PvbBeforeInfoResponse.rank_no', index=8,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fight_times', full_name='PvbBeforeInfoResponse.fight_times', index=9,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_fight_time', full_name='PvbBeforeInfoResponse.last_fight_time', index=10,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encourage_coin_num', full_name='PvbBeforeInfoResponse.encourage_coin_num', index=11,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encourage_gold_num', full_name='PvbBeforeInfoResponse.encourage_gold_num', index=12,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold_reborn_times', full_name='PvbBeforeInfoResponse.gold_reborn_times', index=13,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hp_max', full_name='PvbBeforeInfoResponse.hp_max', index=14,
      number=17, type=5, cpp_type=1, label=1,
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
  serialized_start=413,
  serialized_end=807,
)


_PVBPLAYERINFOREQUEST = _descriptor.Descriptor(
  name='PvbPlayerInfoRequest',
  full_name='PvbPlayerInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rank_no', full_name='PvbPlayerInfoRequest.rank_no', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boss_id', full_name='PvbPlayerInfoRequest.boss_id', index=1,
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
  serialized_start=809,
  serialized_end=865,
)


_ENCOURAGEHEROSREQUEST = _descriptor.Descriptor(
  name='EncourageHerosRequest',
  full_name='EncourageHerosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='finance_type', full_name='EncourageHerosRequest.finance_type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finance_num', full_name='EncourageHerosRequest.finance_num', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boss_id', full_name='EncourageHerosRequest.boss_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=867,
  serialized_end=950,
)


_PVBSTARTREQUEST = _descriptor.Descriptor(
  name='PvbStartRequest',
  full_name='PvbStartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boss_id', full_name='PvbStartRequest.boss_id', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lineup', full_name='PvbStartRequest.lineup', index=1,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unparalleled', full_name='PvbStartRequest.unparalleled', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fid', full_name='PvbStartRequest.fid', index=3,
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
  serialized_start=952,
  serialized_end=1037,
)


_PVBFIGHTRESPONSE = _descriptor.Descriptor(
  name='PvbFightResponse',
  full_name='PvbFightResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='PvbFightResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='red', full_name='PvbFightResponse.red', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blue', full_name='PvbFightResponse.blue', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='red_best_skill', full_name='PvbFightResponse.red_best_skill', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='red_best_skill_level', full_name='PvbFightResponse.red_best_skill_level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fight_result', full_name='PvbFightResponse.fight_result', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed1', full_name='PvbFightResponse.seed1', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed2', full_name='PvbFightResponse.seed2', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=1040,
  serialized_end=1247,
)


_MINEBOSSRESPONSE = _descriptor.Descriptor(
  name='MineBossResponse',
  full_name='MineBossResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='MineBossResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boss_id', full_name='MineBossResponse.boss_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='MineBossResponse.stage_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=1249,
  serialized_end=1332,
)


_PVBAWARDRESPONSE = _descriptor.Descriptor(
  name='PvbAwardResponse',
  full_name='PvbAwardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_over', full_name='PvbAwardResponse.is_over', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='award_type', full_name='PvbAwardResponse.award_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='PvbAwardResponse.gain', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank_no', full_name='PvbAwardResponse.rank_no', index=3,
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
  serialized_start=1334,
  serialized_end=1444,
)

_PVBRANKITEM.fields_by_name['line_up_info'].message_type = line_up_pb2._LINEUPRESPONSE
_LUCKYHEROITEM.fields_by_name['attr'].message_type = _LUCKYHEROATTR
_PVBBEFOREINFORESPONSE.fields_by_name['lucky_heros'].message_type = _LUCKYHEROITEM
_PVBBEFOREINFORESPONSE.fields_by_name['rank_items'].message_type = _PVBRANKITEM
_PVBBEFOREINFORESPONSE.fields_by_name['last_shot_item'].message_type = _PVBRANKITEM
_PVBFIGHTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_PVBFIGHTRESPONSE.fields_by_name['red'].message_type = stage_pb2._BATTLEUNIT
_PVBFIGHTRESPONSE.fields_by_name['blue'].message_type = stage_pb2._BATTLEUNIT
_MINEBOSSRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_PVBAWARDRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
DESCRIPTOR.message_types_by_name['PvbRequest'] = _PVBREQUEST
DESCRIPTOR.message_types_by_name['PvbRankItem'] = _PVBRANKITEM
DESCRIPTOR.message_types_by_name['LuckyHeroAttr'] = _LUCKYHEROATTR
DESCRIPTOR.message_types_by_name['LuckyHeroItem'] = _LUCKYHEROITEM
DESCRIPTOR.message_types_by_name['PvbBeforeInfoResponse'] = _PVBBEFOREINFORESPONSE
DESCRIPTOR.message_types_by_name['PvbPlayerInfoRequest'] = _PVBPLAYERINFOREQUEST
DESCRIPTOR.message_types_by_name['EncourageHerosRequest'] = _ENCOURAGEHEROSREQUEST
DESCRIPTOR.message_types_by_name['PvbStartRequest'] = _PVBSTARTREQUEST
DESCRIPTOR.message_types_by_name['PvbFightResponse'] = _PVBFIGHTRESPONSE
DESCRIPTOR.message_types_by_name['MineBossResponse'] = _MINEBOSSRESPONSE
DESCRIPTOR.message_types_by_name['PvbAwardResponse'] = _PVBAWARDRESPONSE

class PvbRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PVBREQUEST

  # @@protoc_insertion_point(class_scope:PvbRequest)

class PvbRankItem(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PVBRANKITEM

  # @@protoc_insertion_point(class_scope:PvbRankItem)

class LuckyHeroAttr(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LUCKYHEROATTR

  # @@protoc_insertion_point(class_scope:LuckyHeroAttr)

class LuckyHeroItem(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LUCKYHEROITEM

  # @@protoc_insertion_point(class_scope:LuckyHeroItem)

class PvbBeforeInfoResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PVBBEFOREINFORESPONSE

  # @@protoc_insertion_point(class_scope:PvbBeforeInfoResponse)

class PvbPlayerInfoRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PVBPLAYERINFOREQUEST

  # @@protoc_insertion_point(class_scope:PvbPlayerInfoRequest)

class EncourageHerosRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENCOURAGEHEROSREQUEST

  # @@protoc_insertion_point(class_scope:EncourageHerosRequest)

class PvbStartRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PVBSTARTREQUEST

  # @@protoc_insertion_point(class_scope:PvbStartRequest)

class PvbFightResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PVBFIGHTRESPONSE

  # @@protoc_insertion_point(class_scope:PvbFightResponse)

class MineBossResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MINEBOSSRESPONSE

  # @@protoc_insertion_point(class_scope:MineBossResponse)

class PvbAwardResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PVBAWARDRESPONSE

  # @@protoc_insertion_point(class_scope:PvbAwardResponse)


# @@protoc_insertion_point(module_scope)
