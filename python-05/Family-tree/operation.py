import data                                                      # connecting data.py to operation.py
print("Current members of the family are :")
print("#######>>> Family Members <<<#########")
for i in data.members:print(i)                                   # for loop iterates through the members list and prints them line by line
print("##########################")
print("There are",len(data.members),"members in your family")    # counting the number of members

while True:
    r1 = input("Do you want to add or remove members to the family? (y/n) : ").strip().lower()   # first prompt to ask for add and remove
    if r1 == 'y' or r1 == 'n':
        break
    # print("Invalid Input!! Please enter y/n ")
    
if r1 == 'y':
    while True:
        r2 = input("what do you want to do add or remove?? (a/r) : ").strip().lower()   # first prompt to ask for add and remove
        if r2 == 'a' or r2 == 'r':
            break
        # print("Invalid Input!! Please enter a/r ")
    
    if r2 == 'a':                                                                            # Add logic
        print("##########################")
        add_more = 'y'                                                                      # while loop for multiple user input
        while add_more == 'y':
            new_member = input("Enter new members Name : ").strip()                         # takes new members name except space
            if new_member:
                if new_member in data.members:                                              # cheackes if the member is already in list or not
                    print("{} already exists!!".format(new_member))
                else:
                    data.members.append(new_member)                                         # addes member to the list
            else:                                                                           # if there is no entry
                    print("Name can't be empty.")
            while True:
                add_more = input("Do you want to add another member? (y/n) : ").strip().lower() # condition for while loop to run
                if add_more == 'y' or add_more == 'n':
                    break
                # print("Invalid Input!! Please enter y/n ")
        print("#######>>> Family Members <<<#########")      
        for i in data.members:print(i)                                                      # for loop to print the new members
        print("##########################")  
        print("There are",len(data.members),"members in your family")                       # len() for counting the new members
   
    else:                                                                          # Remove logic
        print("###########>>> WARNING <<<##############")   
        remove_more = 'y'                                                                                      # while loop for removing multiple users
        while remove_more == 'y':
            member_to_remove = input("Enter the members name you want to remove : ").strip()                   # take user input
            if member_to_remove in data.members :                                                              # checkes the list
                while True:
                    r3 = input("Do you want to remove {} (y/n) : ".format(member_to_remove)).strip().lower()
                    if r3 == 'y' or r3 == 'n':
                        break
                    # print("Invalid Input!! please enter y/n")
                if r3 == 'y':
                     data.members.remove(member_to_remove)
                     print("{} removed succesfully".format(member_to_remove))                                   # removes the member
                else:
                     print("{} is not removed".format(member_to_remove))              
            else:
                print("The member is not in the family list!!")                                                # if the member is not in the list
            while True:
                remove_more = input("Do you want to remove another member? (y/n) : ").strip().lower()
                if remove_more == 'y' or remove_more == 'n':
                   break             
                # print("Invalid input!! Please enter y/n.")

        print("#######>>> Family Members <<<#########")                     # print the final output the new member list
        for i in data.members:print(i)
        print("##########################")
        print("There are",len(data.members),"members in your family")       # total new number of members

else:
    print("#######>>> (^ = ^)<<<#########")                                                  # if the user choses nothing to do
    print("No members is Added or Removed")
