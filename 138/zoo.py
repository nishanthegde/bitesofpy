class Animal:
    seq = 10000
    instances = []

    def __init__(self, name):
        self.__class__.seq += 1
        self.name = name.capitalize()
        self.__class__.instances.append(f"{self.__class__.seq}. {self.name}")

    def __str__(self):
        return f"{self.__class__.seq}. {self.name}"

    @classmethod
    def zoo(cls):
        return '\n'.join(cls.instances)
