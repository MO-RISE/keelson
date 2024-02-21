# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: Rudder.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import Rudder_pb2


class RudderBase(abc.ABC):

    @abc.abstractmethod
    async def set_rudder_angle_listener_key(self, stream: 'grpclib.server.Stream[Rudder_pb2.RudderAngle, Rudder_pb2.Response]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/Rudder/set_rudder_angle_listener_key': grpclib.const.Handler(
                self.set_rudder_angle_listener_key,
                grpclib.const.Cardinality.UNARY_UNARY,
                Rudder_pb2.RudderAngle,
                Rudder_pb2.Response,
            ),
        }


class RudderStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.set_rudder_angle_listener_key = grpclib.client.UnaryUnaryMethod(
            channel,
            '/Rudder/set_rudder_angle_listener_key',
            Rudder_pb2.RudderAngle,
            Rudder_pb2.Response,
        )