class JsObject(dict):
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """

    def __init__(self, *arg, **kw):
        super(JsObject, self).__init__(*arg, **kw)
        self.__dict__ = self


# def main():
#     print('here!')

#     j = JsObject(a=1, b=2, c=3)

#     assert type(j) == JsObject
#     assert j['a'] == 1
#     assert j['b'] == 2
#     assert j['c'] == 3

#     # j['d'] = 4
#     print(j)
#     # assert len(j) == 4
#     # del j['b']
#     # assert 'b' not in j
#     # assert len(j) == 3
#     # print(list(j.keys()))
#     # print(list(j.values()))
#     # print(list(j.items()))
#     # assert list(j.keys()) == ['a', 'c', 'd']
#     # assert list(j.values()) == [1, 3, 4]

#     assert j.a == 1
#     assert j.b == 2
#     assert j.c == 3

#     # j.d = 4
#     # # print(j)
#     # # j['d'] = 10
#     # print(j)
#     # assert len(j) == 4

#     # del j.b
#     # print(j)

#     # j.update(dict(e=5))
#     # print(j)
#     # assert j.e == 5

#     j.d = JsObject(e=5)
#     print(j)
#     assert j.d.e == 5
#     j.d.e = JsObject(f=6)
#     print(j)
#     assert j.d.e.f == 6


# if __name__ == '__main__':
#     main()
