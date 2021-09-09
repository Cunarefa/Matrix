
class File():
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return self.size + other.size

    def some(self):
        return self.size


class Directory():
    def __init__(self, components):
        self.components = components
        self.limit = -1

    # def __next__(self):
    #     if self.limit < len(self.components) - 1:
    #         self.limit += 1
    #         return self.components[self.limit]
    #     else:
    #         raise StopIteration

    # def __iter__(self):
    #     return self

    def some(self):
        result = []
        for i in self.components:
            result.append(i.some())
        return sum(result)


s = File(50)
d = File(20)
q = Directory([s, d])
dir = Directory([s, q])
print(dir.some())






