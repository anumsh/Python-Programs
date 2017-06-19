# Inheritance interview questions


class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()


"""
output:

go A go!
go A go!
go B go!
go A go!
go C go!
go A go!
go C go!
go B go!
go D go!
go A go!
go C go!
go B go!
stop A stop!
stop A stop!
stop A stop!
stop C stop!
stop A stop!
stop C stop!
stop D stop!
stop A stop!
stop C stop!
"""
