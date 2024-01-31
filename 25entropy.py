# co authors: aman, adele 
import math
import sys

def shannon(a, c, g, t):
	nt = (a + c + g + t)
	if nt == 0: return 0
	pa = a/nt
	pc = c/nt
	pg = g/nt
	pt = t/nt
	ma = pa*math.log2(pa)
	mc = pc*math.log2(pc)
	mg = pg*math.log2(pg)
	mt = pt*math.log2(pt)
	return -(ma + mc + mg + mt)

print(shannon(1, 9, 2, 3))
print(shannon(3, 7, 8, 10))
print(shannon(77, 55, 55, 77))
print(shannon(0 ,0 ,0, 0))