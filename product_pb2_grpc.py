# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import product_pb2 as product__pb2


class ProductStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.update = channel.unary_unary(
                '/product.Product/update',
                request_serializer=product__pb2.ProductProto.SerializeToString,
                response_deserializer=product__pb2.ProductStatsProto.FromString,
                )


class ProductServicer(object):
    """Missing associated documentation comment in .proto file."""

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=product__pb2.ProductProto.FromString,
                    response_serializer=product__pb2.ProductStatsProto.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'product.Product', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Product(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/update',
            product__pb2.ProductProto.SerializeToString,
            product__pb2.ProductStatsProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
