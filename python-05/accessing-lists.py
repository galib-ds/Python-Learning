list1 =['physics','chemistry',2005,2026]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = ["a","b",'c',"d"]
print("list1[0]: ", list1[0])
print("list1[3]: ", list1[3])
print("list1[2]: ", list1[2])
print("list2[1:5]: ", list2[1:5])

# update
print(list1)
print("Value available at index 2 : ", list1[2])
list1[2] = 2024
print("New value available at index 2 : ", list1[2])
print(list1)

# delete
del list1[2]
print("After deleting value at index 2 : ", list1)

print(list2)
del list2

# print(list2)
# NameError: name 'list2' is not defined. Did you mean: 'list1'?