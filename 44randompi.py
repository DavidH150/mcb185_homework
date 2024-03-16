import math
import random

total = 0
inside = 0
while True:
	x = random.random()
	y = random.random()
	total += 1
	if math.sqrt(x ** 2 + y ** 2) < 1: inside += 1
	pi = 4 * inside / total 
	print(pi)
