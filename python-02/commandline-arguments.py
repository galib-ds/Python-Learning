#argv sys argument
import sys
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x+y
print("x=",x,"y=",y,"z=",z)