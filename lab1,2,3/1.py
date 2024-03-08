class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(isinstance(side, (int, float)) and side > 0 for side in [self.a, self.b, self.c]):
            return 
        elif any(side <= 0 for side in [self.a, self.b, self.c]):
            return 
        elif self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 
        else:
            return 
a=TriangleChecker(1,2,3)
print(a.is_triangle())