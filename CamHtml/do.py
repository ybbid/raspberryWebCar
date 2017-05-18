#!/usr/bin/python3
import sys
import serial
ser = serial.Serial('/dev/ttyAMA0',         # Device name varies
        baudrate=9600,         # Set baud rate  to 38400
        bytesize=8,
        parity='N',
        stopbits=1)
if len(sys.argv) < 2:
    print("ERROR ARGV")
    sys.exit()
#MSP430命令
cmd = ""
#摄像头向上移动
if str(sys.argv[1])=="cam_up":
    cmd = "w"
#摄像头向下移动
elif str(sys.argv[1])=="cam_down":
    cmd = "s"
#摄像头向左移动
elif str(sys.argv[1])=="cam_left":
    cmd = "a"
#摄像头向右移动
elif str(sys.argv[1])=="cam_right":
    cmd = "d"
else:
    print("ERROR ARGV")
ser.write(cmd.encode('utf-8'))
ser.close()
