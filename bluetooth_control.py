import bluetooth
import time
import RPi.GPIO as GPIO

m11=18
m12=23
m21=24
m22=25
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.output(m11 , 0)
GPIO.output(m12 , 0)
GPIO.output(m21, 0)
GPIO.output(m22, 0)

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
 
client_socket,address = server_socket.accept()
print "Accepted connection from ",address



def forward():
   print "FORWARD"
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 0)
   time.sleep(.5)
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)

def left():
   print "LEFT"
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 1)
   time.sleep(.5)
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 0)

def right():
   print "RIGHT"

   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
   time.sleep(.5)
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)

def reverse():
   print "BACKWARD"
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 1)

def stop():
   print "STOP"
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 0)
 
data=""
while 1:
         data= client_socket.recv(1024)
         print "Received: %s" % data
         if (data == "f"):    
            forward()
         elif (data == "l"):    
            left()
         elif (data == "r"):    
            right()
         elif (data == "b"):    
            reverse()
         elif (data == "s"):
            stop()
         elif (data == "q"):
            print ("Quit")
            break
client_socket.close()
server_socket.close()