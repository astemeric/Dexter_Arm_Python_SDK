from __future__ import print_function
import socket
import time
import threading
import logging
import grpc
from concurrent import futures
import robot_arm_pb2
import robot_arm_pb2_grpc
import configuration_update_pb2
import configuration_update_pb2_grpc

#####!!!!#####

########## Jason Notes #########
# +-334000 seems to be about 90 degrees for joints
# +-3711 (334000/90) per degree
#coordinates are in micrometers - so x = 100000 will be x = .1 meters

#'M x y z xtheta ytheta ztheta right_arm elbow_up wrist_out
#b before string denotes bytes
#first four parameters are not used for arm command - probably just used by DDE
#'a theta1 theta2 theta3 theta4 theta5'


########## Old Notes ###########
#The old notes are useless now in my opinion

class ConfigurationUpdate(configuration_update_pb2_grpc.ConfigurationUpdateServicer):

    def SendUpdate(self, request, context):
        dexter.send(b'xxx xxx xxx xxx g;')
        status = dexter.recv(bufferSize)
        jointList = convertMessage(status)

        note, these two should be the same data
        joint1_Curr = jointList[12]/degree
        joint1_Goal = jointList[16]/degree
        joint2_Curr = jointList[22]/degree
        joint2_Goal = jointList[26]/degree
        joint3_Curr = jointList[32]/degree
        joint3_Goal = jointList[36]/degree
        joint4_Curr = jointList[42]/degree
        joint4_Goal = jointList[46]/degree
        joint5_Curr = jointList[52]/degree
        joint5_Goal = jointList[56]/degree

        JointMessage = robot_arm_pb2.robotConfiguration()
        JointMessage.j1.currentAngle = joint1_Curr
        JointMessage.j1.goalAngle = joint1_Goal
        JointMessage.j2.currentAngle = joint2_Curr
        JointMessage.j2.goalAngle = joint2_Goal
        JointMessage.j3.currentAngle = joint3_Curr
        JointMessage.j3.goalAngle = joint3_Goal
        JointMessage.j4.currentAngle = joint4_Curr
        JointMessage.j4.goalAngle = joint4_Goal
        JointMessage.j5.currentAngle = joint5_Curr
        JointMessage.j5.goalAngle = joint5_Goal

        return JointMessage

    def Move5(self, request, context):

        angle1 = request.j1
        angle2 = request.j2
        angle3 = request.j3
        angle4 = request.j4
        angle5 = request.j5

        if request.commandType == robot_arm_pb2.P_MOVE:
            sendSuccess = move_p5(angle1, angle2, angle3, angle4, angle5)
        elif request.commandType == robot_arm_pb2.A_MOVE:
            sendSuccess = move_a5(angle1, angle2, angle3, angle4, angle5)
        else:
            sendSuccess = -1

        robotStatus = robot_arm_pb2.currentStatus()
        robotStatus.status = sendSuccess
        return robotStatus

    def Move7(self, request, context):

        angle1 = request.j1
        angle2 = request.j2
        angle3 = request.j3
        angle4 = request.j4
        angle5 = request.j5
        angle6 = request.j6
        angle7 = request.j7

        moveType = ''
        if request.MoveType == P_MOVE:
            sendSuccess = move_p7(angle1, angle2, angle3, angle4, angle5, angle6, angle7)
        elif request.MoveType == A_MOVE:
            sendSuccess = move_a7(angle1, angle2, angle3, angle4, angle5, angle6, angle7)
        else:
            sendSuccess = -1

        robotStatus = currentStatus()
        robotStatus.status = sendSuccess
        return robotStatus

def connect():
    # Connect to Dexter to send it commands

    dex_ip = '192.168.1.142'
    dex_port = 50000

    global dexter
    dexter = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dexter.connect((dex_ip, dex_port))

