class animals:
     
    def sound(self):
        print("Meow Meow")
    
    def eat(self):
        print("Meat")    

        
class dogs(animals): 
    
    def sound(self):
        print("Bhow Bhow")
    
    def eat(self):
        print("Meat and Bone")


cat = animals()
labra = dogs()
labra.sound()
labra.eat() 
cat.eat()                
cat.sound() 
         
