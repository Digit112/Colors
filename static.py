import sys
import time
import random

while True:
	brightness=str(random.randint(80,245))
	sys.stdout.write("\033[48;2;"+brightness+";"+brightness+";"+brightness+"m ")