#send in the thetas in terms of degrees
def move_a5(theta1, theta2, theta3, theta4, theta5):

    if abs(theta1) < 180 and abs(theta2) < 180 and abs(theta3) < 180 and abs(theta4) < 180 and abs(theta5) < 180:

        theta1 = theta1 * degree
        theta2 = theta2 * degree
        theta3 = theta3 * degree
        theta4 = theta4 * degree
        theta5 = theta5 * degree

        dexter.send(b'xxx xxx xxx xxx a %(t1)d %(t2)d %(t3)d %(t4)d %(t5)d;'%{b't1':theta1, b't2':theta2, b't3':theta3, b't4':theta4, b't5':theta5})
        status = dexter.recv(bufferSize)
        #print(b'xxx xxx xxx xxx a %(t1)d %(t2)d %(t3)d %(t4)d %(t5)d;'%{b't1':theta1, b't2':theta2, b't3':theta3, b't4':theta4, b't5':theta5})

        sendSuccess = 1

    else:
        print("Please send in a valid theta value in terms of degrees")
        sendSuccess = -1



    return sendSuccess

#send in the thetas in terms of degrees
def move_a7(theta1, theta2, theta3, theta4, theta5, theta6, theta7):

    if abs(theta1) < 180 and abs(theta2) < 180 and abs(theta3) < 180 and abs(theta4) < 180 and abs(theta5) < 180 and abs(theta6) < 1024 and abs(theta7) < 700:

        theta1 = theta1 * degree
        theta2 = theta2 * degree
        theta3 = theta3 * degree
        theta4 = theta4 * degree
        theta5 = theta5 * degree
        theta6 = theta6 * degree
        theta7 = theta7 * degree

        if theta7 < 125:
            theta7 = 125

        dexter.send(b'xxx xxx xxx xxx a %(t1)d %(t2)d %(t3)d %(t4)d %(t5)d %(t6)d %(t7)d;'%{b't1':theta1, b't2':theta2, b't3':theta3, b't4':theta4, b't5':theta5, b't6':theta6, b't7':theta7})
        status = dexter.recv(bufferSize)
        #print(b'xxx xxx xxx xxx a %(t1)d %(t2)d %(t3)d %(t4)d %(t5)d %(t6)d %(t7)d;'%{b't1':theta1, b't2':theta2, b't3':theta3, b't4':theta4, b't5':theta5, b't6':theta6, b't7':theta7})

        sendSuccess = 1

    else:
        print("Please send in a valid theta value in terms of degrees")
        sendSuccess = -1

    return sendSuccess

def move_End_Effector(theta6, theta7):

    if abs(theta6) < 1024 and abs(theta7) < 700:

        if theta7 < 125:
            theta7 = 125

        dexter.send(b'xxx xxx xxx xxx a 0 0 0 0 0 %(t6)d %(t7)d;'%{b't6':theta6, b't7':theta7})
        status = dexter.recv(bufferSize)
        #print(b'xxx xxx xxx xxx a 0 0 0 0 0 %(t6)d %(t7)d;'%{b't6':theta6, b't7':theta7})

        sendSuccess = 1

    else:
        print("Please send in a valid theta value in terms of degrees")
        sendSuccess = -1

    return sendSuccess

#send in the thetas in terms of degrees
def move_p5(theta1, theta2, theta3, theta4, theta5):

    if abs(theta1) < 180 and abs(theta2) < 180 and abs(theta3) < 180 and abs(theta4) < 180 and abs(theta5) < 180:

        theta1 = theta1 * degree
        theta2 = theta2 * degree
        theta3 = theta3 * degree
        theta4 = theta4 * degree
        theta5 = theta5 * degree

        dexter.send(b'xxx xxx xxx xxx P %(t1)d %(t2)d %(t3)d %(t4)d %(t5)d;'%{b't1':theta1, b't2':theta2, b't3':theta3, b't4':theta4, b't5':theta5})
        status = dexter.recv(bufferSize)
        #print(b'xxx xxx xxx xxx P %(t1)d %(t2)d %(t3)d %(t4)d %(t5)d;'%{b't1':theta1, b't2':theta2, b't3':theta3, b't4':theta4, b't5':theta5})

        sendSuccess = 1

    else:
        print("Please send in a valid theta value in terms of degrees")
        sendSuccess = -1

    return sendSuccess

