#Automated cashier program
#Willard Sullivan, 2020

#total cost of items
total = 0 
done = ""


from users import users_dict
from items import items_dict, cost_dict

print("Welcome to the Automated Cashier Program. ")
go = input("Type the Enter key to continue. ")

while go != "": 
    go = input("Type the Enter key to continue. ")

user = input("What is your User ID? ")
print("Hello, " + users_dict[user])

while done != "y" :
    item = input("Type the number corresponding to the item you would like to purchase. 1)Eggs 2)Milk 3)Bread ")
    item_int = int(item)
    while item_int<0 or item_int>4:
        print("Sorry, that item does not exist.")
        item = input("Type the number corresponding to the item you would like to purchase. 1)Eggs 2)Milk 3)Bread ")
        item_int = int(item)
    amount = int(input("Type the amount of " + items_dict[item] + " you would like. "))
    total = (total + ((cost_dict[item])*amount))
    done = input("Type 'y' if you are done shopping. Otherwise, type any key. ")

print("Your total is: $" + str(total))



