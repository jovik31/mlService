# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/file_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proto/file_service.proto\"\x1f\n\nFileStream\x12\x11\n\tfileChunk\x18\x01 \x01(\x0c\"\x1f\n\x0bRequestFile\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\"\x14\n\x04\x46ile\x12\x0c\n\x04\x66ile\x18\x01 \x01(\x0c\"0\n\x0cResponseFile\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\t2\xb3\x01\n\x0b\x46ileTranfer\x12.\n\x0cUploadStream\x12\x0b.FileStream\x1a\r.ResponseFile\"\x00(\x01\x12/\n\x0e\x44ownloadStream\x12\x0c.RequestFile\x1a\x0b.FileStream\"\x00\x30\x01\x12 \n\x06Upload\x12\x05.File\x1a\r.ResponseFile\"\x00\x12!\n\x08\x44ownload\x12\x0c.RequestFile\x1a\x05.File\"\x00\x42\tZ\x07./protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.file_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\007./proto'
  _globals['_FILESTREAM']._serialized_start=28
  _globals['_FILESTREAM']._serialized_end=59
  _globals['_REQUESTFILE']._serialized_start=61
  _globals['_REQUESTFILE']._serialized_end=92
  _globals['_FILE']._serialized_start=94
  _globals['_FILE']._serialized_end=114
  _globals['_RESPONSEFILE']._serialized_start=116
  _globals['_RESPONSEFILE']._serialized_end=164
  _globals['_FILETRANFER']._serialized_start=167
  _globals['_FILETRANFER']._serialized_end=346
# @@protoc_insertion_point(module_scope)
