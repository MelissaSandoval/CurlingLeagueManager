class OddIterator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            value = next(self.iterable)
            if value % 2 != 0:
                return value


class Last:
    def __init__(self, iterable, count):
        self.iterable = iterable
        self.count = count
        self.index = len(iterable) - count
        if self.index < 0:
            self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            value = self.iterable[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration
