# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import midmsg_pb2 as proto_dot_midmsg__pb2


class MidServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Sync = channel.unary_unary(
        '/proto.MidService/Sync',
        request_serializer=proto_dot_midmsg__pb2.NetReqInfo.SerializeToString,
        response_deserializer=proto_dot_midmsg__pb2.NetRspInfo.FromString,
        )
    self.Async = channel.unary_unary(
        '/proto.MidService/Async',
        request_serializer=proto_dot_midmsg__pb2.NetReqInfo.SerializeToString,
        response_deserializer=proto_dot_midmsg__pb2.NetRspInfo.FromString,
        )
    self.Broadcast = channel.unary_unary(
        '/proto.MidService/Broadcast',
        request_serializer=proto_dot_midmsg__pb2.NetReqInfo.SerializeToString,
        response_deserializer=proto_dot_midmsg__pb2.NetRspInfo.FromString,
        )
    self.Register = channel.unary_unary(
        '/proto.MidService/Register',
        request_serializer=proto_dot_midmsg__pb2.RegisterInfo.SerializeToString,
        response_deserializer=proto_dot_midmsg__pb2.RegisterReturnInfo.FromString,
        )
    self.Publish = channel.unary_unary(
        '/proto.MidService/Publish',
        request_serializer=proto_dot_midmsg__pb2.PublishInfo.SerializeToString,
        response_deserializer=proto_dot_midmsg__pb2.PublishReturnInfo.FromString,
        )
    self.Subscribe = channel.unary_unary(
        '/proto.MidService/Subscribe',
        request_serializer=proto_dot_midmsg__pb2.SubscribeInfo.SerializeToString,
        response_deserializer=proto_dot_midmsg__pb2.SubscribeReturnInfo.FromString,
        )


class MidServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Sync(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Async(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Broadcast(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Register(self, request, context):
    """rpc ReloadConfig(Rload)         returns (Rload) {};
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Publish(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Subscribe(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MidServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Sync': grpc.unary_unary_rpc_method_handler(
          servicer.Sync,
          request_deserializer=proto_dot_midmsg__pb2.NetReqInfo.FromString,
          response_serializer=proto_dot_midmsg__pb2.NetRspInfo.SerializeToString,
      ),
      'Async': grpc.unary_unary_rpc_method_handler(
          servicer.Async,
          request_deserializer=proto_dot_midmsg__pb2.NetReqInfo.FromString,
          response_serializer=proto_dot_midmsg__pb2.NetRspInfo.SerializeToString,
      ),
      'Broadcast': grpc.unary_unary_rpc_method_handler(
          servicer.Broadcast,
          request_deserializer=proto_dot_midmsg__pb2.NetReqInfo.FromString,
          response_serializer=proto_dot_midmsg__pb2.NetRspInfo.SerializeToString,
      ),
      'Register': grpc.unary_unary_rpc_method_handler(
          servicer.Register,
          request_deserializer=proto_dot_midmsg__pb2.RegisterInfo.FromString,
          response_serializer=proto_dot_midmsg__pb2.RegisterReturnInfo.SerializeToString,
      ),
      'Publish': grpc.unary_unary_rpc_method_handler(
          servicer.Publish,
          request_deserializer=proto_dot_midmsg__pb2.PublishInfo.FromString,
          response_serializer=proto_dot_midmsg__pb2.PublishReturnInfo.SerializeToString,
      ),
      'Subscribe': grpc.unary_unary_rpc_method_handler(
          servicer.Subscribe,
          request_deserializer=proto_dot_midmsg__pb2.SubscribeInfo.FromString,
          response_serializer=proto_dot_midmsg__pb2.SubscribeReturnInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.MidService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ClientServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Call = channel.unary_unary(
        '/proto.ClientService/Call',
        request_serializer=proto_dot_midmsg__pb2.NetReqInfo.SerializeToString,
        response_deserializer=proto_dot_midmsg__pb2.CallRspInfo.FromString,
        )
    self.AsyncCall = channel.unary_unary(
        '/proto.ClientService/AsyncCall',
        request_serializer=proto_dot_midmsg__pb2.SingleResultInfo.SerializeToString,
        response_deserializer=proto_dot_midmsg__pb2.CallRspInfo.FromString,
        )


class ClientServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Call(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AsyncCall(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClientServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Call': grpc.unary_unary_rpc_method_handler(
          servicer.Call,
          request_deserializer=proto_dot_midmsg__pb2.NetReqInfo.FromString,
          response_serializer=proto_dot_midmsg__pb2.CallRspInfo.SerializeToString,
      ),
      'AsyncCall': grpc.unary_unary_rpc_method_handler(
          servicer.AsyncCall,
          request_deserializer=proto_dot_midmsg__pb2.SingleResultInfo.FromString,
          response_serializer=proto_dot_midmsg__pb2.CallRspInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.ClientService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
