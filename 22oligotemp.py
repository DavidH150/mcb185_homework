import math
def oligotemp(A, C, G, T):
    oligo = A+T+C+G
    if oligo <= 13: tm = (A+T)*2 + (G+C)*4
    else: tm = 64.9 + 41*(G+C-16.4)/(A+T+G+C)
    print('when A:',A,'C:',C,'G:',G,'T:',T, 'the oligo melting point is',tm,'Celsius')

oligotemp(1,1,1,1)
oligotemp(4,4,4,4)

