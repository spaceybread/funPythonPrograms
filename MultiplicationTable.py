multiplier = int(input("Multiplication Table of Which Number?: "))


def tableLength(length):
    x = 0
    while x <= length:
        print(str(multiplier) + " * " + str(x) + " = " + str(multiplier * x))
        x = x + 1


tableLength(int(input("Length of Table: ")))
