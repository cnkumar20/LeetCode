class C:
    def __init__(self):
        self.x = C()
        self.y = 20
    def print_x(self):
        print(f"{self.x}")
        print(f"{self.y}")

a = C()
a.print_x()
