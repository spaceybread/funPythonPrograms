userInput = input("Given an array of numbers separated by spaces: ")
arrayTable = userInput.split()
arrayTable = list(map(int, arrayTable))
evenPrime = []
evenNonPrime = []
oddPrime = []
oddNonPrime = []

for num in arrayTable:
    if num % 2 == 0 and num == 2:
        evenPrime.append(2)
    elif num % 2 == 0 and num != 2:
        evenNonPrime.append(num)
    else:
        pass
for num in arrayTable:
    divisors = []
    if num % 2 != 0:
        x = 1
        while x <= num:
            if num % x == 0:
                divisors.append(x)
                x = x + 1
            else:
                x = x + 1
        if len(divisors) == 2:
            oddPrime.append(num)
        else:
            oddNonPrime.append(num)
for num in oddNonPrime:
    if 1 in oddNonPrime:
        oddNonPrime.remove(1)

print('even prime numbers are: ' + str(evenPrime))
print('even composite numbers are: ' + str(evenNonPrime))
print('odd prime numbers are: ' + str(oddPrime))
print('odd composite numbers are ' + str(oddNonPrime))
