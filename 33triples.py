import math
#co-created with Jedidiah
for a in range(1, 100):
		for b in range(a + 1, 100):
			c = math.sqrt(a**2 + b**2)
			if c % 1 == 0:
				print(a, b, c)
