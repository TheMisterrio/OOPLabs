import cmath


class String:
    def __init__(self, string):
        self.string = string

    def get_length(self):
        return len(self.string)

    def make_empty(self):
        self.string = ''
        return self.string


class ComplexNum(String):
    def __init__(self, part1, part2):
        decimal = ['0','1','2','3','4','5','6','7','8','9']
        self.part1 = part1
        self.part2 = part2
        self.complex_number = '0'
        print(str(self.part1)[0])
        if str(self.part1)[0] != '-' and str(self.part1)[0] not in decimal:
            self.complex_number = 0
        for i in str(self.part1)[1:]:
            if i not in decimal:
                self.complex_number = 0
        for i in str(self.part2):
            if i not in decimal:
                self.complex_number = 0
        if self.complex_number != 0:
            try:
                self.part1 = int(self.part1)
                self.part2 = int(self.part2)
            except:
                self.complex_number = 0
            self.complex_number = complex(self.part1, self.part2)

    def __eq__(self, other):
        return self.complex_number == other.complex_number

    def __add__(self, other):
        return self.complex_number + other.complex_number

    def __mul__(self, other):
        return self.complex_number * other.complex_number

