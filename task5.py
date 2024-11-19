class RealString:
    def __init__(self, string):
        self.string = string

    def __eq__(self, other):
        if isinstance(other, str):
            other = RealString(other)
        return len(self.string) == len(other.string)

    def __lt__(self, other):
        if isinstance(other, str):
            other = RealString(other)
        return len(self.string) < len(other.string)

apple = RealString("Apple")
yabloko = RealString("Яблоко")

print(yabloko > apple)
print(apple < yabloko)
print(yabloko == apple)

print("Яблоко" > apple)
print(apple < "Яблоко")
print("Яблоко" == apple)
