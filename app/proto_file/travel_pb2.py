# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: travel.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2
import travel_item_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='travel.proto',
  package='',
  serialized_pb='\n\x0ctravel.proto\x1a\x0c\x63ommon.proto\x1a\x11travel_item.proto\"4\n\x07\x43hapter\x12\x17\n\x06travel\x18\x01 \x03(\x0b\x32\x07.Travel\x12\x10\n\x08stage_id\x18\x02 \x02(\x05\"^\n\x06Travel\x12\x10\n\x08\x65vent_id\x18\x01 \x02(\x05\x12%\n\x05\x64rops\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\x12\x0c\n\x04time\x18\x03 \x01(\x05\x12\r\n\x05state\x18\x04 \x01(\x05\")\n\x05Shoes\x12\x0b\n\x03num\x18\x01 \x02(\x05\x12\x13\n\x0bremain_time\x18\x02 \x02(\x05\"!\n\rTravelRequest\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\"g\n\x0eTravelResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\x12%\n\x05\x64rops\x18\x03 \x01(\x0b\x32\x16.GameResourcesResponse\"\xe5\x01\n\x12TravelInitResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x19\n\x07\x63hapter\x18\x02 \x03(\x0b\x32\x08.Chapter\x12\x15\n\x05shoes\x18\x03 \x01(\x0b\x32\x06.Shoes\x12\x12\n\nchest_time\x18\x04 \x02(\x05\x12/\n\x13travel_item_chapter\x18\x05 \x03(\x0b\x32\x12.TravelItemChapter\x12\"\n\x0cstage_travel\x18\x06 \x03(\x0b\x32\x0c.StageTravel\x12\x16\n\x0e\x62uy_shoe_times\x18\x07 \x02(\x05\"G\n\x11TravelItemChapter\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\x12 \n\x0btravel_item\x18\x02 \x03(\x0b\x32\x0b.TravelItem\"\x1e\n\x0f\x42uyShoesRequest\x12\x0b\n\x03num\x18\x01 \x02(\x05\"0\n\x10\x42uyShoesResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\"L\n\x13TravelSettleRequest\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x02(\x05\x12\x11\n\tparameter\x18\x03 \x01(\x03\"[\n\x14TravelSettleResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12%\n\x05\x64rops\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\"7\n\x11\x45ventStartRequest\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x02(\x05\"@\n\x12\x45ventStartResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x0c\n\x04time\x18\x02 \x01(\x05\"3\n\rNoWaitRequest\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x02(\x05\"<\n\x0eNoWaitResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x0c\n\x04time\x18\x02 \x01(\x05\"X\n\x11OpenChestResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12%\n\x05\x64rops\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\"4\n\x11\x41utoTravelRequest\x12\r\n\x05ttime\x18\x01 \x02(\x05\x12\x10\n\x08stage_id\x18\x02 \x02(\x05\"V\n\x12\x41utoTravelResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\"\n\x0cstage_travel\x18\x02 \x03(\x0b\x32\x0c.StageTravel\"h\n\nAutoTravel\x12\x12\n\nstart_time\x18\x01 \x02(\x05\x12\x16\n\x0e\x63ontinued_time\x18\x02 \x02(\x05\x12\x17\n\x06travel\x18\x03 \x03(\x0b\x32\x07.Travel\x12\x15\n\ralready_times\x18\x04 \x02(\x05\"A\n\x0bStageTravel\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\x12 \n\x0b\x61uto_travel\x18\x02 \x03(\x0b\x32\x0b.AutoTravel\"`\n\x11SettleAutoRequest\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\x12\x12\n\nstart_time\x18\x02 \x02(\x05\x12\x10\n\x08\x65vent_id\x18\x03 \x02(\x05\x12\x13\n\x0bsettle_type\x18\x04 \x02(\x05\"V\n\x12SettleAutoResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\"\n\x0cstage_travel\x18\x02 \x03(\x0b\x32\x0c.StageTravel\"=\n\x15\x46\x61stFinishAutoRequest\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\x12\x12\n\nstart_time\x18\x02 \x02(\x05\"Z\n\x16\x46\x61stFinishAutoResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\"\n\x0cstage_travel\x18\x02 \x03(\x0b\x32\x0c.StageTravel')




_CHAPTER = _descriptor.Descriptor(
  name='Chapter',
  full_name='Chapter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='travel', full_name='Chapter.travel', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='Chapter.stage_id', index=1,
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
  serialized_start=49,
  serialized_end=101,
)


_TRAVEL = _descriptor.Descriptor(
  name='Travel',
  full_name='Travel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='Travel.event_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drops', full_name='Travel.drops', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='Travel.time', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='Travel.state', index=3,
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
  serialized_start=103,
  serialized_end=197,
)


