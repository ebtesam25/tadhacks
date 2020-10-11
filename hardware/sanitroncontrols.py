import pygame
import time
import random
import serial


command = sys.argv[1]

ser = serial.Serial('/dev/ttyACM0', 115200)

# ser = serial.Serial('COM24', 115200)


print ("connected to: " + ser.portstr)

serialmsg = b''
 

def send_messageU():
    ser.flush()
    ser.write(b'U')
    ser.write(b'\n')
    

def send_messageu():
    ser.flush()
    ser.write(b'u')
    ser.write(b'\n')

def send_messageH():
    ser.flush()
    ser.write(b'H')

def send_messageh():
    ser.flush()
    ser.write(b'h')

if command = 'on':
    send_messageU()
    send_messageH()
    

if command = 'off':
    send_messageu()
    send_messageh()




ser.close()
quit()
        
