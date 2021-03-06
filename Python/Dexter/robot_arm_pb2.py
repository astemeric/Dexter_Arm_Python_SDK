# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: robot_arm.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='robot_arm.proto',
  package='SpotPlusArm',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0frobot_arm.proto\x12\x0bSpotPlusArm\"\xcb\x02\n\x13\x64\x65xterConfiguration\x12\x32\n\x02j1\x18\x01 \x01(\x0b\x32&.SpotPlusArm.dexterConfiguration.Joint\x12\x32\n\x02j2\x18\x02 \x01(\x0b\x32&.SpotPlusArm.dexterConfiguration.Joint\x12\x32\n\x02j3\x18\x03 \x01(\x0b\x32&.SpotPlusArm.dexterConfiguration.Joint\x12\x32\n\x02j4\x18\x04 \x01(\x0b\x32&.SpotPlusArm.dexterConfiguration.Joint\x12\x32\n\x02j5\x18\x05 \x01(\x0b\x32&.SpotPlusArm.dexterConfiguration.Joint\x1a\x30\n\x05Joint\x12\x14\n\x0c\x63urrentAngle\x18\x01 \x01(\x01\x12\x11\n\tgoalAngle\x18\x02 \x01(\x01\"x\n\x0e\x64\x65xterRequest5\x12\n\n\x02j1\x18\x01 \x01(\x01\x12\n\n\x02j2\x18\x02 \x01(\x01\x12\n\n\x02j3\x18\x03 \x01(\x01\x12\n\n\x02j4\x18\x04 \x01(\x01\x12\n\n\x02j5\x18\x05 \x01(\x01\x12*\n\x0b\x63ommandType\x18\x06 \x01(\x0e\x32\x15.SpotPlusArm.MoveType\"\x90\x01\n\x0e\x64\x65xterRequest7\x12\n\n\x02j1\x18\x01 \x01(\x01\x12\n\n\x02j2\x18\x02 \x01(\x01\x12\n\n\x02j3\x18\x03 \x01(\x01\x12\n\n\x02j4\x18\x04 \x01(\x01\x12\n\n\x02j5\x18\x05 \x01(\x01\x12\n\n\x02j6\x18\x06 \x01(\x01\x12\n\n\x02j7\x18\x07 \x01(\x01\x12*\n\x0b\x63ommandType\x18\x08 \x01(\x0e\x32\x15.SpotPlusArm.MoveType\"\x1e\n\x0c\x64\x65xterStatus\x12\x0e\n\x06status\x18\x01 \x01(\x05*\"\n\x08MoveType\x12\n\n\x06P_MOVE\x10\x00\x12\n\n\x06\x41_MOVE\x10\x01\x62\x06proto3'
)

_MOVETYPE = _descriptor.EnumDescriptor(
  name='MoveType',
  full_name='SpotPlusArm.MoveType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='P_MOVE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='A_MOVE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=667,
  serialized_end=701,
)
_sym_db.RegisterEnumDescriptor(_MOVETYPE)

MoveType = enum_type_wrapper.EnumTypeWrapper(_MOVETYPE)
P_MOVE = 0
A_MOVE = 1



_DEXTERCONFIGURATION_JOINT = _descriptor.Descriptor(
  name='Joint',
  full_name='SpotPlusArm.dexterConfiguration.Joint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currentAngle', full_name='SpotPlusArm.dexterConfiguration.Joint.currentAngle', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goalAngle', full_name='SpotPlusArm.dexterConfiguration.Joint.goalAngle', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=316,
  serialized_end=364,
)

_DEXTERCONFIGURATION = _descriptor.Descriptor(
  name='dexterConfiguration',
  full_name='SpotPlusArm.dexterConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='j1', full_name='SpotPlusArm.dexterConfiguration.j1', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j2', full_name='SpotPlusArm.dexterConfiguration.j2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j3', full_name='SpotPlusArm.dexterConfiguration.j3', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j4', full_name='SpotPlusArm.dexterConfiguration.j4', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j5', full_name='SpotPlusArm.dexterConfiguration.j5', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEXTERCONFIGURATION_JOINT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=364,
)


_DEXTERREQUEST5 = _descriptor.Descriptor(
  name='dexterRequest5',
  full_name='SpotPlusArm.dexterRequest5',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='j1', full_name='SpotPlusArm.dexterRequest5.j1', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j2', full_name='SpotPlusArm.dexterRequest5.j2', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j3', full_name='SpotPlusArm.dexterRequest5.j3', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j4', full_name='SpotPlusArm.dexterRequest5.j4', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j5', full_name='SpotPlusArm.dexterRequest5.j5', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commandType', full_name='SpotPlusArm.dexterRequest5.commandType', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=366,
  serialized_end=486,
)


