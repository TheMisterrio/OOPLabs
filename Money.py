class Money:
    def __init__(self, value, coins):
        self.value = value
        if coins > 100:
            raise ValueError
        self.coins = coins

    def __repr__(self):
        return str(self.value) + '.' + str(self.coins if self.coins > 10 else '0' + str(self.coins)) + ' грн.'

    @staticmethod
    def convert_to_coins(num):
        return num.value * 100 + num.coins

    def __add__(self, other):
        result = Money.convert_to_coins(self) + Money.convert_to_coins(other)
        return Money(result//100, result % 100)

    def __sub__(self, other):
        result = Money.convert_to_coins(self) - Money.convert_to_coins(other)
        return Money(result // 100, result % 100)

    def __eq__(self, other):
        return Money.convert_to_coins(self) == Money.convert_to_coins(other)

    def __lt__(self, other):
        return Money.convert_to_coins(self) < Money.convert_to_coins(other)

    def __le__(self, other):
        return Money.convert_to_coins(self) <= Money.convert_to_coins(other)

