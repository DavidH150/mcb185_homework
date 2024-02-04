import math

def poisson(k, n):
	return ((n ** k) * (math.e ** -n)) / math.factorial(k)

print(poisson(1, 0.5))