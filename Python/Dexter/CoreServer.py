from __future__ import print_function
from concurrent import futures
from DexterServer import DexterServer
import time
import logging
import threading
import grpc
import dexter_update_pb2
import dexter_update_pb2_grpc


class CoreServer:

    #def __init__(self):

    def StartDexterServer(self, port=50051):
        dexterPort = '[::]:'+str(port)
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        dexter_update_pb2_grpc.add_DexterUpdateServicer_to_server(DexterServer(), server)
        #can add a secure port later
        server.add_insecure_port(dexterPort)
        print('Starting Dexter Server...')
        server.start()
        server.wait_for_termination()
