#Automated cashier program
#Willard Sullivan, 2020

#total cost of items
total = 0 
done = ""


from users import users_dict, pwds_dict
from items import items_dict, cost_dict

print("Welcome to the Automated Cashier Program. ")
go = input("Type the Enter key to continue. ")

while go != "": 
    go = input("Type the Enter key to continue. ")

user = input("What is your User ID? ") #asks for user id, checks if user exists
user_int = int(user)
while user_int<0 or user_int>(len(users_dict)):
    print("That user does not exist. Please try again: ")
    user = input("What is your User ID? ")
    user_int = int(user)

pwd = input("What is your password? ") #asks for password, allows user to continue with correct password
while pwd != pwds_dict[user]:
    print("Incorrect password.")
    pwd = input("What is your password? ") 

print("Hello, " + users_dict[user] + ". Welcome to your shopping account. ")

while done != "y" : #allows user to select items and how many. allows user to continue or quit using "y"
    item = input("Type the number corresponding to the item you would like to purchase. 1)Eggs 2)Milk 3)Bread ")
    item_int = int(item)
    while item_int<0 or item_int>(len(items_dict)):
        print("Sorry, that item does not exist.")
        item = input("Type the number corresponding to the item you would like to purchase. 1)Eggs 2)Milk 3)Bread ")
        item_int = int(item)
    amount = int(input("Type the amount of " + items_dict[item] + " you would like. "))
    total = (total + ((cost_dict[item])*amount))
    done = input("Type 'y' if you are done shopping. Otherwise, type any key. ")

print("Your total is: $" + str(total)) #calculates total cost



