import random
import time

def doc():
    """
    This program will generate 30 numbers between 1 and 70. If the number is unique, it'll place it in a
    unique list or if it's a duplicate, it'll place the number in a list of duplicates. Both lists will print.
    No user input is required.
    """
my_list = []
dup_list = []


for i in range(30):
    num = random.randrange(1,70,1)

    if num not in my_list:
        my_list.append(num)
    else:
        dup_list.append(num)

var = input("Would you like to see the help documentation? y/n ")
if var == 'y':
    help(doc)
    time.sleep(1)
    print(my_list)
    print("\nThese are the duplicate numbers that were generated: \n")
    print(dup_list)

elif var == 'n':
    print("\nHere are 30 random numbers between 1 and 70: \n")
    print(my_list)
    print("\nThese are the duplicate numbers that were generated: \n")
    print(dup_list)

else:
    print("I'm sorry, that was not a valid answer.")
