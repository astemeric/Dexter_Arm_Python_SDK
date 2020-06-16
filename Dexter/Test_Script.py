import socket
import time

########## Jason Notes #########
# +-334000 seems to be about 90 degrees for joints
# +-3711 (334000/90) per degree

#b before string denotes bytes
#first four parameters are not used for arm command - probably just used by DDE - which is why they are 'xxx xxx xxx xxx'
#'M x y z xtheta ytheta ztheta right_arm elbow_up wrist_out
#'a theta1 theta2 theta3 theta4 theta5'
#coordinates are in micrometers - so x = 100000 will be x = .1 meters

########## Old Notes ###########
# dexter.connect((dex_ip, dex_port))  # not really sure when I need to do this, can i keep the connection open the
# whole time? What's necessary here
# dexter.send(b'xx xx xx xx g;')       # will see the format of this string from Sam's code, send speed! - This seems
# to make dexter stop listening to commands!
# dexStatus = dexter.recv(bufferSize)
# dexter.close()
# Move to straight: Currently not working, machine does nothing, and stops listening, and refuses connections until restarted
# dexter.send(b'xxx xxx xxx xxx T 50000 100000 500000 75000 0 0 -1 1 1 1 -100000 500000 75000 0 0 -1 1 1 1;')
# Move to: this has been working consistently, even a bunch in a row
# dexter.send(b'xxx xxx xxx xxx M 0 500000 75000 0 0 -1 1 1 1;')

dex_ip = '192.168.1.142'
dex_port = 50000

def connect():
    # Connect to Dexter to send him commands
    global dexter
    dexter = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dexter.connect((dex_ip, dex_port))

#ignore
def moveTo(coords):
    #dexter.send(b'xxx xxx xxx xxx M %(x)d %(y)d %(z)d 0 0 -1 1 1 1;'%{b'x':coords[0], b'y':coords[1], b'z':coords[2]})
    #print(b'xxx xxx xxx xxx M %(x)d %(y)d %(z)d 0 0 -1 1 1 1;'%{b'x':coords[0], b'y':coords[1], b'z':coords[2]})

def move():
    #dexter.send(b'xxx xxx xxx xxx M 0 500000 100000 0 0 -1 1 1 1;')
    dexter.send(b'xxx xxx xxx xxx a 0 167000 -167000 0 0;')
    time.sleep(1)
    dexter.send(b'xxx xxx xxx xxx a 0 -167000 -334000 0 0;')
    time.sleep(1)
    dexter.send(b'xxx xxx xxx xxx a -334000 -167000 167000 0 0;')
    time.sleep(1)
    dexter.send(b'xxx xxx xxx xxx a 0 0 0 0 0;')
    time.sleep(1)


# Connect to Dexter:
connect()
# Initial move to zero position
time.sleep(1)
#moveTo(zero)

#print('Move the transducer to the center of the treatment point')
zeroConf = ''
while zeroConf != 'y':
    zeroConf = input('When in place, type y and press enter: ') # User must prompt when Dexter is at proper position

move()

print('Exiting...')
dexter.close()
