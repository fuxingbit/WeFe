# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data-io-param.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='data-io-param.proto',
    package='com.welab.wefe.core.mlmodel.buffer',
    syntax='proto3',
    serialized_options=b'B\020DataIOParamProto',
    serialized_pb=b'\n\x13\x64\x61ta-io-param.proto\x12\"com.welab.wefe.core.mlmodel.buffer\"\xd4\x02\n\x0cImputerParam\x12h\n\x15missing_replace_value\x18\x01 \x03(\x0b\x32I.com.welab.wefe.core.mlmodel.buffer.ImputerParam.MissingReplaceValueEntry\x12\x64\n\x13missing_value_ratio\x18\x02 \x03(\x0b\x32G.com.welab.wefe.core.mlmodel.buffer.ImputerParam.MissingValueRatioEntry\x1a:\n\x18MissingReplaceValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x38\n\x16MissingValueRatioEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\xd4\x02\n\x0cOutlierParam\x12h\n\x15outlier_replace_value\x18\x01 \x03(\x0b\x32I.com.welab.wefe.core.mlmodel.buffer.OutlierParam.OutlierReplaceValueEntry\x12\x64\n\x13outlier_value_ratio\x18\x02 \x03(\x0b\x32G.com.welab.wefe.core.mlmodel.buffer.OutlierParam.OutlierValueRatioEntry\x1a:\n\x18OutlierReplaceValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x38\n\x16OutlierValueRatioEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\xd5\x01\n\x0b\x44\x61taIOParam\x12\x0e\n\x06header\x18\x01 \x03(\t\x12\x10\n\x08sid_name\x18\x02 \x01(\t\x12\x12\n\nlabel_name\x18\x03 \x01(\t\x12G\n\rimputer_param\x18\x04 \x01(\x0b\x32\x30.com.welab.wefe.core.mlmodel.buffer.ImputerParam\x12G\n\routlier_param\x18\x05 \x01(\x0b\x32\x30.com.welab.wefe.core.mlmodel.buffer.OutlierParamB\x12\x42\x10\x44\x61taIOParamProtob\x06proto3'
)

_IMPUTERPARAM_MISSINGREPLACEVALUEENTRY = _descriptor.Descriptor(
    name='MissingReplaceValueEntry',
    full_name='com.welab.wefe.core.mlmodel.buffer.ImputerParam.MissingReplaceValueEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='com.welab.wefe.core.mlmodel.buffer.ImputerParam.MissingReplaceValueEntry.key',
            index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value', full_name='com.welab.wefe.core.mlmodel.buffer.ImputerParam.MissingReplaceValueEntry.value',
            index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=b'8\001',
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=284,
    serialized_end=342,
)

_IMPUTERPARAM_MISSINGVALUERATIOENTRY = _descriptor.Descriptor(
    name='MissingValueRatioEntry',
    full_name='com.welab.wefe.core.mlmodel.buffer.ImputerParam.MissingValueRatioEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='com.welab.wefe.core.mlmodel.buffer.ImputerParam.MissingValueRatioEntry.key', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value', full_name='com.welab.wefe.core.mlmodel.buffer.ImputerParam.MissingValueRatioEntry.value',
            index=1,
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
    serialized_options=b'8\001',
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=344,
    serialized_end=400,
)

_IMPUTERPARAM = _descriptor.Descriptor(
    name='ImputerParam',
    full_name='com.welab.wefe.core.mlmodel.buffer.ImputerParam',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='missing_replace_value',
            full_name='com.welab.wefe.core.mlmodel.buffer.ImputerParam.missing_replace_value', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='missing_value_ratio', full_name='com.welab.wefe.core.mlmodel.buffer.ImputerParam.missing_value_ratio',
            index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_IMPUTERPARAM_MISSINGREPLACEVALUEENTRY, _IMPUTERPARAM_MISSINGVALUERATIOENTRY, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=60,
    serialized_end=400,
)

