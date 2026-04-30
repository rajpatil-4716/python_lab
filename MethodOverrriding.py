# when there is a same method prototipe in your both base class and drive class in if you call that method using the object of drive class then only drive class method will be call.
# so u can say that method of drive class over rittes the method of your base class.

class A:
    def show(self):
        print("Show from Class A")
class B(A):
    def show(self):
        super().show()
        print("Show from Class B")
class C(A):
    def show(self):
        super().show()
        print("Show from Class C")
class D(C,B):
    def show(self):
        super().show()
        print("Show from Class D")

d1=D()
d1.show()
