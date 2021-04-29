# Game of Fizz Buzz
# Count upwards with a partner
# If the number is divisble by 3, say Buzz
# If number divisible by 5, say fizz
# If neither, say the number

def fizz_buzz(number:int) -> str:
    """
    Play fizz buzz
    :param number: Number to determine correct answer
    :return: The correct thing to say
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "fizz"
    else:
        return str(number)




for i in range(1,101):
    if i % 2 == 0:
        answer = input("Your turn: ")
        if answer.casefold() != fizz_buzz(i):
            print("You lost, correct answer was {}".format(fizz_buzz(i)))
            break
    else:
        print(fizz_buzz(i))
else:
    print("Well done you reached 100")

def factorial(number:int) -> int:
    """
    returns the factorial of input

    :param number: number to get factorial of
    :return: factorial of input
    """
    answer=1
    if number == 0:
        return 1
    else:
        for i in range(1, number + 1):
            answer *= i
        return answer





