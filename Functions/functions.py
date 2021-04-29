def multiply(x: float, y: float) -> float:
    """
    Multiply two integers or sequences together

    :param x: first `int` to get multiplied
    :param y: second `int` to get multiplied
    :return: the product of both parameters
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    :param string: The string to check
    :return: True is string is a palindrome, False otherwise
    """
    return string.casefold() == string[::-1].casefold()


def palindrome_sentence(sentence: str) -> bool:
    string= ""
    for char in sentence:
        if char.isalnum():
            string += char

    print(string)
    return is_palindrome(string)


print(palindrome_sentence("Was it a car, or a cat, I saw?"))

print(multiply(18, 3))


def fibonacci(n: int) -> int:
    """ Return the `n` th fibonacci number, for positive `n`. """
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result

for i in range(35):
    print(i, fibonacci(i))



