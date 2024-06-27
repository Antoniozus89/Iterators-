class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start if start % 2 == 0 else start + 1
        self.end = end
        if self.start >= self.end:
            raise ValueError("Начало должно быть меньше конца")

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration()

        result = self.start
        self.start += 2
        return result



iterator = EvenNumbers(10, 25)

for even_number in iterator:
    print(even_number)



