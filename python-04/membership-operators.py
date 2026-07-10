# in     x in y
#not in  x not in y

a = int(input("Enter a : "))
b = int(input("Enter b : "))

list = [1,2,3,4,5,6,7,8,9,10]

print(list)
print("a : ",a,"\nb : ",b,)

if(a in list):
    print("Line 1 - a is available in the given list")
else:
    print("Line 1 - a is not available in the given list")

if(b not in list):
    print("Line 2 - b is not available in the given list")
else:
    print("Line 2 - b is available in the given list")