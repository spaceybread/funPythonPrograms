def table(multiplier, length):
    for i in range(length): 
        print(str(multiplier) + " * " + str(i + 1) + " = " + str(multiplier * (i + 1)))

table(int(input("Table of: ")), int(input("Upto: ")))
