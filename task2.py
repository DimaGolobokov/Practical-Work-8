class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not (isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)) and isinstance(self.c, (int, float))):
            return "Нужно вводить только числа!"

        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"

        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."

triangle_checker = TriangleChecker(3, 4, 5)
print(triangle_checker.is_triangle())

triangle_checker = TriangleChecker(-1, -2, -3)
print(triangle_checker.is_triangle())

triangle_checker = TriangleChecker(1, "abc", 3)
print(triangle_checker.is_triangle())

triangle_checker = TriangleChecker(1, 2, 10)
print(triangle_checker.is_triangle())