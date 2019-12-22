# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mensajeria.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mensajeria.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\242\002\004AUTH'),
  serialized_pb=_b('\n\x10mensajeria.proto\"6\n\x07newUser\x12\x0b\n\x03tkn\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"#\n\x0fresponseNewUser\x12\x10\n\x08response\x18\x01 \x01(\t\"2\n\tmsgToUser\x12\x14\n\x0cnameReceptor\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1f\n\x0bmsgFromUser\x12\x10\n\x08response\x18\x01 \x01(\t\"\x1f\n\x06ToUser\x12\x15\n\rreceptor_name\x18\x01 \x01(\t\"\"\n\x0eToUserResponse\x12\x10\n\x08response\x18\x01 \x01(\t\"\x1e\n\x0brequestList\x12\x0f\n\x07request\x18\x01 \x01(\t\"\x1c\n\x0cresponseList\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\rrequestAllMsg\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\x0eresponseAllMsg\x12\x0f\n\x07message\x18\x01 \x01(\t2\xf7\x01\n\nMensajeria\x12*\n\nCreateUser\x12\x08.newUser\x1a\x10.responseNewUser\"\x00\x12+\n\tMsgToUser\x12\n.msgToUser\x1a\x0c.msgFromUser\"\x00(\x01\x30\x01\x12,\n\x0e\x43hangeReceptor\x12\x07.ToUser\x1a\x0f.ToUserResponse\"\x00\x12-\n\nObtainList\x12\x0c.requestList\x1a\r.responseList\"\x00\x30\x01\x12\x33\n\x0cObtainAllMsg\x12\x0e.requestAllMsg\x1a\x0f.responseAllMsg\"\x00\x30\x01\x42\x07\xa2\x02\x04\x41UTHb\x06proto3')
)




_NEWUSER = _descriptor.Descriptor(
  name='newUser',
  full_name='newUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tkn', full_name='newUser.tkn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='newUser.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='newUser.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=74,
)


_RESPONSENEWUSER = _descriptor.Descriptor(
  name='responseNewUser',
  full_name='responseNewUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='responseNewUser.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=111,
)


_MSGTOUSER = _descriptor.Descriptor(
  name='msgToUser',
  full_name='msgToUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nameReceptor', full_name='msgToUser.nameReceptor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='msgToUser.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=163,
)


_MSGFROMUSER = _descriptor.Descriptor(
  name='msgFromUser',
  full_name='msgFromUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='msgFromUser.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=196,
)


_TOUSER = _descriptor.Descriptor(
  name='ToUser',
  full_name='ToUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='receptor_name', full_name='ToUser.receptor_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=229,
)


_TOUSERRESPONSE = _descriptor.Descriptor(
  name='ToUserResponse',
  full_name='ToUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='ToUserResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=265,
)


_REQUESTLIST = _descriptor.Descriptor(
  name='requestList',
  full_name='requestList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='requestList.request', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=267,
  serialized_end=297,
)


_RESPONSELIST = _descriptor.Descriptor(
  name='responseList',
  full_name='responseList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='responseList.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=327,
)


_REQUESTALLMSG = _descriptor.Descriptor(
  name='requestAllMsg',
  full_name='requestAllMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='requestAllMsg.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=358,
)


_RESPONSEALLMSG = _descriptor.Descriptor(
  name='responseAllMsg',
  full_name='responseAllMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='responseAllMsg.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=360,
  serialized_end=393,
)

DESCRIPTOR.message_types_by_name['newUser'] = _NEWUSER
DESCRIPTOR.message_types_by_name['responseNewUser'] = _RESPONSENEWUSER
DESCRIPTOR.message_types_by_name['msgToUser'] = _MSGTOUSER
DESCRIPTOR.message_types_by_name['msgFromUser'] = _MSGFROMUSER
DESCRIPTOR.message_types_by_name['ToUser'] = _TOUSER
DESCRIPTOR.message_types_by_name['ToUserResponse'] = _TOUSERRESPONSE
DESCRIPTOR.message_types_by_name['requestList'] = _REQUESTLIST
DESCRIPTOR.message_types_by_name['responseList'] = _RESPONSELIST
DESCRIPTOR.message_types_by_name['requestAllMsg'] = _REQUESTALLMSG
DESCRIPTOR.message_types_by_name['responseAllMsg'] = _RESPONSEALLMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