_DEXTERREQUEST7 = _descriptor.Descriptor(
  name='dexterRequest7',
  full_name='SpotPlusArm.dexterRequest7',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='j1', full_name='SpotPlusArm.dexterRequest7.j1', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j2', full_name='SpotPlusArm.dexterRequest7.j2', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j3', full_name='SpotPlusArm.dexterRequest7.j3', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j4', full_name='SpotPlusArm.dexterRequest7.j4', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j5', full_name='SpotPlusArm.dexterRequest7.j5', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j6', full_name='SpotPlusArm.dexterRequest7.j6', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j7', full_name='SpotPlusArm.dexterRequest7.j7', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commandType', full_name='SpotPlusArm.dexterRequest7.commandType', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=489,
  serialized_end=633,
)


_DEXTERSTATUS = _descriptor.Descriptor(
  name='dexterStatus',
  full_name='SpotPlusArm.dexterStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SpotPlusArm.dexterStatus.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=635,
  serialized_end=665,
)

_DEXTERCONFIGURATION_JOINT.containing_type = _DEXTERCONFIGURATION
_DEXTERCONFIGURATION.fields_by_name['j1'].message_type = _DEXTERCONFIGURATION_JOINT
_DEXTERCONFIGURATION.fields_by_name['j2'].message_type = _DEXTERCONFIGURATION_JOINT
_DEXTERCONFIGURATION.fields_by_name['j3'].message_type = _DEXTERCONFIGURATION_JOINT
_DEXTERCONFIGURATION.fields_by_name['j4'].message_type = _DEXTERCONFIGURATION_JOINT
_DEXTERCONFIGURATION.fields_by_name['j5'].message_type = _DEXTERCONFIGURATION_JOINT
_DEXTERREQUEST5.fields_by_name['commandType'].enum_type = _MOVETYPE
_DEXTERREQUEST7.fields_by_name['commandType'].enum_type = _MOVETYPE
DESCRIPTOR.message_types_by_name['dexterConfiguration'] = _DEXTERCONFIGURATION
DESCRIPTOR.message_types_by_name['dexterRequest5'] = _DEXTERREQUEST5
DESCRIPTOR.message_types_by_name['dexterRequest7'] = _DEXTERREQUEST7
DESCRIPTOR.message_types_by_name['dexterStatus'] = _DEXTERSTATUS
DESCRIPTOR.enum_types_by_name['MoveType'] = _MOVETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

dexterConfiguration = _reflection.GeneratedProtocolMessageType('dexterConfiguration', (_message.Message,), {

  'Joint' : _reflection.GeneratedProtocolMessageType('Joint', (_message.Message,), {
    'DESCRIPTOR' : _DEXTERCONFIGURATION_JOINT,
    '__module__' : 'robot_arm_pb2'
    # @@protoc_insertion_point(class_scope:SpotPlusArm.dexterConfiguration.Joint)
    })
  ,
  'DESCRIPTOR' : _DEXTERCONFIGURATION,
  '__module__' : 'robot_arm_pb2'
  # @@protoc_insertion_point(class_scope:SpotPlusArm.dexterConfiguration)
  })
_sym_db.RegisterMessage(dexterConfiguration)
_sym_db.RegisterMessage(dexterConfiguration.Joint)

dexterRequest5 = _reflection.GeneratedProtocolMessageType('dexterRequest5', (_message.Message,), {
  'DESCRIPTOR' : _DEXTERREQUEST5,
  '__module__' : 'robot_arm_pb2'
  # @@protoc_insertion_point(class_scope:SpotPlusArm.dexterRequest5)
  })
_sym_db.RegisterMessage(dexterRequest5)

dexterRequest7 = _reflection.GeneratedProtocolMessageType('dexterRequest7', (_message.Message,), {
  'DESCRIPTOR' : _DEXTERREQUEST7,
  '__module__' : 'robot_arm_pb2'
  # @@protoc_insertion_point(class_scope:SpotPlusArm.dexterRequest7)
  })
_sym_db.RegisterMessage(dexterRequest7)

dexterStatus = _reflection.GeneratedProtocolMessageType('dexterStatus', (_message.Message,), {
  'DESCRIPTOR' : _DEXTERSTATUS,
  '__module__' : 'robot_arm_pb2'
  # @@protoc_insertion_point(class_scope:SpotPlusArm.dexterStatus)
  })
_sym_db.RegisterMessage(dexterStatus)


# @@protoc_insertion_point(module_scope)
