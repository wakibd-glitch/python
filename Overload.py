class A:
    def __init__(self,a):
        self.a = a

    def __lt__(self,other):
        if self.a < other.a:
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
        

object1 = A(2)
object2 = A(3)

print("Passed Values:" , object1.a, object2.a)
print(object1 < object2)