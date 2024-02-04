sign = 1
pi = 3

for i in range(1, 1000):
	n = 2 * i
	if sign: pi = pi + 4 / (n * (n+1) * (n+2))
	else:     pi = pi - 4 / (n * (n+1) * (n+2))
	print(n, n+1, n+2, sign, pi)
	sign = not sign