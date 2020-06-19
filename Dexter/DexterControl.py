import socket
import time
import threading

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

dex_ip = '192.168.1.142'
dex_port = 50000
number_of_addresses = 64
size_of_data = 4 #bytes
bufferSize = number_of_addresses * size_of_data

def connect():
    # Connect to Dexter to send him commands
    global dexter
    dexter = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dexter.connect((dex_ip, dex_port))

def moveTo(coords):
    # This way of encoding works!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #dexter.send(b'xxx xxx xxx xxx M %(x)d %(y)d %(z)d 0 0 -1 1 1 1;'%{b'x':coords[0], b'y':coords[1], b'z':coords[2]})

    print(b'xxx xxx xxx xxx M %(x)d %(y)d %(z)d 0 0 -1 1 1 1;'%{b'x':coords[0], b'y':coords[1], b'z':coords[2]})

def moveToHigh():
    #When sending a command, the return value will be the current robot status
    dexter.send(b'xxx xxx xxx xxx g;')

    #So the status object will contain all of the information in a byte array
    status = dexter.recv(bufferSize)
    print("\n\nStart:")

    #But we can't glean information from a byte array without
    #Decoding it to an int array
    convertMessage(status)
    time.sleep(1)

    dexter.send(b'1 1 xxx xxx P 167000 0 0 0 0;')
    status = dexter.recv(bufferSize)
    print("Start Result (should be same as start):")
    print("(Cmd 1 just input):")
    convertMessage(status)
    time.sleep(6)

    dexter.send(b'2 1 xxx xxx P -167000 0 0 0 0;')
    status = dexter.recv(bufferSize)
    print("Cmd 1 Result:")
    print("(Cmd 2 just input):")
    convertMessage(status)
    time.sleep(6)

    dexter.send(b'1 2 100 300 P 167000 0 0 0 0;')
    status = dexter.recv(bufferSize)
    print("Cmd 2 Result:")
    print("(Cmd 3 just input):")
    convertMessage(status)
    time.sleep(6)


    dexter.send(b'3 4 600 9999 P 0 0 0 0 0;')
    status = dexter.recv(bufferSize)
    print("Cmd 3 Result:")
    print("(Cmd 4 just input):")
    convertMessage(status)
    time.sleep(6)

    dexter.send(b'xxx xxx xxx xxx g;')
    status = dexter.recv(bufferSize)
    print("Cmd 4 Result (Should be same as Start Result):")
    convertMessage(status)
    time.sleep(6)

#Used to convert the byte object to  4byte integer objects
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
    print("\t\tBASE_POSITION_AT: " + str(joint_Data[0])
    + "\tBASE_POSITION_DELTA: " + str(joint_Data[1])
    + "\tBASE_POSITION_PID_DELTA: " + str(joint_Data[2])
    + "\tBASE_POSITION_FORCE_DELTA: " + str(joint_Data[3])
    + "\tBASE_SIN: " + str(joint_Data[4])
    + "\n\t\tBASE_COS: " + str(joint_Data[5])
    + "\tBASE_MEASURED_ANGLE: " + str(joint_Data[6])
    + "\tSENT_BASE_POSITION: " + str(joint_Data[7])
    + "\tSLOPE_BASE_POSITION: " + str(joint_Data[8])
    + "\tEmpty: " + str(joint_Data[9]) + "\n")

# Connect to Dexter:
connect()
time.sleep(1)

zeroConf = ''
while zeroConf != 'y':
    zeroConf = input('When in place, type y and press enter: ') # User must prompt when Dexter is at proper position

moveToHigh()
#readStatus()

print('Exiting...')
dexter.close()
