
import random
''' prints 5 different numbers betweeon 0, 1
for i in range(5):
	print(random.random())
'''
''' prints 50 nt each with a 25%
for i in range(50):
	print(random.choice('ACGT'), end='')
print()
'''
''' prints a 50 nt with a 70% chance of AT
for i in range(50):
	r = random.random()
	if r < 0.7: print('AT', end='')
	else:       print('GC', end='')
print()
'''
''' rolls a 6 sided die three times
for i in range(3):
	print(random.randint(1, 6))
'''
''' normal distribution 5 times
for i in range(5):
	print(random.gauss(0.0, 1.0))
'''
''' line break
print('this line\n has some\n line breaks')

tab spacing
print('a\tb\tcat\tdogma')
print(10, 20 , 30, 40, sep='\t')
print(100, 2000, 30000, 40000, sep='\t')
''' 
#''' f strings
i = 1 
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi:.3f}')
print(f'tau {pi + pi}')
'''
'''
'''
import sys
print('logging', file=sys.stderr)
'''
'''random seeds can be predefined
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())
'''