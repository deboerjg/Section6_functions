import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric() and 1 <= int(temp) <= 1000:
            return int(temp) # Return prevents further code from exceuting
        else:
            print("{} is not a valid number".format(temp))  # Code after return is not run, so you dont need else statement


highest = 1000
lowest = 1
answer = random.randint(lowest, highest)
guess = 0
print(answer) # TODO: Remove later

print("Please guess number between 1 and {}: ".format(highest))
while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        print("You quit the game")
        break
    elif guess == answer:
        print("You got it right!")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")


# if guess == answer:
#     print("Got it first try")
# else:
#     if guess > answer:
#         print("Please guess lower")
#     else:
#         print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, second try")
#     else:
#         print("Sorry bro, didn't get it")




 # if guess < 5:
#     print("Try a higher number you stupid fuck")
#     guess =  int(input())
#     if guess == answer:
#         print("Well done, I did it first try though brah")
#     else:
#         print("You fucking suck at this")
# elif guess > 5:
#     print("Try a lower number you stupid fuck")
#     guess =  int(input())
#     if guess == answer:
#         print("Well done, I did it first try though brah")
#     else:
#         print("You fucking suck at this")
# else:
#     print("Congrats you smart fuck")