_SHOES = _descriptor.Descriptor(
  name='Shoes',
  full_name='Shoes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='Shoes.num', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remain_time', full_name='Shoes.remain_time', index=1,
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
  serialized_start=199,
  serialized_end=240,
)


_TRAVELREQUEST = _descriptor.Descriptor(
  name='TravelRequest',
  full_name='TravelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='TravelRequest.stage_id', index=0,
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
  serialized_start=242,
  serialized_end=275,
)


_TRAVELRESPONSE = _descriptor.Descriptor(
  name='TravelResponse',
  full_name='TravelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='TravelResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='TravelResponse.event_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drops', full_name='TravelResponse.drops', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=277,
  serialized_end=380,
)


_TRAVELINITRESPONSE = _descriptor.Descriptor(
  name='TravelInitResponse',
  full_name='TravelInitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='TravelInitResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chapter', full_name='TravelInitResponse.chapter', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shoes', full_name='TravelInitResponse.shoes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chest_time', full_name='TravelInitResponse.chest_time', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='travel_item_chapter', full_name='TravelInitResponse.travel_item_chapter', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stage_travel', full_name='TravelInitResponse.stage_travel', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buy_shoe_times', full_name='TravelInitResponse.buy_shoe_times', index=6,
      number=7, type=5, cpp_type=1, label=2,
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
  serialized_start=383,
  serialized_end=612,
)


_TRAVELITEMCHAPTER = _descriptor.Descriptor(
  name='TravelItemChapter',
  full_name='TravelItemChapter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='TravelItemChapter.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='travel_item', full_name='TravelItemChapter.travel_item', index=1,
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
  serialized_start=614,
  serialized_end=685,
)


_BUYSHOESREQUEST = _descriptor.Descriptor(
  name='BuyShoesRequest',
  full_name='BuyShoesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='BuyShoesRequest.num', index=0,
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
  serialized_start=687,
  serialized_end=717,
)


_BUYSHOESRESPONSE = _descriptor.Descriptor(
  name='BuyShoesResponse',
  full_name='BuyShoesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='BuyShoesResponse.res', index=0,
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
  serialized_start=719,
  serialized_end=767,
)


_TRAVELSETTLEREQUEST = _descriptor.Descriptor(
  name='TravelSettleRequest',
  full_name='TravelSettleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='TravelSettleRequest.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='TravelSettleRequest.event_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='TravelSettleRequest.parameter', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=769,
  serialized_end=845,
)


_TRAVELSETTLERESPONSE = _descriptor.Descriptor(
  name='TravelSettleResponse',
  full_name='TravelSettleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='TravelSettleResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drops', full_name='TravelSettleResponse.drops', index=1,
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
  serialized_start=847,
  serialized_end=938,
)


_EVENTSTARTREQUEST = _descriptor.Descriptor(
  name='EventStartRequest',
  full_name='EventStartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='EventStartRequest.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='EventStartRequest.event_id', index=1,
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
  serialized_start=940,
  serialized_end=995,
)


_EVENTSTARTRESPONSE = _descriptor.Descriptor(
  name='EventStartResponse',
  full_name='EventStartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='EventStartResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='EventStartResponse.time', index=1,
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
  serialized_start=997,
  serialized_end=1061,
)


_NOWAITREQUEST = _descriptor.Descriptor(
  name='NoWaitRequest',
  full_name='NoWaitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='NoWaitRequest.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='NoWaitRequest.event_id', index=1,
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
  serialized_start=1063,
  serialized_end=1114,
)


_NOWAITRESPONSE = _descriptor.Descriptor(
  name='NoWaitResponse',
  full_name='NoWaitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='NoWaitResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='NoWaitResponse.time', index=1,
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
  serialized_start=1116,
  serialized_end=1176,
)


_OPENCHESTRESPONSE = _descriptor.Descriptor(
  name='OpenChestResponse',
  full_name='OpenChestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='OpenChestResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drops', full_name='OpenChestResponse.drops', index=1,
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
  serialized_start=1178,
  serialized_end=1266,
)


_AUTOTRAVELREQUEST = _descriptor.Descriptor(
  name='AutoTravelRequest',
  full_name='AutoTravelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ttime', full_name='AutoTravelRequest.ttime', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='AutoTravelRequest.stage_id', index=1,
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
  serialized_start=1268,
  serialized_end=1320,
)


_AUTOTRAVELRESPONSE = _descriptor.Descriptor(
  name='AutoTravelResponse',
  full_name='AutoTravelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='AutoTravelResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stage_travel', full_name='AutoTravelResponse.stage_travel', index=1,
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
  serialized_start=1322,
  serialized_end=1408,
)


