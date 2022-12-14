# def hello():
#     print("Hello")
#
#
# hi = hello
# hello()
# hi()

say = print
say("This is awesome!!")


class overloading:

    def overload(self):
        pass

    def overload(self, hello):
        pass

overloading1 = overloading()

hello = "hello"

overloading1.overload()
overloading1.overload(hello)