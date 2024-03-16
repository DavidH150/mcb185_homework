#Authors: David, Jed
import random 

dies = 0
stabilizes = 0
revive = 0

for a in range(100000):
	fail = 0
	success = 0
	while fail < 3 and success < 3:
		x = random.randint(1, 20)
		if x == 20: 
			revive += 1
			success += 3
		if x >= 10: 
			success += 1
			if success == 3: stabilizes += 1
		if x == 1:  
			fail += 1 #doesn't double count fail below 10
		if x < 10: 
			fail += 1
			if fail >= 3: dies+= 1
print(f'died = {dies / 1000:.2f}%')
print(f'stabilized = {stabilizes / 1000:.2f}%')
print(f'revived = {revive / 1000:.2f}%')
	