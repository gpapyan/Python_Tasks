# 3.	Find the sum and product of the digits of the entered natural number. For example, if the number 325 is
# entered, the sum of its digits is 10 (3+2+5), and the product is 30 (325). Do not use string and string methods


def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


numA = validate("Please input number : ")


# Product of digits

def numProduct(numA):

    product = 1

    while numA != 0:

        product = product * (numA % 10)

        numA = numA // 10

    return product


print(numProduct(numA), " is Product of digits \n")


# Summ of digits

def numSum(numA):

    summ = 0

    while (numA != 0):

        summ = summ + int(numA % 10)

        numA = int(numA / 10)

    return summ


print(numSum(numA), " is Summ of digits")

