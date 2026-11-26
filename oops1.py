# intialize a class
class employee:
   # special methods/magic method/dunder method - constructor
   def __init__(self):
      print("started executing attributes/data")
      self.id = 123
      self.salary = 50000
      self.designation = "SDE"
      print("attributes/data have been initiated")



   def travel(self,destination ):
        print("this travel funtion was called manually")
        print(f"Employee is now travelling to {destination}")


 # CREATE AN ONJ/INSTANCE OF THE CLASS 
sam = employee()

# printing the atrribute
# print(sam.salary)
# print(sam.id)

# calling a method 
# sam.travel("keral")


print(type(sam))


