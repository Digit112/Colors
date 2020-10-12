import sys
import time
import os
import random

def regulate(tup):
	lis = list(tup)
	for i in range(0, len(tup)):
		if lis[i] > 255:
			lis[i] = 255
		elif lis[i] < 0:
			lis[i] = 0
	return tuple(lis)
mod = 5

while True:
	line = []

	red = 125
	green = 125
	blue = 125

	line.append((125, 125, 125))

	for i in range(1, 250):
		line.append(regulate((line[i-1][0]+random.randint(-mod, mod), line[i-1][1]+random.randint(-mod, mod), line[i-1][2]+random.randint(-mod, mod))))

	time.sleep(.05)

	rows, columns = os.popen('stty size', 'r').read().split()

	for i in range(0, int(columns)):
		sys.stdout.write("\033[48;2;"+str(line[i][0])+";"+str(line[i][1])+";"+str(line[i][2])+"m ")

