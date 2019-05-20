# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: integrations.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from . import definitions_pb2 as definitions__pb2
from . import peers_pb2 as peers__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='integrations.proto',
  package='dialog',
  syntax='proto3',
  serialized_options=_b('\342?\026\n\024im.dlg.grpc.services'),
  serialized_pb=_b('\n\x12integrations.proto\x12\x06\x64ialog\x1a\x1cgoogle/api/annotations.proto\x1a\x11\x64\x65\x66initions.proto\x1a\x0bpeers.proto\x1a\x15scalapb/scalapb.proto\"q\n\x18ResponseIntegrationToken\x12\x1b\n\x05token\x18\x01 \x01(\tB\x0c\x8a\xea\x30\x08\n\x06\x64\x61nger\x12\x19\n\x03url\x18\x02 \x01(\tB\x0c\x8a\xea\x30\x08\n\x06\x64\x61nger:\x1d\xe2?\x1a\n\x18im.dlg.grpc.GrpcResponse\"n\n\x1aRequestGetIntegrationToken\x12\x32\n\ngroup_peer\x18\x01 \x01(\x0b\x32\x0f.dialog.OutPeerB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"q\n\x1dRequestRevokeIntegrationToken\x12\x32\n\ngroup_peer\x18\x01 \x01(\x0b\x32\x0f.dialog.OutPeerB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest2\xbf\x02\n\x0cIntegrations\x12\x91\x01\n\x13GetIntegrationToken\x12\".dialog.RequestGetIntegrationToken\x1a .dialog.ResponseIntegrationToken\"4\x82\xd3\xe4\x93\x02.\")/v1/grpc/Integrations/GetIntegrationToken:\x01*\x12\x9a\x01\n\x16RevokeIntegrationToken\x12%.dialog.RequestRevokeIntegrationToken\x1a .dialog.ResponseIntegrationToken\"7\x82\xd3\xe4\x93\x02\x31\",/v1/grpc/Integrations/RevokeIntegrationToken:\x01*B\x19\xe2?\x16\n\x14im.dlg.grpc.servicesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,definitions__pb2.DESCRIPTOR,peers__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])




_RESPONSEINTEGRATIONTOKEN = _descriptor.Descriptor(
  name='ResponseIntegrationToken',
  full_name='dialog.ResponseIntegrationToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='dialog.ResponseIntegrationToken.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\010\n\006danger'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='dialog.ResponseIntegrationToken.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\010\n\006danger'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\342?\032\n\030im.dlg.grpc.GrpcResponse'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=228,
)


_REQUESTGETINTEGRATIONTOKEN = _descriptor.Descriptor(
  name='RequestGetIntegrationToken',
  full_name='dialog.RequestGetIntegrationToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_peer', full_name='dialog.RequestGetIntegrationToken.group_peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\342?\031\n\027im.dlg.grpc.GrpcRequest'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=340,
)


_REQUESTREVOKEINTEGRATIONTOKEN = _descriptor.Descriptor(
  name='RequestRevokeIntegrationToken',
  full_name='dialog.RequestRevokeIntegrationToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_peer', full_name='dialog.RequestRevokeIntegrationToken.group_peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\342?\031\n\027im.dlg.grpc.GrpcRequest'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=455,
)

_REQUESTGETINTEGRATIONTOKEN.fields_by_name['group_peer'].message_type = peers__pb2._OUTPEER
_REQUESTREVOKEINTEGRATIONTOKEN.fields_by_name['group_peer'].message_type = peers__pb2._OUTPEER
DESCRIPTOR.message_types_by_name['ResponseIntegrationToken'] = _RESPONSEINTEGRATIONTOKEN
DESCRIPTOR.message_types_by_name['RequestGetIntegrationToken'] = _REQUESTGETINTEGRATIONTOKEN
DESCRIPTOR.message_types_by_name['RequestRevokeIntegrationToken'] = _REQUESTREVOKEINTEGRATIONTOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseIntegrationToken = _reflection.GeneratedProtocolMessageType('ResponseIntegrationToken', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEINTEGRATIONTOKEN,
  __module__ = 'integrations_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ResponseIntegrationToken)
  ))
_sym_db.RegisterMessage(ResponseIntegrationToken)

RequestGetIntegrationToken = _reflection.GeneratedProtocolMessageType('RequestGetIntegrationToken', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTGETINTEGRATIONTOKEN,
  __module__ = 'integrations_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestGetIntegrationToken)
  ))
_sym_db.RegisterMessage(RequestGetIntegrationToken)

RequestRevokeIntegrationToken = _reflection.GeneratedProtocolMessageType('RequestRevokeIntegrationToken', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTREVOKEINTEGRATIONTOKEN,
  __module__ = 'integrations_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestRevokeIntegrationToken)
  ))
_sym_db.RegisterMessage(RequestRevokeIntegrationToken)


DESCRIPTOR._options = None
_RESPONSEINTEGRATIONTOKEN.fields_by_name['token']._options = None
_RESPONSEINTEGRATIONTOKEN.fields_by_name['url']._options = None
_RESPONSEINTEGRATIONTOKEN._options = None
_REQUESTGETINTEGRATIONTOKEN.fields_by_name['group_peer']._options = None
_REQUESTGETINTEGRATIONTOKEN._options = None
_REQUESTREVOKEINTEGRATIONTOKEN.fields_by_name['group_peer']._options = None
_REQUESTREVOKEINTEGRATIONTOKEN._options = None

_INTEGRATIONS = _descriptor.ServiceDescriptor(
  name='Integrations',
  full_name='dialog.Integrations',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=458,
  serialized_end=777,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetIntegrationToken',
    full_name='dialog.Integrations.GetIntegrationToken',
    index=0,
    containing_service=None,
    input_type=_REQUESTGETINTEGRATIONTOKEN,
    output_type=_RESPONSEINTEGRATIONTOKEN,
    serialized_options=_b('\202\323\344\223\002.\")/v1/grpc/Integrations/GetIntegrationToken:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='RevokeIntegrationToken',
    full_name='dialog.Integrations.RevokeIntegrationToken',
    index=1,
    containing_service=None,
    input_type=_REQUESTREVOKEINTEGRATIONTOKEN,
    output_type=_RESPONSEINTEGRATIONTOKEN,
    serialized_options=_b('\202\323\344\223\0021\",/v1/grpc/Integrations/RevokeIntegrationToken:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_INTEGRATIONS)

DESCRIPTOR.services_by_name['Integrations'] = _INTEGRATIONS

# @@protoc_insertion_point(module_scope)
