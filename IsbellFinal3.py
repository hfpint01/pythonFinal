import random


def compare(ans,res):

    """
    This program generates two random numbers and asks for the sum. It then does a comparison of the
    user input and the expected answer. If the answer is wrong, it'll ask again. If it's correct, it will say correct. 
    """
    correct = False

    while correct == False:
        if ans == res:
            correct = True
            print("You are correct!")
        else:
            ans = int(input("Please try again. What is the sum of %d + %d? " % (x, y)))

x = random.randint(1,9)
y = random.randint(1,9)
result = x + y

var = input("Would you like to view the help documentation? Enter y/n: ")
if var == 'y':
    help(compare)
    answer = int(input("What is the sum of %d + %d? \n" % (x, y)))
    compare(answer, result)

else:
    answer = int(input("What is the sum of %d + %d? \n" % (x, y)))
    compare(answer, result)


