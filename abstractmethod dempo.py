from abc import ABC,abstractmethod

class CAR(ABC):
     @abstractmethod
     def feturs(speed, seat, fule):
         pass

class volvo(CAR):
    def show(self):
        print("I Am volvo")
    def feturs(self,speed,seat,fule):
        print("Max Speed is :",speed)
        print("Max Seat is :",seat)
        print("Fule type is : ",fule)

class BMW(CAR):
    def show(self):
        print("I Am BMW")
    def feturs(self,speed):
        print("Max Speed is :",speed)
    def feturs(self,seat):
        print("Max seat is :",seat)    
   
class HONDA(CAR):
    def show(self):
        print("I Am HONDA")
    def feturs(self,speed):
        print("Max Speed is :",speed)
    def feturs(self,seat):
        print("Max seat is :",seat)    
    
class MARUTI(CAR):
    def show(self):
        print("I Am MARUTI")
    def feturs(self,speed):
        print("Max Speed is :",speed)
    def feturs(self,seat):
        print("Max seat is :",seat)    
                  
        
        
v1=volvo()
v1.show()
v1.feturs(110)
v1.feturs(5)
v1.fule(petrol)

b1=BMW()
b1.show()
b1.feturs(105)
b1.feturs(5)

h1=HONDA()
h1.show()
h1.feturs(100)
h1.feturs(5)

m1=MARUTI()
m1.show()
m1.feturs(120)
m1.feturs(7)
