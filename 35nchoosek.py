import math
import sys

def nck(n, k):
	return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

print(nck(4, 2))