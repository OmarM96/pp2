def genOdd():
    n=int(input("Enter your number: "))
    odd=[(i) for i in range(0, n+2, 2)]
    print(odd)
genOdd()