_OUTLIERPARAM_OUTLIERREPLACEVALUEENTRY = _descriptor.Descriptor(
    name='OutlierReplaceValueEntry',
    full_name='com.welab.wefe.core.mlmodel.buffer.OutlierParam.OutlierReplaceValueEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='com.welab.wefe.core.mlmodel.buffer.OutlierParam.OutlierReplaceValueEntry.key',
            index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value', full_name='com.welab.wefe.core.mlmodel.buffer.OutlierParam.OutlierReplaceValueEntry.value',
            index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=b'8\001',
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=627,
    serialized_end=685,
)

_OUTLIERPARAM_OUTLIERVALUERATIOENTRY = _descriptor.Descriptor(
    name='OutlierValueRatioEntry',
    full_name='com.welab.wefe.core.mlmodel.buffer.OutlierParam.OutlierValueRatioEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='com.welab.wefe.core.mlmodel.buffer.OutlierParam.OutlierValueRatioEntry.key', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value', full_name='com.welab.wefe.core.mlmodel.buffer.OutlierParam.OutlierValueRatioEntry.value',
            index=1,
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
    serialized_options=b'8\001',
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=687,
    serialized_end=743,
)

_OUTLIERPARAM = _descriptor.Descriptor(
    name='OutlierParam',
    full_name='com.welab.wefe.core.mlmodel.buffer.OutlierParam',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='outlier_replace_value',
            full_name='com.welab.wefe.core.mlmodel.buffer.OutlierParam.outlier_replace_value', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='outlier_value_ratio', full_name='com.welab.wefe.core.mlmodel.buffer.OutlierParam.outlier_value_ratio',
            index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_OUTLIERPARAM_OUTLIERREPLACEVALUEENTRY, _OUTLIERPARAM_OUTLIERVALUERATIOENTRY, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=403,
    serialized_end=743,
)

_DATAIOPARAM = _descriptor.Descriptor(
    name='DataIOParam',
    full_name='com.welab.wefe.core.mlmodel.buffer.DataIOParam',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='header', full_name='com.welab.wefe.core.mlmodel.buffer.DataIOParam.header', index=0,
            number=1, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='sid_name', full_name='com.welab.wefe.core.mlmodel.buffer.DataIOParam.sid_name', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='label_name', full_name='com.welab.wefe.core.mlmodel.buffer.DataIOParam.label_name', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='imputer_param', full_name='com.welab.wefe.core.mlmodel.buffer.DataIOParam.imputer_param', index=3,
            number=4, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='outlier_param', full_name='com.welab.wefe.core.mlmodel.buffer.DataIOParam.outlier_param', index=4,
            number=5, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
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
    serialized_start=746,
    serialized_end=959,
)

