import sys
import time
import math

Tint = 0

increment = 1;
tdelta = increment / 720.0;

while True:
	redf = 0.0
	greenf = 0.0
	bluef = 0.0

	redf = int((math.sin((Tint * 360) / 180 * math.pi) + 1) / 2 * 255)
	greenf = int((math.sin((Tint * 360 + 120) / 180 * math.pi) + 1) / 2 * 255)
	bluef = int((math.sin((Tint * 360 + 240) / 180 * math.pi) + 1) / 2 * 255)

	Tint = Tint + tdelta
	if Tint > 1:
		Tint = Tint - 1
	
	time.sleep(.02)
	
	sys.stdout.write("\033[48;2;"+str(redf)+";"+str(greenf)+";"+str(bluef)+"m\n")

