
class Person:
    def __init__(self,name,age,size,hair_color):
        self.name = name
        self.age = age
        self.size =size
        self.hair_color = hair_color
        
    def walk(self,distancia):
        print (f"Soy {self.name} y he recorrido {distancia} de distancia")
        
    def eat(self,food):
        print (f"Soy {self.name} y he comido {food}")
        
    def speak(self,language):
        print (f"Soy {self.name} y hablo {language}")
    
class Student(Person):
    def study(self,subject):
        print (f"Soy {self.name} y estudio {subject}")

class Teacher(Person):
    def teach(self,subject):
        print (f"Soy {self.name} y enseño {subject}")
    
s1=Student("Luisa", 18, 1.60, "Cafe")
t1=Teacher("Maria_Clara", 35, 1.68, "Negro")


s1.walk(16)
s1.eat("Pollo")
s1.speak("Frances")
   
t1.teach("Procesos de negocios")
