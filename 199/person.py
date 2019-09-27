import inspect


class Person:
    def __str__(self):
        return 'I am a person'


class Mother(Person):
    def __str__(self):
        return '{} and awesome mom'.format(super().__str__())


class Father(Person):
    def __str__(self):
        return '{} and cool daddy'.format(super().__str__())


class Child(Father, Mother):
    def __str__(self):
        return 'I am the coolest kid'


# def main():
#     print('here ...')

#     person = Person()
#     # print(str(person))
#     assert str(person) == 'I am a person'

#     mom = Mother()
#     assert str(mom) == 'I am a person and awesome mom'

#     dad = Father()
#     assert str(dad) == 'I am a person and cool daddy'
#     # print(str(dad))
#     child = Child()
#     assert str(child) == 'I am the coolest kid'

#     assert Person.__mro__ == (Person, object)

#     assert Father.__mro__ == (Father, Person, object)

#     assert Mother.__mro__ == (Mother, Person, object)

#     assert Child.__mro__ == (Child, Father, Mother, Person, object)

#     assert issubclass(Person, object)
#     assert issubclass(Father, Person)
#     assert issubclass(Father, object)
#     assert issubclass(Mother, Person)
#     assert issubclass(Mother, object)
#     assert issubclass(Child, Father)
#     assert issubclass(Child, Mother)
#     assert issubclass(Child, Person)
#     assert issubclass(Child, object)

#     substr = 'I am a person'
#     for src in (inspect.getsource(Father),
#                 inspect.getsource(Mother)):
#         assert substr not in src


# if __name__ == '__main__':
#     main()
