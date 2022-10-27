class Protected:
    def __init__ (self):
        self._protectedVar = 0 # creation of a protected class
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private
        


obj = Protected() # instantiation of the protected class
obj._protectedVar = 19 # giving the protected class an assigned variable
print(obj._protectedVar)
obj1 = Protected()
obj1.getprivate()
obj1.setPrivate(17)
obj1.getPrivate()
