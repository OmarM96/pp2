def genSquares():
    a=int(input("Enter your number: "))
    b=int(input("Enter your second number: "))
    numbers=[i**2 for i in range(a, b+1)]
    print(numbers)
genSquares()