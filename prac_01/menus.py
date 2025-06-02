"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

user_name = input("Enter name: ")

menu = "(H)ello\n(G)oodbye\n(Q)uit"

print(menu)

choice = input(">>> ")

while choice != "Q":
    if choice == "H":
        print (f"Hello {user_name}")
    elif choice == "G":
        print (f"Goodbye {user_name}")
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>> ")
print ("Finished.")
