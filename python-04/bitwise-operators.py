print("###########################################")

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = 0
print("a",a,"=",bin(a),"b",b,"=",bin(b))

print("###########################################")

c = a & b
print("Reasult of a AND b is ",c,":",bin(c))

c = a | b
print("Reasult of a OR b is ",c,":",bin(c))

c = ~a
print("Reasult of a NOT is ",c,":",bin(c))

c = a ^ b
print("Reasult of a EXOR b is ",c,":",bin(c))

c = a << 2
print("Reasult of LEFT SHIFT is ",c,":",bin(c))

c = a >> 2
print("Reasult of RIGHT SHIFT is ",c,":",bin(c))

print("############################################")
