"""
2.	Enter an integer representing the character code according to the ASCII table. Determine if this is an English
letter code or some other character.

"""


def charCheck(input_char):

    if ((65 <= int(ord(input_char)) <= 90) or (
            97 <= int(ord(input_char)) <= 122)):
        print("Eng Alphabet")

    elif 48 <= int(ord(input_char)) <= 57:
        print("Digit")

    else:
        print("Spec. Chars")


input_char = input("Enter the Char : ")
charCheck(input_char)


