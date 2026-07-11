# list is a sequence data type
# startes from index 0

list1 =['physics','chemistry',2005,2026]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = ["a","b",'c',"d"]

print("len(list1) = ",len(list1))
print("len(list1) = ",len(list2))
print("len(list1) = ",len(list3))
print("\n")
print("list1 + list2 = ",list1 + list2)
print("\n")
print("list1 * 2 = ", list1 * 2)

# membership operation
print("7 in list2 = ", 7 in list2)
print("7 not in list2 = ", 10 not in list2)
print("\n")
print("\"c\" in list3 = ", "c" in list3)
print("\"X\" not in list3 = ", "x" not in list3)

# iterate through a list

for x in list1:print(x)
print("\n")
for n in  list2:print(n)
print("\n")
for y in list3:print(y)