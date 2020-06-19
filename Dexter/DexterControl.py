from __future__ import print_function
import socket
import time
import threading
import logging
import grpc
#import helloworld_pb2
#import helloworld_pb2_grpc

#####!!!!#####
#Will need to add a mutex since two threads are sharing the same socket!

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

def connect():
    # Connect to Dexter to send it commands

    dex_ip = '192.168.1.142'
    dex_port = 50000

    global dexter
    dexter = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dexter.connect((dex_ip, dex_port))

    global statusSocket
    statusSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    statusSocket.connect((dex_ip, dex_port))

#send in the thetas in terms of degrees
def move_a5(theta1, theta2, theta3, theta4, theta5):

    if abs(theta1) < 180 and abs(theta2) < 180 and abs(theta3) < 180 and abs(theta4) < 180 and abs(theta5) < 180:

        theta1 = theta1 * degree
        theta2 = theta2 * degree
        theta3 = theta3 * degree
        theta4 = theta4 * degree
        theta5 = theta5 * degree

        dexter.send(b'xxx xxx xxx xxx a %(t1)d %(t2)d %(t3)d %(t4)d %(t5)d;'%{b't1':theta1, b't2':theta2, b't3':theta3, b't4':theta4, b't5':theta5})
        #make sure you read after every send, so we don't clog up the buffer - not sure if Python will hold old messages in the buffer
        status = dexter.recv(bufferSize)

    else:
        print("Please send in a valid theta value in terms of degrees")

#send in the thetas in terms of degrees
def move_a7(theta1, theta2, theta3, theta4, theta5, theta6, theta7):

    if abs(theta1) < 180 and abs(theta2) < 180 and abs(theta3) < 180 and abs(theta4) < 180 and abs(theta5) < 180 and abs(theta6) < 180 and abs(theta7) < 180:

        theta1 = theta1 * degree
        theta2 = theta2 * degree
        theta3 = theta3 * degree
        theta4 = theta4 * degree
        theta5 = theta5 * degree
        theta6 = theta6 * degree
        theta7 = theta7 * degree

        dexter.send(b'xxx xxx xxx xxx a %(t1)d %(t2)d %(t3)d %(t4)d %(t5)d %(t6)d %(t7)d;'%{b't1':theta1, b't2':theta2, b't3':theta3, b't4':theta4, b't5':theta5, b't6':theta6, b't7':theta7})
        status = dexter.recv(bufferSize)

    else:
        print("Please send in a valid theta value in terms of degrees")

#send in the thetas in terms of degrees
def move_p(theta1, theta2, theta3, theta4, theta5):

    if abs(theta1) < 180 and abs(theta2) < 180 and abs(theta3) < 180 and abs(theta4) < 180 and abs(theta5) < 180:

        theta1 = theta1 * degree
        theta2 = theta2 * degree
        theta3 = theta3 * degree
        theta4 = theta4 * degree
        theta5 = theta5 * degree

        dexter.send(b'xxx xxx xxx xxx P %(t1)d %(t2)d %(t3)d %(t4)d %(t5)d;'%{b't1':theta1, b't2':theta2, b't3':theta3, b't4':theta4, b't5':theta5})
        status = dexter.recv(bufferSize)

    else:
        print("Please send in a valid theta value in terms of degrees")


def moveToHigh():


    move_p(-45, 0, 0 ,0 ,0)
    time.sleep(6)

    move_p(45, 0, 0 ,0 ,0)
    time.sleep(6)

    move_p(-45, 0, 0 ,0 ,0)
    time.sleep(6)

    move_p(0, 0, 0 ,0 ,0)
    time.sleep(6)


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

    printCurrentStatus(finalList)

#Function to print out all the joint information
def printCurrentStatus(cur_List):
    #Python sucks - when you try to get a sublist, you have to give it the
    #last index you want + 1

    joint1 = cur_List[10:20]
    printJoint(joint1, 1)
    joint2 = cur_List[20:30]
    printJoint(joint2, 2)
    joint3 = cur_List[30:40]
    printJoint(joint3, 3)
    joint4 = cur_List[40:50]
    printJoint(joint4, 4)
    joint5 = cur_List[50:60]
    printJoint(joint5, 5)
    print("\n")

#Function to print individual joint information
def printJoint(joint_Data, joint_Number):
    print("\tJoint " + str(joint_Number) + ": ")
    print("\t\tBASE_POSITION_AT: " + str(round(joint_Data[0]/degree,2))
    + "\tBASE_POSITION_DELTA: " + str(round(joint_Data[1]/degree,2))
    + "\tBASE_POSITION_PID_DELTA: " + str(round(joint_Data[2]/degree,2))
    + "\tBASE_POSITION_FORCE_DELTA: " + str(round(joint_Data[3],2))
    + "\tBASE_SIN: " + str(joint_Data[4])
    + "\n\t\tBASE_COS: " + str(joint_Data[5])
    + "\tBASE_MEASURED_ANGLE: " + str(round(joint_Data[6]/degree,2))
    + "\tSENT_BASE_POSITION: " + str(round(joint_Data[7]/degree*-4.05,2))
    + "\tSLOPE_BASE_POSITION: " + str(round(joint_Data[8],2))
    + "\tEmpty: " + str(joint_Data[9]) + "\n")

#Function to receive status updates
#Note - we're using the same socket to send!
#If we increase the update rate, we will run into race conditions
#Will need to add a mutex soon
def receiveStatusUpdate():
    while threadStopped == 0:
        print("Thread Update")
        dexter.send(b'xxx xxx xxx xxx g;')
        status = dexter.recv(bufferSize)
        convertMessage(status)
        time.sleep(.3)


# Connect to Dexter:

if __name__ == "__main__":
    global bufferSize
    global threadStopped
    global degree
    degree = 3711
    threadStopped = 0

    number_of_addresses = 64
    size_of_data = 4 #bytes
    bufferSize = number_of_addresses * size_of_data

    connect()
    time.sleep(1)

    zeroConf = ''
    while zeroConf != 'y':
        zeroConf = input('When in place, type y and press enter: ') # User must prompt when Dexter is at proper position

    updateStatus = threading.Thread(target = receiveStatusUpdate, args=())
    updateStatus.start()

    print("Moving...")

    moveToHigh()
    #thread is not holding critical resource, so we're good
    threadStopped = 1

    print('Exiting...')
    dexter.close()