_AUTOTRAVEL = _descriptor.Descriptor(
  name='AutoTravel',
  full_name='AutoTravel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='AutoTravel.start_time', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='continued_time', full_name='AutoTravel.continued_time', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='travel', full_name='AutoTravel.travel', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='already_times', full_name='AutoTravel.already_times', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=1410,
  serialized_end=1514,
)


_STAGETRAVEL = _descriptor.Descriptor(
  name='StageTravel',
  full_name='StageTravel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='StageTravel.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auto_travel', full_name='StageTravel.auto_travel', index=1,
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
  serialized_start=1516,
  serialized_end=1581,
)


_SETTLEAUTOREQUEST = _descriptor.Descriptor(
  name='SettleAutoRequest',
  full_name='SettleAutoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='SettleAutoRequest.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='SettleAutoRequest.start_time', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='SettleAutoRequest.event_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='settle_type', full_name='SettleAutoRequest.settle_type', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=1583,
  serialized_end=1679,
)


_SETTLEAUTORESPONSE = _descriptor.Descriptor(
  name='SettleAutoResponse',
  full_name='SettleAutoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='SettleAutoResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stage_travel', full_name='SettleAutoResponse.stage_travel', index=1,
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
  serialized_start=1681,
  serialized_end=1767,
)


_FASTFINISHAUTOREQUEST = _descriptor.Descriptor(
  name='FastFinishAutoRequest',
  full_name='FastFinishAutoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='FastFinishAutoRequest.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='FastFinishAutoRequest.start_time', index=1,
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
  serialized_start=1769,
  serialized_end=1830,
)


_FASTFINISHAUTORESPONSE = _descriptor.Descriptor(
  name='FastFinishAutoResponse',
  full_name='FastFinishAutoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='FastFinishAutoResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stage_travel', full_name='FastFinishAutoResponse.stage_travel', index=1,
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
  serialized_start=1832,
  serialized_end=1922,
)

_CHAPTER.fields_by_name['travel'].message_type = _TRAVEL
_TRAVEL.fields_by_name['drops'].message_type = common_pb2._GAMERESOURCESRESPONSE
_TRAVELRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_TRAVELRESPONSE.fields_by_name['drops'].message_type = common_pb2._GAMERESOURCESRESPONSE
_TRAVELINITRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_TRAVELINITRESPONSE.fields_by_name['chapter'].message_type = _CHAPTER
_TRAVELINITRESPONSE.fields_by_name['shoes'].message_type = _SHOES
_TRAVELINITRESPONSE.fields_by_name['travel_item_chapter'].message_type = _TRAVELITEMCHAPTER
_TRAVELINITRESPONSE.fields_by_name['stage_travel'].message_type = _STAGETRAVEL
_TRAVELITEMCHAPTER.fields_by_name['travel_item'].message_type = travel_item_pb2._TRAVELITEM
_BUYSHOESRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_TRAVELSETTLERESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_TRAVELSETTLERESPONSE.fields_by_name['drops'].message_type = common_pb2._GAMERESOURCESRESPONSE
_EVENTSTARTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_NOWAITRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_OPENCHESTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_OPENCHESTRESPONSE.fields_by_name['drops'].message_type = common_pb2._GAMERESOURCESRESPONSE
_AUTOTRAVELRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_AUTOTRAVELRESPONSE.fields_by_name['stage_travel'].message_type = _STAGETRAVEL
_AUTOTRAVEL.fields_by_name['travel'].message_type = _TRAVEL
_STAGETRAVEL.fields_by_name['auto_travel'].message_type = _AUTOTRAVEL
_SETTLEAUTORESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_SETTLEAUTORESPONSE.fields_by_name['stage_travel'].message_type = _STAGETRAVEL
_FASTFINISHAUTORESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_FASTFINISHAUTORESPONSE.fields_by_name['stage_travel'].message_type = _STAGETRAVEL
DESCRIPTOR.message_types_by_name['Chapter'] = _CHAPTER
DESCRIPTOR.message_types_by_name['Travel'] = _TRAVEL
DESCRIPTOR.message_types_by_name['Shoes'] = _SHOES
DESCRIPTOR.message_types_by_name['TravelRequest'] = _TRAVELREQUEST
DESCRIPTOR.message_types_by_name['TravelResponse'] = _TRAVELRESPONSE
DESCRIPTOR.message_types_by_name['TravelInitResponse'] = _TRAVELINITRESPONSE
DESCRIPTOR.message_types_by_name['TravelItemChapter'] = _TRAVELITEMCHAPTER
DESCRIPTOR.message_types_by_name['BuyShoesRequest'] = _BUYSHOESREQUEST
DESCRIPTOR.message_types_by_name['BuyShoesResponse'] = _BUYSHOESRESPONSE
DESCRIPTOR.message_types_by_name['TravelSettleRequest'] = _TRAVELSETTLEREQUEST
DESCRIPTOR.message_types_by_name['TravelSettleResponse'] = _TRAVELSETTLERESPONSE
DESCRIPTOR.message_types_by_name['EventStartRequest'] = _EVENTSTARTREQUEST
DESCRIPTOR.message_types_by_name['EventStartResponse'] = _EVENTSTARTRESPONSE
DESCRIPTOR.message_types_by_name['NoWaitRequest'] = _NOWAITREQUEST
DESCRIPTOR.message_types_by_name['NoWaitResponse'] = _NOWAITRESPONSE
DESCRIPTOR.message_types_by_name['OpenChestResponse'] = _OPENCHESTRESPONSE
DESCRIPTOR.message_types_by_name['AutoTravelRequest'] = _AUTOTRAVELREQUEST
DESCRIPTOR.message_types_by_name['AutoTravelResponse'] = _AUTOTRAVELRESPONSE
DESCRIPTOR.message_types_by_name['AutoTravel'] = _AUTOTRAVEL
DESCRIPTOR.message_types_by_name['StageTravel'] = _STAGETRAVEL
DESCRIPTOR.message_types_by_name['SettleAutoRequest'] = _SETTLEAUTOREQUEST
DESCRIPTOR.message_types_by_name['SettleAutoResponse'] = _SETTLEAUTORESPONSE
DESCRIPTOR.message_types_by_name['FastFinishAutoRequest'] = _FASTFINISHAUTOREQUEST
DESCRIPTOR.message_types_by_name['FastFinishAutoResponse'] = _FASTFINISHAUTORESPONSE