#send in the thetas in terms of degrees
def move_p7(theta1, theta2, theta3, theta4, theta5, theta6, theta7):

    if abs(theta1) < 180 and abs(theta2) < 180 and abs(theta3) < 180 and abs(theta4) < 180 and abs(theta5) < 180 and abs(theta6) < 1024 and abs(theta7) < 700:

        theta1 = theta1 * degree
        theta2 = theta2 * degree
        theta3 = theta3 * degree
        theta4 = theta4 * degree
        theta5 = theta5 * degree
        theta6 = theta6 * degree
        theta7 = theta7 * degree

        if theta7 < 125:
            theta7 = 125

        dexter.send(b'xxx xxx xxx xxx P %(t1)d %(t2)d %(t3)d %(t4)d %(t5)d %(t6)d %(t7)d;'%{b't1':theta1, b't2':theta2, b't3':theta3, b't4':theta4, b't5':theta5, b't6':theta6, b't7':theta7})
        status = dexter.recv(bufferSize)
        #print(b'xxx xxx xxx xxx P %(t1)d %(t2)d %(t3)d %(t4)d %(t5)d %(t6)d %(t7)d;'%{b't1':theta1, b't2':theta2, b't3':theta3, b't4':theta4, b't5':theta5, b't6':theta6, b't7':theta7})

        sendSuccess = 1

    else:
        print("Please send in a valid theta value in terms of degrees")
        sendSuccess = -1

    return sendSuccess

#Used to convert the byte object to  4byte integer objects
#When sending a command, the return value will be the current robot status
#So the status object will contain all of the information in a byte array
#But we can't glean information from a byte array without
#Decoding it to an int array using ConverMessage(status)
def convertMessage(byte_Status):
    finalList = [None]*60

    #Byte array is Big Endian, so the 0th byte will represent the
    #lower 256 bits and the 3rd byte will represent the top bits
    byte0 = 1
    byte1 = 2**8
    byte2 = 2**16
    byte3 = 2**24

    #Convert the byte list into an int list
    for x in range (0, 60):
        twos_comp_flag = 0

        #Determine the current offset
        offset0 = x*4
        offset1 = x*4+1
        offset2 = x*4+2
        offset3 = x*4+3

        #Since the first byte determines whether the signed int is + or -
        #Check if the first bit is 1 (since 1 byte = 256 potential values,
        #check if the first byte is at least 256/2)
        if byte_Status[offset3] > 127:
            twos_comp_flag = 1

        #save the data from the byte array for manipulation
        byteStatus0 = byte_Status[offset0]
        byteStatus1 = byte_Status[offset1]
        byteStatus2 = byte_Status[offset2]
        byteStatus3 = byte_Status[offset3]

        #Multiply the values by the offsets to determine int values
        value0 = byteStatus0 * byte0
        value1 = byteStatus1 * byte1
        value2 = byteStatus2 * byte2
        value3 = byteStatus3 * byte3

        #add them all together
        finalValue = value0+value1+value2+value3

        #If negative, set negative
        if twos_comp_flag == 1:
            finalValue = finalValue - 0xFFFFFFFF

        #update values
        finalList[x] = finalValue

    #finalList now contains all of the status values

    #printCurrentStatus(finalList)

    return finalList

#Function to receive status updates
#Note - we're using the same socket to send!
#If we increase the update rate, we will run into race conditions
#Will need to add a mutex soon
def GRPCServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    configuration_update_pb2_grpc.add_ConfigurationUpdateServicer_to_server(ConfigurationUpdate(), server)
    #can add a secure port later
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

# Connect to Dexter:
if __name__ == "__main__":
    global bufferSize
    global degree
    degree = 3600


    number_of_addresses = 64
    size_of_data = 4 #bytes
    bufferSize = number_of_addresses * size_of_data

    connect()
    GRPCServer()

    print('Exiting...')
    dexter.close()
