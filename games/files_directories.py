from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def get_size(self):
        pass

    def add_component(self, component):
        pass


class File(Component):
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return self.size + other.size

    @property
    def get_size(self):
        return self.size


class Directory(Component):
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

    @property
    def get_size(self):
        result = 0
        for i in self.components:
            result += i.get_size
        return result

    def add_component(self, component):
        self.components.append(component)


s = File(50)
d = File(20)
q = Directory([s, d])
dir = Directory([s, q])
print(dir.get_size, '\n')
dir.add_component(d)
print(dir.get_size)






