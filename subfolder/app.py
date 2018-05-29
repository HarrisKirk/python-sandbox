import sys

for p in sys.path:
    print (f'the path is {p}')
import mod

print ( mod.s)
print ('*')
print (mod.__file__)
