import sys
import time
import os
import random
import math

def regulate(tup):
	lis = list(tup)
	for i in range(0, len(tup)):
		if lis[i] > 255:
			lis[i] = 255
		elif lis[i] < 0:
			lis[i] = 0
	return tuple(lis)

sta = 145
mod = 4
if len(sys.argv) > 1:
	if sys.argv[1] == "help" or sys.argv[1] == "-help" or sys.argv[1] == "-h":
		print("Performs 2D Random Walk on 3-tuples and displays them in order as colors in the terminal.")
		print("First argument is starting brightness between 0 and 255,")
		print("Second argument is change in maximum change in each RGB value, per space.")
		exit()
	elif sys.argv[1].isdigit():
		if  int(sys.argv[1]) >= 0 and int(sys.argv[1]) <= 255:
			sta = int(sys.argv[1])
		else:
			print("First argument is starting brightness, value must be an integer between 0 and 255.")
			exit()
	else:
		print("First argument is starting brightness, value must be an integer between 0 and 255.")
		exit()

line = []

red = 125
green = 125
blue = 125

line.append((sta, sta, sta))

for i in range(1, 230):
	line.append(regulate((line[i-1][0]+random.randint(-mod, mod), line[i-1][1]+random.randint(-mod, mod), line[i-1][2]+random.randint(-mod, mod))))

modmod = 0

while True:
	#time.sleep(.04)
	modmod = modmod + math.pi/128

	mod = int(math.sin(modmod) * 6 + 10)
	
	line[0] = regulate((line[0][0]+random.randint(-mod, mod), line[0][1]+random.randint(-mod, mod), line[0][2]+random.randint(-mod, mod)))
	for i in range(1, 230):
		line[i] = regulate(((line[i][0]+line[i-1][0])/2+random.randint(-mod, mod), (line[i][1]+line[i-1][1])/2+random.randint(-mod, mod), (line[i][2]+line[i-1][2])/2+random.randint(-mod, mod)))

	rows, columns = os.popen('stty size', 'r').read().split()
	for i in range(0, int(columns)):
		sys.stdout.write("\033[48;2;"+str(line[i][0])+";"+str(line[i][1])+";"+str(line[i][2])+"m ")

