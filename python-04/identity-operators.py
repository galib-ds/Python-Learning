# is x is y
# is not x is not y

a = 20
b = a
print("a =",a,":",id(a),"\nb =",b,":",id(b))

if(a is b):
    print("a and b have the same identity")
else:
    print("a and b do not have the same identity")

if(id(a) == id(b)):
    print("a and b have the same identity")
else:
    print("a and b do not have the same identity")

b = 30
print("id(a) =",a,id(a),"\nid(b) =",b,id(b))
if(a is not b):
    print("a and b do not have the same identity")
else:
    print("a and b have the same identity")

x = 10
y = 20
a = x+y

print("id(a) =",a,id(a),"\nid(b) =",b,id(b))
if(a is b):
    print("a and b have the same identity")
else:
    print("a and b do not have the same identity")