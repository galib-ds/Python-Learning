import data                                                                  # connecting data.py to operation.py
print("Current members of the family are :")
print("#######>>> Family Members <<<#########")

for i in data.members:print(i)
print("##########################")                                          # for loop iterates through the members list and prints them line by line
print("There are",len(data.members),"members in your family")                # counting the number of members

r1 = input("Do you want to add or remove members to the family? (y/n) : ")   # first prompt to ask for add and remove

if( r1 == 'y'):
    r2 = input("what do you want to do add or remove?? (a/r) : ")           # ask what to do add or remove 

    if( r2 == 'a'):                                                         # Add logic
        print("##########################")

        while True:                                                         # use a while loop for multiple input
            new_member = input("Enter New member : ")
            data.members.append(new_member)
            r = input("Do you want to add more? (y/n) : ")
            if( r == 'y'):
                continue
            else:
                break
        
        print("#######>>> Family Members <<<#########")
        
        for i in data.members:print(i)                                      # for loop to print the new members
        print("##########################")  

        print("There are",len(data.members),"members in your family")       # len() for counting the new members

    else:                                                                   # Remove logic
        print("###########>>> WARNING <<<##############")
        member_to_remove = input("Enter the member's name : ")
        if member_to_remove in data.members:                                # searching the list for the members name we inputed
            print("###########>>> WARNING <<<##############")
            print(member_to_remove)
            r3 = input("The member you want to remove!!\nAre you sure? (y/n) : ")
            if( r3 == 'y'):                                                 # Remove by members name
                data.members.remove(member_to_remove)
                print("#######>>> Family Members <<<#########")
                for i in data.members:print(i)
                print("##########################")
                print("There are",len(data.members),"members in your family") 
        else:
            print("That member is not in the family list.")

else:
    print("#######>>> (^ = ^)<<<#########")
    print("No members is Added or Removed")
