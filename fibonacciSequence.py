def sequence(limit):
    list = [1, 2]
    n = 0
    while n < limit:
        lastTerm = list[-1] + list[-2]
        list.append(lastTerm)
        print(list[n])
        n = n + 1


while True:
    sequence(int(input("Sequence Number: ")))
