class Greeting:
    
    def __init__(self, name):
        self.name = name
         
    def greeting(self):
        print(f"Welcome {self.name}")
    
name = "Abhijit"    
message = Greeting(name)
message.greeting()    
    