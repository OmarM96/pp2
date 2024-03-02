def genrev():
    n=int(input("Enter your number: "))
    numbers=[k for k in range(n, -1, -1)]
    print(numbers)

genrev()