
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    
    def is_triangle(self):
    if (self.a + self.b) >= self.c or (self.a + self.c) >= self.b or (self.c + self.b) >= self.a:
        return "we can create triangle "
    
    elif self.a < 0 or self.b < 0 or  self.c < 0:
           return "we can not create triangle with negative numbers"

    elif [self.a or self.b or self.c] != (int, float):
        return "we can not create triangle with symbols or words"

ttt = TriangleChecker()

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

ttt.__init__(a, b, s)
print(ttt.is_triangle())

    
