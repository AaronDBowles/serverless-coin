# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: full_node.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='full_node.proto',
  package='full_node',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x66ull_node.proto\x12\tfull_node\x1a\x1fgoogle/protobuf/timestamp.proto\"&\n\x04Node\x12\x11\n\tnode_type\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"\x9c\x01\n\x05\x42lock\x12\x15\n\rprevious_hash\x18\x01 \x01(\t\x12,\n\x0ctransactions\x18\x02 \x03(\x0b\x32\x16.full_node.Transaction\x12\x31\n\rcreation_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05nonce\x18\x04 \x01(\x03\x12\x0c\n\x04hash\x18\x05 \x01(\t\"\x96\x01\n\x12TransactionDetails\x12\x12\n\nto_address\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x02\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x14\n\x0ctarget_input\x18\x04 \x01(\t\x12\x0c\n\x04\x66\x65\x65s\x18\x05 \x01(\x02\x12(\n\nchallenges\x18\x06 \x03(\x0b\x32\x14.full_node.Challenge\"~\n\x0f\x43hallengeTarget\x12\x0e\n\x06\x62inary\x18\x01 \x01(\t\x12\x15\n\rinitial_input\x18\x02 \x01(\t\x12\x44\n\x18\x65nvironment_requirements\x18\x03 \x01(\x0b\x32\".full_node.EnvironmentRequirements\"R\n\x17\x45nvironmentRequirements\x12\x18\n\x10operating_system\x18\x01 \x01(\t\x12\x1d\n\x15prerequisite_installs\x18\x02 \x03(\t\"w\n\tExecution\x12\x14\n\x0c\x63hallenge_id\x18\x01 \x01(\t\x12\x1a\n\x12\x65xecutor_signature\x18\x02 \x01(\t\x12\x13\n\x0btarget_hash\x18\x03 \x01(\t\x12\x13\n\x0bresult_hash\x18\x04 \x01(\t\x12\x0e\n\x06\x65rrors\x18\x05 \x01(\t\"\xa3\x01\n\tChallenge\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\x06target\x18\x02 \x01(\x0b\x32\x1a.full_node.ChallengeTarget\x12(\n\nexecutions\x18\x03 \x03(\x0b\x32\x14.full_node.Execution\x12\x16\n\x0etransaction_id\x18\x04 \x01(\t\x12\x1c\n\x14\x63hallenger_signature\x18\x05 \x01(\t\"j\n\x0bTransaction\x12\x11\n\tsignature\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12.\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x1d.full_node.TransactionDetails\x12\n\n\x02id\x18\x04 \x01(\t\"\x81\x02\n\x08NodeInfo\x12\x1e\n\x05nodes\x18\x01 \x03(\x0b\x32\x0f.full_node.Node\x12\x1f\n\x05\x63hain\x18\x02 \x03(\x0b\x32\x10.full_node.Block\x12\x37\n\x17\x65xecutable_transactions\x18\x03 \x03(\x0b\x32\x16.full_node.Transaction\x12\x35\n\x15\x65xecuted_transactions\x18\x04 \x03(\x0b\x32\x16.full_node.Transaction\x12\x1a\n\x12\x63urrent_difficulty\x18\x05 \x01(\x05\x12(\n\nchallenges\x18\x06 \x03(\x0b\x32\x14.full_node.Challenge2\x88\x01\n\x08\x46ullNode\x12<\n\x0epush_node_info\x12\x13.full_node.NodeInfo\x1a\x13.full_node.NodeInfo\"\x00\x12>\n\x0epush_challenge\x12\x14.full_node.Challenge\x1a\x14.full_node.Challenge\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='full_node.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_type', full_name='full_node.Node.node_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='full_node.Node.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=63,
  serialized_end=101,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='full_node.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='previous_hash', full_name='full_node.Block.previous_hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactions', full_name='full_node.Block.transactions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='full_node.Block.creation_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='full_node.Block.nonce', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='full_node.Block.hash', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=104,
  serialized_end=260,
)


_TRANSACTIONDETAILS = _descriptor.Descriptor(
  name='TransactionDetails',
  full_name='full_node.TransactionDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='to_address', full_name='full_node.TransactionDetails.to_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='full_node.TransactionDetails.amount', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='full_node.TransactionDetails.target', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_input', full_name='full_node.TransactionDetails.target_input', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fees', full_name='full_node.TransactionDetails.fees', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='challenges', full_name='full_node.TransactionDetails.challenges', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=263,
  serialized_end=413,
)


_CHALLENGETARGET = _descriptor.Descriptor(
  name='ChallengeTarget',
  full_name='full_node.ChallengeTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='binary', full_name='full_node.ChallengeTarget.binary', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial_input', full_name='full_node.ChallengeTarget.initial_input', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environment_requirements', full_name='full_node.ChallengeTarget.environment_requirements', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=415,
  serialized_end=541,
)


_ENVIRONMENTREQUIREMENTS = _descriptor.Descriptor(
  name='EnvironmentRequirements',
  full_name='full_node.EnvironmentRequirements',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operating_system', full_name='full_node.EnvironmentRequirements.operating_system', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prerequisite_installs', full_name='full_node.EnvironmentRequirements.prerequisite_installs', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=543,
  serialized_end=625,
)


_EXECUTION = _descriptor.Descriptor(
  name='Execution',
  full_name='full_node.Execution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge_id', full_name='full_node.Execution.challenge_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='executor_signature', full_name='full_node.Execution.executor_signature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_hash', full_name='full_node.Execution.target_hash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_hash', full_name='full_node.Execution.result_hash', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errors', full_name='full_node.Execution.errors', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=627,
  serialized_end=746,
)


_CHALLENGE = _descriptor.Descriptor(
  name='Challenge',
  full_name='full_node.Challenge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='full_node.Challenge.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='full_node.Challenge.target', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='executions', full_name='full_node.Challenge.executions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='full_node.Challenge.transaction_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='challenger_signature', full_name='full_node.Challenge.challenger_signature', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=749,
  serialized_end=912,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='full_node.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='full_node.Transaction.signature', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='full_node.Transaction.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='details', full_name='full_node.Transaction.details', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='full_node.Transaction.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=914,
  serialized_end=1020,
)


_NODEINFO = _descriptor.Descriptor(
  name='NodeInfo',
  full_name='full_node.NodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='full_node.NodeInfo.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chain', full_name='full_node.NodeInfo.chain', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='executable_transactions', full_name='full_node.NodeInfo.executable_transactions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='executed_transactions', full_name='full_node.NodeInfo.executed_transactions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_difficulty', full_name='full_node.NodeInfo.current_difficulty', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='challenges', full_name='full_node.NodeInfo.challenges', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1023,
  serialized_end=1280,
)

_BLOCK.fields_by_name['transactions'].message_type = _TRANSACTION
_BLOCK.fields_by_name['creation_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRANSACTIONDETAILS.fields_by_name['challenges'].message_type = _CHALLENGE
_CHALLENGETARGET.fields_by_name['environment_requirements'].message_type = _ENVIRONMENTREQUIREMENTS
_CHALLENGE.fields_by_name['target'].message_type = _CHALLENGETARGET
_CHALLENGE.fields_by_name['executions'].message_type = _EXECUTION
_TRANSACTION.fields_by_name['details'].message_type = _TRANSACTIONDETAILS
_NODEINFO.fields_by_name['nodes'].message_type = _NODE
_NODEINFO.fields_by_name['chain'].message_type = _BLOCK
_NODEINFO.fields_by_name['executable_transactions'].message_type = _TRANSACTION
_NODEINFO.fields_by_name['executed_transactions'].message_type = _TRANSACTION
_NODEINFO.fields_by_name['challenges'].message_type = _CHALLENGE
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['TransactionDetails'] = _TRANSACTIONDETAILS
DESCRIPTOR.message_types_by_name['ChallengeTarget'] = _CHALLENGETARGET
DESCRIPTOR.message_types_by_name['EnvironmentRequirements'] = _ENVIRONMENTREQUIREMENTS
DESCRIPTOR.message_types_by_name['Execution'] = _EXECUTION
DESCRIPTOR.message_types_by_name['Challenge'] = _CHALLENGE
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['NodeInfo'] = _NODEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:full_node.Node)
  })
_sym_db.RegisterMessage(Node)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:full_node.Block)
  })
