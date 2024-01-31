import math
import sys

def quadraticsolver(a, b, c):
	if (b**2)-(4*a*c) < 0:  sys.exit('Can not take sqrt of values less than 0')
	x1 = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a)
	x2 = (-b - math.sqrt((b**2)-(4*a*c)))/(2*a)
	return x1, x2


print('x1, x2', quadraticsolver(2, 60, 3))
print('x1, x2', quadraticsolver(4, 79, 30))
print('x1, x2', quadraticsolver(3, 6, 9))