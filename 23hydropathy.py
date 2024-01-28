import sys

def hydropathy(x):
    if x == 'A': return 1.8
    if x == 'C': return 2.5
    if x == 'D': return -3.5
    if x == 'E': return -3.5
    if x == 'F': return 2.8
    if x == 'G': return -.4
    if x == 'H': return -3.2
    if x == 'I': return 4.5
    if x == 'K': return -3.9
    if x == 'L': return 3.8
    if x == 'M': return 1.9
    if x == 'N': return -3.5
    if x == 'P': return -1.6
    if x == 'Q': return -3.5
    if x == 'R': return -4.5
    if x == 'S': return -.8
    if x == 'T': return -.7
    if x == 'V': return 4.2
    if x == 'W': return -.9
    if x == 'Y': return -1.3
    else:        sys.exit('Not an amino acid')


print(hydropathy('L'))
print(hydropathy('A'))
print(hydropathy('B'))

