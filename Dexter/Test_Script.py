import socket
import time

########## Jason Notes #########
# +-334000 seems to be about 90 degrees for joints
# +-3711 (334000/90) per degree

#'M x y z xtheta ytheta ztheta right_arm elbow_up wrist_out
#b before string denotes bytes
#first four parameters are not used for arm command - probably just used by DDE
#'a theta1 theta2 theta3 theta4 theta5'


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

# dexter.close()  # this ends the connection

#coordinates are in micrometers - so x = 100000 will be x = .1 meters

#nx = 5
#ny = 5
#step = 5 * 1000
#points = []
#zero = [0, 500000, -100000]
#topLeft = [zero[0]-0.5*step*(nx-1), zero[1]+0.5*step*(ny-1), zero[2]]   # Generate top left point of grid
# Generate the grid points for Dexter to move to -> This makes an S pattern,
# I can make it have different cases if we want to always go left to right or whatever

#for i in range(int(float(ny))):                # Number of rows
#    for j in range(int(float(nx))):            # Number of columns
#        if i % 2 == 0:             # Check to see if row number is even
#            points.append([round(topLeft[0]+j*step, -2), round(topLeft[1]-i*step, -2), round(topLeft[2], -2)])
#        else:                      # If the row is odd, move right to left
#            points.append([round(topLeft[0] + (nx-1)*step - j*step, -2), round(topLeft[1]-i*step, -2),
#                           round(topLeft[2], -2)])


def moveTo(coords):
    # This way of encoding works!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #dexter.send(b'xxx xxx xxx xxx M %(x)d %(y)d %(z)d 0 0 -1 1 1 1;'%{b'x':coords[0], b'y':coords[1], b'z':coords[2]})

    print(b'xxx xxx xxx xxx M %(x)d %(y)d %(z)d 0 0 -1 1 1 1;'%{b'x':coords[0], b'y':coords[1], b'z':coords[2]})

def moveToHigh(coords):
    #dexter.send(b'xxx xxx xxx xxx M %(x)d %(y)d %(z)d 0 0 -1 1 1 1;' % {b'x': coords[0], b'y': coords[1], b'z': coords[2]+10000})
    print(b'xxx xxx xxx xxx M %(x)d %(y)d %(z)d 0 0 -1 1 1 1;' % {b'x': coords[0], b'y': coords[1], b'z': coords[2]+10000})

def moveToHigh():
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

# Move to start position (top left of grid):

moveToHigh()

#for i in range(len(points)):
#    moveToHigh(points[i])
#    time.sleep(0.5)
#    moveTo(points[i])
#    time.sleep(2)
#    moveToHigh(points[i])
#    time.sleep(0.5)
    # proceed = ''
    # while proceed != 'y':
    #    proceed = input('When ready to continue to next point, type y and press enter: ')

print('Exiting...')
dexter.close()
