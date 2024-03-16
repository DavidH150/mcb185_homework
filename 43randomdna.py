import random

seq = 3
for i in range(1, seq + 1):
	print(f'>seq-{i}')
	for s in range(random.randint(50, 60)):
		print(random.choice('ACGT'), end='')
	
	print()

	