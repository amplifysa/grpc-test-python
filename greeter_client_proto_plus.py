import logging

import grpc

from helloword_proto_plus import SayHelloService


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        sayHelloService = SayHelloService(channel)
        response = sayHelloService.sayHello(name="Amplify")
        print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
