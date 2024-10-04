#!/usr/bin/python3

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
import signal 
import sys
from psonic import *
from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

NOTE1 = 50
NOTE2 = 51
NOTE3 = 52
NOTE4 = 53
NOTE5 = 54
NOTE6 = 55
NOTE7 = 56
NOTE8 = 57

AMP = 100

# set GPIO5 on rising edge
GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# set GPIO6 on rising edge
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# set GPIO13 on rising edge
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# set GPIO19 on rising edge
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# set GPIO26 on rising edge
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# set GPIO16 on rising edge
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# set GPIO20 on rising edge
GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# set GPIO21 on rising edge
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# callbacks functions 
def callback5(channel):
	sender.send_message('/trigger/propjet',[NOTE1,AMP,8])
def callback6(channel):
	sender.send_message('/trigger/propjet',[NOTE2,AMP,8])
def callback13(channel):
	sender.send_message('/trigger/propjet',[NOTE3,AMP,8])
def callback19(channel):	
	sender.send_message('/trigger/propjet',[NOTE4,AMP,8])
def callback26(channel):
	sender.send_message('/trigger/propjet',[NOTE5,AMP,8])
def callback16(channel):
	sender.send_message('/trigger/propjet',[NOTE6,AMP,8])
def callback20(channel):
	sender.send_message('/trigger/propjet',[NOTE7,AMP,8])
def callback21(channel):
	sender.send_message('/trigger/propjet',[NOTE8,AMP,8])


# register callbacks
GPIO.add_event_detect(5,GPIO.RISING,callback=callback5,bouncetime=100)
GPIO.add_event_detect(6,GPIO.RISING,callback=callback6,bouncetime=100)
GPIO.add_event_detect(13,GPIO.RISING,callback=callback13,bouncetime=100)
GPIO.add_event_detect(19,GPIO.RISING,callback=callback19,bouncetime=100)
GPIO.add_event_detect(26,GPIO.RISING,callback=callback26,bouncetime=100)
GPIO.add_event_detect(16,GPIO.RISING,callback=callback16,bouncetime=100)
GPIO.add_event_detect(20,GPIO.RISING,callback=callback20,bouncetime=100)
GPIO.add_event_detect(21,GPIO.RISING,callback=callback21,bouncetime=100)

# handle ctrl+c
def signal_handler(signal, frame):
	print("sigkill")
	GPIO.cleanup() # clean GPIOS
	print("GPIOS cleaned")
	sys.exit(0)

# main code 
if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_handler)
	# make some noise when system started
	sender.send_message('/trigger/propjet',[NOTE1,AMP,8])
	time.sleep(0.07)
	sender.send_message('/trigger/propjet',[NOTE2,AMP,8])
	time.sleep(0.07)
	sender.send_message('/trigger/propjet',[NOTE3,AMP,8])
	time.sleep(0.07)
	sender.send_message('/trigger/propjet',[NOTE4,AMP,8])
	time.sleep(0.07)
	sender.send_message('/trigger/propjet',[NOTE5,AMP,8])
	time.sleep(0.07)
	sender.send_message('/trigger/propjet',[NOTE6,AMP,8])
	time.sleep(0.07)
	sender.send_message('/trigger/propjet',[NOTE7,AMP,8])
	time.sleep(0.07)
	sender.send_message('/trigger/propjet',[NOTE8,AMP,8])
	while True:
		time.sleep(0.001)
		