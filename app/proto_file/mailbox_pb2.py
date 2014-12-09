# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mailbox.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mailbox.proto',
  package='',
  serialized_pb='\n\rmailbox.proto\x1a\x0c\x63ommon.proto\"\xe9\x01\n\x07Mail_PB\x12\x0f\n\x07mail_id\x18\x01 \x02(\t\x12\x11\n\tsender_id\x18\x02 \x01(\x05\x12\x13\n\x0bsender_name\x18\x03 \x01(\t\x12\x13\n\x0bsender_icon\x18\x04 \x01(\x05\x12\x12\n\nreceive_id\x18\x05 \x01(\x05\x12\x14\n\x0creceive_name\x18\x06 \x01(\t\x12\r\n\x05title\x18\x07 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x08 \x01(\t\x12\x11\n\tmail_type\x18\t \x02(\x05\x12\x11\n\tsend_time\x18\n \x01(\x05\x12\x11\n\tis_readed\x18\x0b \x01(\x08\x12\r\n\x05prize\x18\x0c \x01(\t\"H\n\x0cGetMailInfos\x12\x17\n\x05mails\x18\x01 \x03(\x0b\x32\x08.Mail_PB\x12\x0e\n\x06target\x18\x02 \x01(\x05\x12\x0f\n\x07\x63urrent\x18\x03 \x01(\x05\"6\n\x0fReadMailRequest\x12\x10\n\x08mail_ids\x18\x01 \x03(\t\x12\x11\n\tmail_type\x18\x02 \x01(\x05\"\x8a\x01\n\x10ReadMailResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12$\n\x04gain\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\x12\x0e\n\x06target\x18\x03 \x01(\x05\x12\x0f\n\x07\x63urrent\x18\x04 \x01(\x05\x12\x11\n\tmail_type\x18\x05 \x01(\x05\"$\n\x11\x44\x65leteMailRequest\x12\x0f\n\x07mail_id\x18\x01 \x03(\t\")\n\x0fSendMailRequest\x12\x16\n\x04mail\x18\x01 \x02(\x0b\x32\x08.Mail_PB\"-\n\x13ReceiveMailResponse\x12\x16\n\x04mail\x18\x01 \x02(\x0b\x32\x08.Mail_PB')




_MAIL_PB = _descriptor.Descriptor(
  name='Mail_PB',
  full_name='Mail_PB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail_id', full_name='Mail_PB.mail_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=32,
  serialized_end=265,
)


_GETMAILINFOS = _descriptor.Descriptor(
  name='GetMailInfos',
  full_name='GetMailInfos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mails', full_name='GetMailInfos.mails', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='GetMailInfos.target', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current', full_name='GetMailInfos.current', index=2,
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
  serialized_start=267,
  serialized_end=339,
)


_READMAILREQUEST = _descriptor.Descriptor(
  name='ReadMailRequest',
  full_name='ReadMailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail_ids', full_name='ReadMailRequest.mail_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mail_type', full_name='ReadMailRequest.mail_type', index=1,
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
  serialized_start=341,
  serialized_end=395,
)


_READMAILRESPONSE = _descriptor.Descriptor(
  name='ReadMailResponse',
  full_name='ReadMailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='ReadMailResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='ReadMailResponse.gain', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='ReadMailResponse.target', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current', full_name='ReadMailResponse.current', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mail_type', full_name='ReadMailResponse.mail_type', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=398,
  serialized_end=536,
)


_DELETEMAILREQUEST = _descriptor.Descriptor(
  name='DeleteMailRequest',
  full_name='DeleteMailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail_id', full_name='DeleteMailRequest.mail_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=538,
  serialized_end=574,
)


_SENDMAILREQUEST = _descriptor.Descriptor(
  name='SendMailRequest',
  full_name='SendMailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail', full_name='SendMailRequest.mail', index=0,
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
  serialized_start=576,
  serialized_end=617,
)


_RECEIVEMAILRESPONSE = _descriptor.Descriptor(
  name='ReceiveMailResponse',
  full_name='ReceiveMailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail', full_name='ReceiveMailResponse.mail', index=0,
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
  serialized_start=619,
  serialized_end=664,
)

_GETMAILINFOS.fields_by_name['mails'].message_type = _MAIL_PB
_READMAILRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_READMAILRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
_SENDMAILREQUEST.fields_by_name['mail'].message_type = _MAIL_PB
_RECEIVEMAILRESPONSE.fields_by_name['mail'].message_type = _MAIL_PB
DESCRIPTOR.message_types_by_name['Mail_PB'] = _MAIL_PB
DESCRIPTOR.message_types_by_name['GetMailInfos'] = _GETMAILINFOS
DESCRIPTOR.message_types_by_name['ReadMailRequest'] = _READMAILREQUEST
DESCRIPTOR.message_types_by_name['ReadMailResponse'] = _READMAILRESPONSE
DESCRIPTOR.message_types_by_name['DeleteMailRequest'] = _DELETEMAILREQUEST
DESCRIPTOR.message_types_by_name['SendMailRequest'] = _SENDMAILREQUEST
DESCRIPTOR.message_types_by_name['ReceiveMailResponse'] = _RECEIVEMAILRESPONSE

class Mail_PB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAIL_PB

  # @@protoc_insertion_point(class_scope:Mail_PB)

class GetMailInfos(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETMAILINFOS

  # @@protoc_insertion_point(class_scope:GetMailInfos)

class ReadMailRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _READMAILREQUEST

  # @@protoc_insertion_point(class_scope:ReadMailRequest)

class ReadMailResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _READMAILRESPONSE

  # @@protoc_insertion_point(class_scope:ReadMailResponse)

class DeleteMailRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DELETEMAILREQUEST

  # @@protoc_insertion_point(class_scope:DeleteMailRequest)

class SendMailRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SENDMAILREQUEST

  # @@protoc_insertion_point(class_scope:SendMailRequest)

class ReceiveMailResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECEIVEMAILRESPONSE

  # @@protoc_insertion_point(class_scope:ReceiveMailResponse)


# @@protoc_insertion_point(module_scope)
