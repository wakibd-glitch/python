class myClass:

    __privateVar = 27

    def privMeth(self):
        print("Im inside class myClass")

    def __hello(self):
        print("private variable value: " , myClass.__privateVar)

myobject = myClass()

myobject.privMeth()
