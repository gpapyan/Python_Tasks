# 1.	Enter three different numbers from the keyboard. Find the average (greater than one but less than the other).

def average(num1, num2, num3):

    avg = (num1 + num2 + num3) // 3

    return avg


def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


num1 = validate("Please input 1st number : ")
num2 = validate("Please input 2nd number: ")
num3 = validate("Please input 3rd number: ")

print(average(num1, num2, num3), " is AVG of three numbers")


# middle of three numbers

def middle(num1, num2, num3):

    if num1 > num2:
        if (num2 > num3):
            return num2
        elif (num1 > num3):
            return num3
        else:
            return num1
    else:
        if (num1 > num3):
            return num1
        elif (num2 > num3):
            return num3
        else:
            return num2


print(middle(num1, num2, num3), " is Middle of three numbers")
