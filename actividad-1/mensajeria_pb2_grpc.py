# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import mensajeria_pb2 as mensajeria__pb2


class MensajeriaStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateUser = channel.unary_unary(
        '/Mensajeria/CreateUser',
        request_serializer=mensajeria__pb2.newUser.SerializeToString,
        response_deserializer=mensajeria__pb2.responseNewUser.FromString,
        )
    self.MsgToUser = channel.unary_unary(
        '/Mensajeria/MsgToUser',
        request_serializer=mensajeria__pb2.msgToUser.SerializeToString,
        response_deserializer=mensajeria__pb2.responseCreationMsg.FromString,
        )
    self.ObtainList = channel.unary_stream(
        '/Mensajeria/ObtainList',
        request_serializer=mensajeria__pb2.requestList.SerializeToString,
        response_deserializer=mensajeria__pb2.responseList.FromString,
        )
    self.ObtainAllMsg = channel.unary_stream(
        '/Mensajeria/ObtainAllMsg',
        request_serializer=mensajeria__pb2.requestAllMsg.SerializeToString,
        response_deserializer=mensajeria__pb2.responseAllMsg.FromString,
        )
    self.WaitingMsg = channel.unary_unary(
        '/Mensajeria/WaitingMsg',
        request_serializer=mensajeria__pb2.requestUser.SerializeToString,
        response_deserializer=mensajeria__pb2.waitingMessage.FromString,
        )
    self.ViewMsg = channel.unary_stream(
        '/Mensajeria/ViewMsg',
        request_serializer=mensajeria__pb2.requestMsg.SerializeToString,
        response_deserializer=mensajeria__pb2.responseMsg.FromString,
        )


class MensajeriaServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MsgToUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ObtainList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ObtainAllMsg(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WaitingMsg(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ViewMsg(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MensajeriaServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateUser': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUser,
          request_deserializer=mensajeria__pb2.newUser.FromString,
          response_serializer=mensajeria__pb2.responseNewUser.SerializeToString,
      ),
      'MsgToUser': grpc.unary_unary_rpc_method_handler(
          servicer.MsgToUser,
          request_deserializer=mensajeria__pb2.msgToUser.FromString,
          response_serializer=mensajeria__pb2.responseCreationMsg.SerializeToString,
      ),
      'ObtainList': grpc.unary_stream_rpc_method_handler(
          servicer.ObtainList,
          request_deserializer=mensajeria__pb2.requestList.FromString,
          response_serializer=mensajeria__pb2.responseList.SerializeToString,
      ),
      'ObtainAllMsg': grpc.unary_stream_rpc_method_handler(
          servicer.ObtainAllMsg,
          request_deserializer=mensajeria__pb2.requestAllMsg.FromString,
          response_serializer=mensajeria__pb2.responseAllMsg.SerializeToString,
      ),
      'WaitingMsg': grpc.unary_unary_rpc_method_handler(
          servicer.WaitingMsg,
          request_deserializer=mensajeria__pb2.requestUser.FromString,
          response_serializer=mensajeria__pb2.waitingMessage.SerializeToString,
      ),
      'ViewMsg': grpc.unary_stream_rpc_method_handler(
          servicer.ViewMsg,
          request_deserializer=mensajeria__pb2.requestMsg.FromString,
          response_serializer=mensajeria__pb2.responseMsg.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Mensajeria', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
