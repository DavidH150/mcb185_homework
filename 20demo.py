#20demo.py by David Hurd
import math
import sys

#if statements
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

a = 1 
s = 'G'
if a < s: print('a < s')
"""
a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

if math.isclose(a,b): print('close enough but fancy')
print(abs(a-b)) # 5.55555e-17
if abs(a-b) < 1e-9: print('close enough')
"""
"""
if a == b:
    print('a equals b')
print(a,b)
c = a == b
print(c)
print(type(c))
#strings
s='hello world'
print(s, type(s))
#function of pythag
def pythagoras(a, b):
    if a <= 0: sys.exit('error: a must be greater than 0')
    if b <= 0: sys.exit('error: b must be greater than 0')
    return math.sqrt(a**2 + b**2)
#print(pythagoras(-1,1))
print(pythagoras(3,4))
print(pythagoras(1,1))
#pythag therm
a=3
b=4
c = math.sqrt(a**2 + b**2)
print(c)
print(type(a), type(b), type(c), sep=', ') #seeing variable types
#random math functs
print(0.1*1)
print(0.1*3)
print (math.e,math.pi, math.inf, math.nan)
print(math.ceil(76.5))
print(math.floor(76.7))
print(math.log(1), math.log2(7), math.log10(3))
print (math.sqrt(9), math.pow(2,3), math.factorial(6))
print ('Hello, again') # greetings
print(1.5e-2)
print(1+1)
print(1-1)
print(2*2)
print(1/2)
print(2**3)
print(5//2)
print(5%2)
print(5*(2+1))
print (abs((-6)))
print (pow(2,3))
print (round(7.9738083, ndigits=3))
"""


"""
this is also
a multi-line 
comment
"""



