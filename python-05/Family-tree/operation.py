import data                                                                  # connecting data.py to operation.py
print("Current members of the family are :")
print("#######>>> Family Members <<<#########")

for i in data.members:print(i)
print("##########################")                                          # for loop iterates through the members list and prints them line by line
print("There are",len(data.members),"members in your family")                # counting the number of members

r1 = input("Do you want to add or remove members to the family? (y/n) : ")

if( r1 == 'y'):
    r2 = input("what do you want to do add or remove?? (a/r) : ")
    if( r2 == 'a'):
        print("##########################")
        new_member = input("Enter New member : ")
        data.members.append(new_member)
        print("#######>>> Family Members <<<#########")
        for i in data.members:print(i)
        print("##########################")  
        print("There are",len(data.members),"members in your family")   

    else:
        print("###########>>> WARNING <<<##############")
        member_to_remove = input("Enter the member's name : ")
        if member_to_remove in data.members:
            print("###########>>> WARNING <<<##############")
            print(member_to_remove)
            r3 = input("The member you want to remove!!\nAre you sure? (y/n) : ")
            if( r3 == 'y'):
                data.members.remove(member_to_remove)
                print("#######>>> Family Members <<<#########")
                for i in data.members:print(i)
                print("##########################")
                print("There are",len(data.members),"members in your family") 
        else:
            print("That member is not in the family list.")
else:
    print("#######>>> (^ = ^)<<<#########")
    print("No members is added or removed")
