class Fraction:
    def __init__(self, integer, fractional):
        self.integer = int(integer)
        self.fractional = str(fractional).rstrip('0')

    def check_len(self, other):
        if len(self.fractional) >= len(other.fractional):
            length = len(self.fractional)
        else:
            length = len(other.fractional)
        return length

    def format_fraction(self, other):
        if len(self.fractional) >= len(other.fractional):
            other.fractional = other.fractional + '0' * (
                    len(self.fractional) - len(other.fractional))
        else:
            self.fractional = self.fractional + '0' * (
                        len(other.fractional) - len(self.fractional))
        return other.fractional

    def __add__(self, other):
        self.integer = self.integer + other.integer
        other.fractional = self.format_fraction(other)
        length = self.check_len(other)
        fractional = []
        for i in range(0, length):
            fractional.append('')
            num = int(self.fractional[i]) + int(other.fractional[i])
            if num >= 10:
                try:
                    fractional[i-1] = int(fractional[i-1]) + (num // 10)
                except:
                    self.integer += num//10
            fractional[i] = num % 10
        self.fractional = ''
        for i in range(0, length):
            self.fractional += str(fractional[i])
        self.fractional = self.fractional.rstrip('0')
        return self

    def __sub__(self, other):
        self.integer = self.integer - other.integer
        other.fractional = self.format_fraction(other)
        length = self.check_len(other)
        fractional = []
        for i in range(0, length):
            fractional.append('')
            num = int(self.fractional[i]) - int(other.fractional[i])
            if num < 0:
                try:
                    fractional[i-1] -= 1
                except:
                    self.integer -= 1
                fractional[i] = 10 + int(self.fractional[i]) - int(other.fractional[i])
            else:
                fractional[i] = num
        self.fractional = ''
        for i in range(0, length):
            self.fractional += str(fractional[i])
        self.fractional = self.fractional.rstrip('0')
        return self

    def __mul__(self, other):
        self.num = str(self.integer) + self.fractional
        other.num = (str(other.integer) + other.fractional)[::-1]
        length = len(self.fractional) + len(other.fractional)
        nums = 0
        for i in range(0, len(other.num)):
            nums += int(self.num) * int(other.num[i]) * 10**i
        nums = str(nums)
        print(length)
        self.integer = nums[:len(nums) - length]
        self.fractional = nums[len(nums) - length:]
        return self

    def __eq__(self, other):
        if self.integer == other.integer and self.fractional == other.fractional:
            return True
        return False

    def __ne__(self, other):
        if self.integer != other.integer or self.fractional != other.fractional:
            return True
        return False

    def __lt__(self, other):
        if self.integer <= other.integer and self.fractional < other.fractional:
            return True
        return False

    def __le__(self, other):
        if self.integer <= other.integer and self.fractional <= other.fractional:
            return True
        return False

    def __repr__(self):
        return str(self.integer) + '.' + self.fractional




