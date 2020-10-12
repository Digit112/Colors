import sys
import time
import math
import random

a = 0

sys.stdout.write("\033[38;2;230;230;255m ")

while True:
	if random.randint(0,40) == 0 and a == 0:
		sys.stdout.write("\033[48;2;"+str(40+random.randint(-7,10))+";"+str(140+random.randint(-25,30))+";"+str(230+random.randint(-20,25))+"m ")
		a = 1
	else:
		sys.stdout.write("\033[48;2;"+str(180+random.randint(-5,5))+";"+str(200+random.randint(-5,5))+";"+str(240+random.randint(-5,5))+"m ")
		a = 0

	time.sleep(0.0003)

