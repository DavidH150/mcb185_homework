import random

#3D6
method_1 = 0
for e in range(100000):
	for f in range(3):
		method_1 += random.randint(1, 6)
print(f'Method 1 average = {method_1 / 100000}')


#3D6r1 
method_2 = 0
for d in range(100000):
	for b in range(3):
		a = random.randint(1, 6)
		while a == 1: a = random.randint(1, 6)
		method_2 += a
print(f'Method 2 average = {method_2 / 100000}')
	

#3D6x2
method_3 = 0
for b in range(100000):
	for c in range(3):
		p = random.randint(1, 6)
		l = random.randint(1, 6)
		if p > l: method_3 += p
		else:     method_3 += l
print(f'Method 3 average = {method_3 / 100000}')

#4D6d1
method_4 = 0
for a in range(100000):
	k = random.randint(1, 6)
	m = random.randint(1, 6)
	y = random.randint(1, 6)
	r = random.randint(1, 6)
	if   k <= m and k <= y and k <= r: method_4 += (m+y+r)
	elif m <= k and m <= y and m <= r: method_4 += (k+y+r)
	elif y <= m and y <= k and y <= r: method_4 += (m+k+r)
	else: 							   method_4 += (m+k+y)

print(f'Method 4 average = {method_4 / 100000}')


