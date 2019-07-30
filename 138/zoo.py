
class Animal:

    seq = 10000
    instances = []

    def __init__(self, name):

        self.name = name.capitalize()
        Animal.seq += 1
        self.seq = Animal.seq
        self.__class__.instances.append(self)

    def __str__(self):

        return '{}. {}'.format(self.seq, self.name)

    @classmethod
    def zoo(cls):
        ret = ''
        for instance in cls.instances:
            ret += str(instance)+' \n'
        return ret

# def main():
#     """
#         Finish the Animal class below adding one or more class variables and a classmethod so that the following code
#         dog = Animal('dog')
#         cat = Animal('cat')
#         fish = Animal('fish')
#         lion = Animal('lion')
#         mouse = Animal('mouse')
#         print(Animal.zoo())
#         ... produces the following output:

#         10001. Dog
#         10002. Cat
#         10003. Fish
#         10004. Lion
#         10005. Mouse

#         horse = Animal('horse')
#         assert str(horse) == "10006. Horse"
#     """
#     # dog = Animal('dog')
#     # cat = Animal('cat')
#     # fish = Animal('fish')
#     # lion = Animal('lion')
#     # mouse = Animal('mouse')

#     # print(mouse.name.capitalize())
#     # print(mouse.seq)
#     # print(lion.name.capitalize())
#     # print(lion.seq)
#     # print(str(mouse))

#     # horse = Animal('horse')
#     # print(str(horse))
#     # zoo = Animal.zoo()
#     # print(zoo)

#     for animal in 'dog cat fish lion mouse'.split():
#         Animal(animal)
#     zoo = Animal.zoo()
#     assert "10001. Dog" in zoo
#     assert "10002. Cat" in zoo
#     assert "10003. Fish" in zoo
#     assert "10004. Lion" in zoo
#     assert "10005. Mouse" in zoo

#     horse = Animal('horse')
#     assert str(horse) == "10006. Horse"
#     horse = Animal('monkey')
#     assert str(horse) == "10007. Monkey"

#     zoo = Animal.zoo()
#     print(zoo)
# if __name__ == "__main__":
#     main()
