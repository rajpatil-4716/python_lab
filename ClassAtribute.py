class Car:
    wheels = 4

    def sample(self,brand,model):
        self.brand = brand
        self.model = model

car1 = Car()
car2 = Car()

car1.sample("Toyota", "Camry")
car2.sample("Honda", "Civik")

print(car1.wheels)
print(car2.wheels)

print("Barnd With Car1 : ",car1.brand)
print("Barnd With Car2 : ",car2.brand)
