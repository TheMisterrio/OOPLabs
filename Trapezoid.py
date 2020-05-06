class Trapezoid:
    def __init__(self, leftup, rightup, leftdown, rightdown):
        self.leftup = float(leftup[0]), float(leftup[1])
        self.rightup = float(rightup[0]), float(rightup[1])
        self.leftdown = float(leftdown[0]), float(leftdown[1])
        self.rightdown = float(rightdown[0]), float(rightdown[1])

    def isEquilateral(self):
        left, top, right, bottom = self.side_length()
        return left == right

    def side_length(self):
        left_side = ((self.leftup[0] - self.leftdown[0]) ** 2 + (self.leftup[1] - self.leftdown[1]) ** 2) ** (1 / 2)
        top_side = ((self.leftup[0] - self.rightup[0]) ** 2 + (self.leftup[1] - self.rightup[1]) ** 2) ** (1 / 2)
        right_side = ((self.rightup[0] - self.rightdown[0]) ** 2 + (self.rightup[1] - self.rightdown[1]) ** 2) ** (
                1 / 2)
        bottom_side = ((self.rightdown[0] - self.leftdown[0]) ** 2 + (self.rightdown[1] - self.leftdown[1]) ** 2) ** (
                1 / 2)
        return round(left_side, 3), round(top_side, 3), round(right_side, 3), round(bottom_side, 3)

    def perimeter(self):
        left, top, right, bottom = self.side_length()
        return round(left + top + right + bottom, 3)

    def square(self):
        c, b, d, a = self.side_length()
        area = ((a + b) / 2) * (c ** 2 - (((a - b) ** 2 + c ** 2 - d ** 2) / (2 * (a - b))) ** 2) ** (1 / 2)
        return round(area, 3)
