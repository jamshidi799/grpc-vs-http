# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: product.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='product.proto',
  package='product',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rproduct.proto\x12\x07product\"P\n\x0cProductProto\x12\r\n\x05title\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"(\n\x11ProductStatsProto\x12\x13\n\x0bvisit_count\x18\x01 \x01(\x05\x32H\n\x07Product\x12=\n\x06update\x12\x15.product.ProductProto\x1a\x1a.product.ProductStatsProto\"\x00\x62\x06proto3'
)




_PRODUCTPROTO = _descriptor.Descriptor(
  name='ProductProto',
  full_name='product.ProductProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='product.ProductProto.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='product.ProductProto.image', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='product.ProductProto.price', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='product.ProductProto.description', index=3,
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
  serialized_start=26,
  serialized_end=106,
)


_PRODUCTSTATSPROTO = _descriptor.Descriptor(
  name='ProductStatsProto',
  full_name='product.ProductStatsProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='visit_count', full_name='product.ProductStatsProto.visit_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=108,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['ProductProto'] = _PRODUCTPROTO
DESCRIPTOR.message_types_by_name['ProductStatsProto'] = _PRODUCTSTATSPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductProto = _reflection.GeneratedProtocolMessageType('ProductProto', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTPROTO,
  '__module__' : 'product_pb2'
  # @@protoc_insertion_point(class_scope:product.ProductProto)
  })
_sym_db.RegisterMessage(ProductProto)

ProductStatsProto = _reflection.GeneratedProtocolMessageType('ProductStatsProto', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTSTATSPROTO,
  '__module__' : 'product_pb2'
  # @@protoc_insertion_point(class_scope:product.ProductStatsProto)
  })
_sym_db.RegisterMessage(ProductStatsProto)



_PRODUCT = _descriptor.ServiceDescriptor(
  name='Product',
  full_name='product.Product',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=150,
  serialized_end=222,
  methods=[
  _descriptor.MethodDescriptor(
    name='update',
    full_name='product.Product.update',
    index=0,
    containing_service=None,
    input_type=_PRODUCTPROTO,
    output_type=_PRODUCTSTATSPROTO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRODUCT)

DESCRIPTOR.services_by_name['Product'] = _PRODUCT

# @@protoc_insertion_point(module_scope)
