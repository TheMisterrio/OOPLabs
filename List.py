class List:
    def __init__(self, *args):
        self.l = []
        for x in args:
            self.l.append(x)

    def __getitem__(self, item):
        return self.l[item]

    def __len__(self):
        return len(self.l)

    def add_last(self, *args):
        for x in args:
            self.l.append(x)

    def add_first(self, *args):
        for x in args:
            self.l.insert(0, x)

    def remove_item(self, item):
        if self.count_item(item) == 0:
            return False
        while self.l.count(item) != 0:
            self.l.remove(item)
        return True

    def count_item(self, item):
        return self.l.count(item)


a = List(1, 2, 3)
a.add_first('hello')
a.remove_item(2)
a.add_last(3)
print(a.count_item(3))