class Chapter(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHAPTER

  # @@protoc_insertion_point(class_scope:Chapter)

class Travel(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRAVEL

  # @@protoc_insertion_point(class_scope:Travel)

class Shoes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHOES

  # @@protoc_insertion_point(class_scope:Shoes)

class TravelRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRAVELREQUEST

  # @@protoc_insertion_point(class_scope:TravelRequest)

class TravelResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRAVELRESPONSE

  # @@protoc_insertion_point(class_scope:TravelResponse)

class TravelInitResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRAVELINITRESPONSE

  # @@protoc_insertion_point(class_scope:TravelInitResponse)

class TravelItemChapter(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRAVELITEMCHAPTER

  # @@protoc_insertion_point(class_scope:TravelItemChapter)

class BuyShoesRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUYSHOESREQUEST

  # @@protoc_insertion_point(class_scope:BuyShoesRequest)

class BuyShoesResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUYSHOESRESPONSE

  # @@protoc_insertion_point(class_scope:BuyShoesResponse)

class TravelSettleRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRAVELSETTLEREQUEST

  # @@protoc_insertion_point(class_scope:TravelSettleRequest)

class TravelSettleResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRAVELSETTLERESPONSE

  # @@protoc_insertion_point(class_scope:TravelSettleResponse)

class EventStartRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EVENTSTARTREQUEST

  # @@protoc_insertion_point(class_scope:EventStartRequest)

class EventStartResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EVENTSTARTRESPONSE

  # @@protoc_insertion_point(class_scope:EventStartResponse)

class NoWaitRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NOWAITREQUEST

  # @@protoc_insertion_point(class_scope:NoWaitRequest)

class NoWaitResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NOWAITRESPONSE

  # @@protoc_insertion_point(class_scope:NoWaitResponse)

class OpenChestResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPENCHESTRESPONSE

  # @@protoc_insertion_point(class_scope:OpenChestResponse)

class AutoTravelRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTOTRAVELREQUEST

  # @@protoc_insertion_point(class_scope:AutoTravelRequest)

class AutoTravelResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTOTRAVELRESPONSE

  # @@protoc_insertion_point(class_scope:AutoTravelResponse)

class AutoTravel(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTOTRAVEL

  # @@protoc_insertion_point(class_scope:AutoTravel)

class StageTravel(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAGETRAVEL

  # @@protoc_insertion_point(class_scope:StageTravel)

class SettleAutoRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SETTLEAUTOREQUEST

  # @@protoc_insertion_point(class_scope:SettleAutoRequest)

class SettleAutoResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SETTLEAUTORESPONSE

  # @@protoc_insertion_point(class_scope:SettleAutoResponse)

class FastFinishAutoRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FASTFINISHAUTOREQUEST

  # @@protoc_insertion_point(class_scope:FastFinishAutoRequest)

class FastFinishAutoResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FASTFINISHAUTORESPONSE

  # @@protoc_insertion_point(class_scope:FastFinishAutoResponse)


# @@protoc_insertion_point(module_scope)
