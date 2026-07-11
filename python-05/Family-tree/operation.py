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

        add_more = 'y'

        while add_more == 'y':
            new_member = input("Enter new members Name : ")
            data.members.append(new_member)

            add_more = input("Do you want to add another member? (y/n) : ")
       
        print("#######>>> Family Members <<<#########")
        
        for i in data.members:print(i)                                      # for loop to print the new members
        print("##########################")  

        print("There are",len(data.members),"members in your family")       # len() for counting the new members

    else:                                                                   # Remove logic
        print("###########>>> WARNING <<<##############")
        
        remove_more = 'y'

        while remove_more == 'y':
            members_to_remove = input("Enter the members name you want to remove : ")
            if(members_to_remove in data.members):
                r3 = input("Do you want to remove {} (y/n) : ".format(members_to_remove))
                if r3 == 'y':
                    data.members.remove(members_to_remove)
                else:
                    print("{} is not removed".format(members_to_remove))                   
            else:
                print("The member is not in the family list!!")
            remove_more = input("Do you want to remove another member? (y/n) : ")

        print("#######>>> Family Members <<<#########")
        for i in data.members:print(i)
        print("##########################")
        print("There are",len(data.members),"members in your family")

else:
    print("#######>>> (^ = ^)<<<#########")
    print("No members is Added or Removed")
