def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Print a string centred, with ** on either side.

    :param text:The string to print
        An Asterisk (*) will result in row of asterisks.
        Default will print a blank line, with ** border
    :param screen_width: Overall width of screen to print too
    :raises ValueError: if text exceeds the screen width
    """
    
    if len(text) > screen_width - 4:
        raise ValueError("String '{}' is larger than specified width {}"    # Shouldn't raise exceptions too often, but when you do, include enoguh info to help programmer
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)

banner_text("Today is gonna be the the day, the day i bring it back to you", 100)