_IMPUTERPARAM_MISSINGREPLACEVALUEENTRY.containing_type = _IMPUTERPARAM
_IMPUTERPARAM_MISSINGVALUERATIOENTRY.containing_type = _IMPUTERPARAM
_IMPUTERPARAM.fields_by_name['missing_replace_value'].message_type = _IMPUTERPARAM_MISSINGREPLACEVALUEENTRY
_IMPUTERPARAM.fields_by_name['missing_value_ratio'].message_type = _IMPUTERPARAM_MISSINGVALUERATIOENTRY
_OUTLIERPARAM_OUTLIERREPLACEVALUEENTRY.containing_type = _OUTLIERPARAM
_OUTLIERPARAM_OUTLIERVALUERATIOENTRY.containing_type = _OUTLIERPARAM
_OUTLIERPARAM.fields_by_name['outlier_replace_value'].message_type = _OUTLIERPARAM_OUTLIERREPLACEVALUEENTRY
_OUTLIERPARAM.fields_by_name['outlier_value_ratio'].message_type = _OUTLIERPARAM_OUTLIERVALUERATIOENTRY
_DATAIOPARAM.fields_by_name['imputer_param'].message_type = _IMPUTERPARAM
_DATAIOPARAM.fields_by_name['outlier_param'].message_type = _OUTLIERPARAM
DESCRIPTOR.message_types_by_name['ImputerParam'] = _IMPUTERPARAM
DESCRIPTOR.message_types_by_name['OutlierParam'] = _OUTLIERPARAM
DESCRIPTOR.message_types_by_name['DataIOParam'] = _DATAIOPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImputerParam = _reflection.GeneratedProtocolMessageType('ImputerParam', (_message.Message,), {

    'MissingReplaceValueEntry': _reflection.GeneratedProtocolMessageType('MissingReplaceValueEntry',
                                                                         (_message.Message,), {
                                                                             'DESCRIPTOR': _IMPUTERPARAM_MISSINGREPLACEVALUEENTRY,
                                                                             '__module__': 'data_io_param_pb2'
                                                                             # @@protoc_insertion_point(class_scope:com.welab.wefe.core.mlmodel.buffer.ImputerParam.MissingReplaceValueEntry)
                                                                         })
    ,

    'MissingValueRatioEntry': _reflection.GeneratedProtocolMessageType('MissingValueRatioEntry', (_message.Message,), {
        'DESCRIPTOR': _IMPUTERPARAM_MISSINGVALUERATIOENTRY,
        '__module__': 'data_io_param_pb2'
        # @@protoc_insertion_point(class_scope:com.welab.wefe.core.mlmodel.buffer.ImputerParam.MissingValueRatioEntry)
    })
    ,
    'DESCRIPTOR': _IMPUTERPARAM,
    '__module__': 'data_io_param_pb2'
    # @@protoc_insertion_point(class_scope:com.welab.wefe.core.mlmodel.buffer.ImputerParam)
})
_sym_db.RegisterMessage(ImputerParam)
_sym_db.RegisterMessage(ImputerParam.MissingReplaceValueEntry)
_sym_db.RegisterMessage(ImputerParam.MissingValueRatioEntry)

OutlierParam = _reflection.GeneratedProtocolMessageType('OutlierParam', (_message.Message,), {

    'OutlierReplaceValueEntry': _reflection.GeneratedProtocolMessageType('OutlierReplaceValueEntry',
                                                                         (_message.Message,), {
                                                                             'DESCRIPTOR': _OUTLIERPARAM_OUTLIERREPLACEVALUEENTRY,
                                                                             '__module__': 'data_io_param_pb2'
                                                                             # @@protoc_insertion_point(class_scope:com.welab.wefe.core.mlmodel.buffer.OutlierParam.OutlierReplaceValueEntry)
                                                                         })
    ,

    'OutlierValueRatioEntry': _reflection.GeneratedProtocolMessageType('OutlierValueRatioEntry', (_message.Message,), {
        'DESCRIPTOR': _OUTLIERPARAM_OUTLIERVALUERATIOENTRY,
        '__module__': 'data_io_param_pb2'
        # @@protoc_insertion_point(class_scope:com.welab.wefe.core.mlmodel.buffer.OutlierParam.OutlierValueRatioEntry)
    })
    ,
    'DESCRIPTOR': _OUTLIERPARAM,
    '__module__': 'data_io_param_pb2'
    # @@protoc_insertion_point(class_scope:com.welab.wefe.core.mlmodel.buffer.OutlierParam)
})
_sym_db.RegisterMessage(OutlierParam)
_sym_db.RegisterMessage(OutlierParam.OutlierReplaceValueEntry)
_sym_db.RegisterMessage(OutlierParam.OutlierValueRatioEntry)

DataIOParam = _reflection.GeneratedProtocolMessageType('DataIOParam', (_message.Message,), {
    'DESCRIPTOR': _DATAIOPARAM,
    '__module__': 'data_io_param_pb2'
    # @@protoc_insertion_point(class_scope:com.welab.wefe.core.mlmodel.buffer.DataIOParam)
})
_sym_db.RegisterMessage(DataIOParam)

DESCRIPTOR._options = None
_IMPUTERPARAM_MISSINGREPLACEVALUEENTRY._options = None
_IMPUTERPARAM_MISSINGVALUERATIOENTRY._options = None
_OUTLIERPARAM_OUTLIERREPLACEVALUEENTRY._options = None
_OUTLIERPARAM_OUTLIERVALUERATIOENTRY._options = None
# @@protoc_insertion_point(module_scope)
