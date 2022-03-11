import asyncio
import logging

import grpc

from helloword_proto_plus import SayHelloService


async def run():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        sayHelloService = SayHelloService(channel)
        response = await sayHelloService.sayHello(name="Amplify")
        print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())
