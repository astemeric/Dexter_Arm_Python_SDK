from __future__ import print_function
import logging
import threading
import grpc
import robot_arm_pb2
import robot_arm_pb2_grpc
import configuration_update_pb2
import configuration_update_pb2_grpc
import time

def statusThread():
    global threadStopped
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    # may need to make this asynchronous???
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        while threadStopped == 0:
            stub = configuration_update_pb2_grpc.ConfigurationUpdateStub(channel)
            response = stub.SendUpdate(robot_arm_pb2.currentStatus(status = 1))

            printJoint(response.j1.currentAngle, response.j1.goalAngle, "Joint1")
            printJoint(response.j2.currentAngle, response.j2.goalAngle, "Joint2")
            printJoint(response.j3.currentAngle, response.j3.goalAngle, "Joint3")
            printJoint(response.j4.currentAngle, response.j4.goalAngle, "Joint4")
            printJoint(response.j5.currentAngle, response.j5.goalAngle, "Joint5")
            time.sleep(1)

#put in the control loop here
def commandThread():
    global threadStopped

    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        while threadStopped == 0:
            stub = configuration_update_pb2_grpc.ConfigurationUpdateStub(channel)
            moveRequest = robot_arm_pb2.moveRequest5()

            moveRequest.j1 = 45
            moveRequest.j2 = 0
            moveRequest.j3 = 0
            moveRequest.j4 = 0
            moveRequest.j5 = 0
            moveRequest.commandType = robot_arm_pb2.P_MOVE

            response = stub.Move5(moveRequest)

            time.sleep(waitTime)

def printJoint(current_angle, goal_angle, joint_Number):
    print("\tJoint " + str(joint_Number) + ": ")
    print("\t\tCURRENT_ANGLE: " + str(round(current_angle,2))
    + "\tGOAL_ANGLE: " + str(round(goal_angle,2)))

def interruptListener():
    global threadStopped

    stopClient = 'qpwoienrqwoeprj'
    while stopClient == 'qpwoienrqwoeprj':
        stopClient = input('Click enter to exit: ')

    threadStopped = 1

if __name__ == '__main__':
    global threadStopped
    global hertz
    global waitTime

    threadStopped = 0
    hertz = 1
    waitTime = 1/hertz

    logging.basicConfig()
    statusClient = threading.Thread(target = statusThread, args=())
    statusClient.start()
    commandClient = threading.Thread(target = commandThread, args=())
    commandClient.start()

    interruptListener()
