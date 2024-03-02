def genSqrt():
    n=int(input("Enter a num N: "))
    double=[(i+1)**2 for i in range(n)]
    print(double)
genSqrt()