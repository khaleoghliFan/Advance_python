# method that contain parameters
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person({self.name})"

    def __repr__(self):
        return f'Person({self.name})'
    def full_name(self,midname):
      print(f"name:{self.name}, midname:{midname}")

p=Person("ali")
p.full_name("mohammadi")
