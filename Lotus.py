import sys
import time
import random

while True:
	
	time.sleep(.00025)
	sys.stdout.write("\033[48;2;"+str(230+random.randint(20,20))+";"+str(210+random.randint(-15,15))+";"+str(230+random.randint(-15,15))+"m ")