_sym_db.RegisterMessage(Block)

TransactionDetails = _reflection.GeneratedProtocolMessageType('TransactionDetails', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONDETAILS,
  '__module__' : 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:full_node.TransactionDetails)
  })
_sym_db.RegisterMessage(TransactionDetails)

ChallengeTarget = _reflection.GeneratedProtocolMessageType('ChallengeTarget', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGETARGET,
  '__module__' : 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:full_node.ChallengeTarget)
  })
_sym_db.RegisterMessage(ChallengeTarget)

EnvironmentRequirements = _reflection.GeneratedProtocolMessageType('EnvironmentRequirements', (_message.Message,), {
  'DESCRIPTOR' : _ENVIRONMENTREQUIREMENTS,
  '__module__' : 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:full_node.EnvironmentRequirements)
  })
_sym_db.RegisterMessage(EnvironmentRequirements)

Execution = _reflection.GeneratedProtocolMessageType('Execution', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTION,
  '__module__' : 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:full_node.Execution)
  })
_sym_db.RegisterMessage(Execution)

Challenge = _reflection.GeneratedProtocolMessageType('Challenge', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGE,
  '__module__' : 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:full_node.Challenge)
  })
_sym_db.RegisterMessage(Challenge)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:full_node.Transaction)
  })
_sym_db.RegisterMessage(Transaction)

NodeInfo = _reflection.GeneratedProtocolMessageType('NodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _NODEINFO,
  '__module__' : 'full_node_pb2'
  # @@protoc_insertion_point(class_scope:full_node.NodeInfo)
  })
_sym_db.RegisterMessage(NodeInfo)



_FULLNODE = _descriptor.ServiceDescriptor(
  name='FullNode',
  full_name='full_node.FullNode',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1283,
  serialized_end=1419,
  methods=[
  _descriptor.MethodDescriptor(
    name='push_node_info',
    full_name='full_node.FullNode.push_node_info',
    index=0,
    containing_service=None,
    input_type=_NODEINFO,
    output_type=_NODEINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='push_challenge',
    full_name='full_node.FullNode.push_challenge',
    index=1,
    containing_service=None,
    input_type=_CHALLENGE,
    output_type=_CHALLENGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FULLNODE)

DESCRIPTOR.services_by_name['FullNode'] = _FULLNODE

# @@protoc_insertion_point(module_scope)
