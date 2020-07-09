import logging
import grpc
import robot_arm_pb2
import robot_arm_pb2_grpc
import dexter_update_pb2
import dexter_update_pb2_grpc

class DexterClient:

    def __init__(self,ip='127.0.0.1',port=50051):
        self.ip = ip
        self.port = port
        self.ip_port = ip+':'+str(port)

    def move_P5(self, theta1, theta2, theta3, theta4, theta5):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = dexter_update_pb2_grpc.DexterUpdateStub(channel)
            moveRequest = robot_arm_pb2.dexterRequest5()

            moveRequest.j1 = theta1
            moveRequest.j2 = theta2
            moveRequest.j3 = theta3
            moveRequest.j4 = theta4
            moveRequest.j5 = theta5
            moveRequest.commandType = robot_arm_pb2.P_MOVE

            response = stub.Move5(moveRequest)

        return 1

    def move_P7(self, theta1, theta2, theta3, theta4, theta5, theta6, theta7):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = dexter_update_pb2_grpc.DexterUpdateStub(channel)
            moveRequest = robot_arm_pb2.dexterRequest7()

            moveRequest.j1 = theta1
            moveRequest.j2 = theta2
            moveRequest.j3 = theta3
            moveRequest.j4 = theta4
            moveRequest.j5 = theta5
            moveRequest.j6 = theta6
            moveRequest.j7 = theta7
            moveRequest.commandType = robot_arm_pb2.P_MOVE

            response = stub.Move7(moveRequest)
        return 1

    def move_a5(self, theta1, theta2, theta3, theta4, theta5):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = dexter_update_pb2_grpc.DexterUpdateStub(channel)
            moveRequest = robot_arm_pb2.dexterRequest5()

            moveRequest.j1 = theta1
            moveRequest.j2 = theta2
            moveRequest.j3 = theta3
            moveRequest.j4 = theta4
            moveRequest.j5 = theta5
            moveRequest.commandType = robot_arm_pb2.A_MOVE

            response = stub.Move5(moveRequest)
        return 1

    def move_a7(self, theta1, theta2, theta3, theta4, theta5, theta6, theta7):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = dexter_update_pb2_grpc.DexterUpdateStub(channel)
            moveRequest = robot_arm_pb2.dexterRequest7()

            moveRequest.j1 = theta1
            moveRequest.j2 = theta2
            moveRequest.j3 = theta3
            moveRequest.j4 = theta4
            moveRequest.j5 = theta5
            moveRequest.j6 = theta6
            moveRequest.j7 = theta7
            moveRequest.commandType = robot_arm_pb2.A_MOVE

            response = stub.Move7(moveRequest)
        return 1

    def statusUpdate(self):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = configuration_update_pb2_grpc.ConfigurationUpdateStub(channel)
            response = stub.SendUpdate(robot_arm_pb2.dexterStatus(status = 1))

            status = [None,None,None,None,None,None,None,None,None,None]
            status[0] = response.j1.currentAngle
            status[1] = response.j1.goalAngle
            status[2] = response.j2.currentAngle
            status[3] = response.j2.goalAngle
            status[4] = response.j3.currentAngle
            status[5] = response.j3.goalAngle
            status[6] = response.j4.currentAngle
            status[7] = response.j4.goalAngle
            status[8] = response.j5.currentAngle
            status[9] = response.j5.goalAngle

            return status
