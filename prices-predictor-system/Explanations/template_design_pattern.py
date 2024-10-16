""""This is a referance of how the factory method design paradigm works. [Not a part of project added for understanding purposes]
    TODO: Add more information for better syncronization with Data.  
"""

from abc import ABC, abstractmethod 


# Factory Class 
class DiningExperience(ABC):
    
    def serve_dinner(self):
        self.serve_appetizer()
        self.serve_main_course()
        self.serve_dessert()
        self.serve_beverage() 
    
    @abstractmethod
    def serve_appetizer(self):
        pass 
    
    @abstractmethod
    def serve_main_course(self):
        pass 
    
    @abstractmethod
    def serve_dessert(self):
        pass 
    
    @abstractmethod
    def serve_beverage(self):
        pass 
    
# Conrete Class 

class ItalianDinner(DiningExperience):
    def serve_appetizer(self):
        print("Serving bruschetta as apetizer")
        
    def serve_main_course(self):
        print("Serving pasta as main course")
        
    def serve_dessert(self):
        print("Serving tiramisu as dessert")
        
    def serve_beverage(self):
        print("Serving wine as beverage")
        
class IndianDinner(DiningExperience): 
    def serve_appetizer(self):
        print("Serving Dahi Bhale as apetizer") 
        
    def serve_main_course(self):
        print("Serving Chicken tikka as main course")
        
    def serve_dessert(self):
        print("Serving Gulab jamun")
        
    def serve_beverage(self):
        None        
        
        
class DinnerManager: 
    def serve(self , dinner_type): 
        if dinner_type == 'Italian': 
            ItalianDinner().serve_appetizer
            ItalianDinner().serve_main_course
            ItalianDinner().serve_beverage 
            ItalianDinner().serve_dessert  
        elif dinner_type == 'Indian':
            IndianDinner().serve_appetizer
            IndianDinner().serve_main_course
            IndianDinner().serve_beverage
            IndianDinner().serve_dessert
        else : 
            print('Invalid dinner type') 
            
        
        

    
dinner_manager = DinnerManager() 
    
dinner_manager.serve('Italian')
dinner_manager.serve('Indian')
    