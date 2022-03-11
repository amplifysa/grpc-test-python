import proto


class HelloRequest(proto.Message):
    name = proto.Field(proto.STRING, number=1)


class HelloReply(proto.Message):
    message = proto.Field(proto.STRING, number=1)


class SayHelloService:
    def __init__(self, channel):
        self.SayHello = channel.unary_unary(
            '/Greeter/SayHello',
            request_serializer=HelloRequest.serialize,
            response_deserializer=HelloReply.deserialize,
        )

    def sayHello(self, name) -> HelloReply:
        return self.SayHello(HelloRequest(name=name))
