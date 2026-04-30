from abc import ABC,abstractmethod

class RBI(ABC):
     @abstractmethod
     def roi(r):
         pass

class SBI(RBI):
    def show(self):
        print("I Am SBI")
    def roi(self,r):
        print("Rate Of Intrest Given By SBI:",r)

class HDFC(RBI):
    def show(self):
        print("I Am HDFC")
    def roi(self,r):
        print("Rate Of Intrest Given By HDFC:",r)

s1=SBI()
s1.show()
s1.roi(6.5)

h1=HDFC()
h1.show()
h1.roi(6.9)