newUser = _reflection.GeneratedProtocolMessageType('newUser', (_message.Message,), {
  'DESCRIPTOR' : _NEWUSER,
  '__module__' : 'mensajeria_pb2'
  # @@protoc_insertion_point(class_scope:newUser)
  })
_sym_db.RegisterMessage(newUser)

responseNewUser = _reflection.GeneratedProtocolMessageType('responseNewUser', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSENEWUSER,
  '__module__' : 'mensajeria_pb2'
  # @@protoc_insertion_point(class_scope:responseNewUser)
  })
_sym_db.RegisterMessage(responseNewUser)

msgToUser = _reflection.GeneratedProtocolMessageType('msgToUser', (_message.Message,), {
  'DESCRIPTOR' : _MSGTOUSER,
  '__module__' : 'mensajeria_pb2'
  # @@protoc_insertion_point(class_scope:msgToUser)
  })
_sym_db.RegisterMessage(msgToUser)

msgFromUser = _reflection.GeneratedProtocolMessageType('msgFromUser', (_message.Message,), {
  'DESCRIPTOR' : _MSGFROMUSER,
  '__module__' : 'mensajeria_pb2'
  # @@protoc_insertion_point(class_scope:msgFromUser)
  })
_sym_db.RegisterMessage(msgFromUser)

ToUser = _reflection.GeneratedProtocolMessageType('ToUser', (_message.Message,), {
  'DESCRIPTOR' : _TOUSER,
  '__module__' : 'mensajeria_pb2'
  # @@protoc_insertion_point(class_scope:ToUser)
  })
_sym_db.RegisterMessage(ToUser)

ToUserResponse = _reflection.GeneratedProtocolMessageType('ToUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOUSERRESPONSE,
  '__module__' : 'mensajeria_pb2'
  # @@protoc_insertion_point(class_scope:ToUserResponse)
  })
_sym_db.RegisterMessage(ToUserResponse)

requestList = _reflection.GeneratedProtocolMessageType('requestList', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTLIST,
  '__module__' : 'mensajeria_pb2'
  # @@protoc_insertion_point(class_scope:requestList)
  })
_sym_db.RegisterMessage(requestList)

responseList = _reflection.GeneratedProtocolMessageType('responseList', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSELIST,
  '__module__' : 'mensajeria_pb2'
  # @@protoc_insertion_point(class_scope:responseList)
  })
_sym_db.RegisterMessage(responseList)

requestAllMsg = _reflection.GeneratedProtocolMessageType('requestAllMsg', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTALLMSG,
  '__module__' : 'mensajeria_pb2'
  # @@protoc_insertion_point(class_scope:requestAllMsg)
  })
_sym_db.RegisterMessage(requestAllMsg)

responseAllMsg = _reflection.GeneratedProtocolMessageType('responseAllMsg', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEALLMSG,
  '__module__' : 'mensajeria_pb2'
  # @@protoc_insertion_point(class_scope:responseAllMsg)
  })
_sym_db.RegisterMessage(responseAllMsg)


DESCRIPTOR._options = None

_MENSAJERIA = _descriptor.ServiceDescriptor(
  name='Mensajeria',
  full_name='Mensajeria',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=396,
  serialized_end=643,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUser',
    full_name='Mensajeria.CreateUser',
    index=0,
    containing_service=None,
    input_type=_NEWUSER,
    output_type=_RESPONSENEWUSER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MsgToUser',
    full_name='Mensajeria.MsgToUser',
    index=1,
    containing_service=None,
    input_type=_MSGTOUSER,
    output_type=_MSGFROMUSER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ChangeReceptor',
    full_name='Mensajeria.ChangeReceptor',
    index=2,
    containing_service=None,
    input_type=_TOUSER,
    output_type=_TOUSERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ObtainList',
    full_name='Mensajeria.ObtainList',
    index=3,
    containing_service=None,
    input_type=_REQUESTLIST,
    output_type=_RESPONSELIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ObtainAllMsg',
    full_name='Mensajeria.ObtainAllMsg',
    index=4,
    containing_service=None,
    input_type=_REQUESTALLMSG,
    output_type=_RESPONSEALLMSG,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MENSAJERIA)

DESCRIPTOR.services_by_name['Mensajeria'] = _MENSAJERIA

# @@protoc_insertion_point(module_scope)
