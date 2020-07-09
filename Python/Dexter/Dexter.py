import socket

class Dexter:

    def __init__(self, ip='192.168.199.142', port=50000):
        self.ip = ip
        self.port = port
        self.isConnected = False

        #class variables - like static variables? Not sure Python...
        self.degree = 3600
        self.bufferSize = 256 #rounded up number of addresses * bytes per address
        self.bounds = (-186.1, 186.1, -97.2, 97.2, -158.3, 158.3, -108.3, 108.3, -190, 190) #joint bounds in self.degrees - contained within DexRun

    def connect(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.ip, self.port))
        self.isConnected = True

    def move_P5(self, theta1, theta2, theta3, theta4, theta5):
        self.__command5('P', theta1, theta2, theta3, theta4, theta5)
        return 1

    def move_P7(self, theta1, theta2, theta3, theta4, theta5, theta6, theta7):
        self.__command7('P', theta1, theta2, theta3, theta4, theta5, theta6, theta7)
        return 1

    def move_a5(self, theta1, theta2, theta3, theta4, theta5):
        self.__command5('a', theta1, theta2, theta3, theta4, theta5)
        return 1

    def move_a7(self, theta1, theta2, theta3, theta4, theta5, theta6, theta7):
        self.__command7('a', theta1, theta2, theta3, theta4, theta5, theta6, theta7)
        return 1

    def update(self):
        status = self.__command('g')
        jointList = self.__convertStatus(status)

        joint1_Curr = jointList[12]/self.degree
        joint1_Goal = jointList[16]/self.degree
        joint2_Curr = jointList[22]/self.degree
        joint2_Goal = jointList[26]/self.degree
        joint3_Curr = jointList[32]/self.degree
        joint3_Goal = jointList[36]/self.degree
        joint4_Curr = jointList[42]/self.degree
        joint4_Goal = jointList[46]/self.degree
        joint5_Curr = jointList[52]/self.degree
        joint5_Goal = jointList[56]/self.degree

        jointData = [joint1_Curr, joint1_Goal,joint2_Curr, joint2_Goal,joint3_Curr, joint3_Goal,joint4_Curr, joint4_Goal,joint5_Curr, joint5_Goal]

        return jointData

    def __command(self, type):
        commandString = 'xxx xxx xxx xxx '+type+';'
        byteString = bytes(commandString, 'utf-8')
        self.connection.send(byteString)
        status = self.connection.recv(self.bufferSize)
        return status

    #no return value
    def __command5(self, type, var1, var2, var3, var4, var5):
        var1 = var1 * self.degree
        var2 = var2 * self.degree
        var3 = var3 * self.degree
        var4 = var4 * self.degree
        var5 = var5 * self.degree
        commandString = 'xxx xxx xxx xxx '+type+' '+str(var1)+' '+str(var2)+' '+str(var3)+' '+str(var4)+' '+str(var5)+';'
        byteString = bytes(commandString, 'utf-8')
        self.connection.send(byteString)
        status = self.connection.recv(self.bufferSize) #I have this here, just because I'm not sure how Python flushes the buffer

    def __command7(self, type, var1, var2, var3, var4, var5, var6, var7):
        var1 = var1 * self.degree
        var2 = var2 * self.degree
        var3 = var3 * self.degree
        var4 = var4 * self.degree
        var5 = var5 * self.degree
        var6 = var6 * self.degree
        var7 = var7 * self.degree
        commandString = 'xxx xxx xxx xxx '+type+' '+str(var1)+' '+str(var2)+' '+str(var3)+' '+str(var4)+' '+str(var5)+' '+str(var6)+' '+str(var7)+';'
        byteString = bytes(commandString, 'utf-8')
        self.connection.send(byteString)
        status = self.connection.recv(self.bufferSize)

    def __convertStatus(self, byteStatus):
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
