class Student:
    def sample(self, name , age):
        self.name = name
        self.age = age

     def describr(self):
         return f"{self.name} is {self.age} years old."

student = Student()
student.sample("raj",21)
print(student.describr())
