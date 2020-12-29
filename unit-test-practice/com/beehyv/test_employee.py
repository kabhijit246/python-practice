import unittest
from com.beehyv.employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.emp1 = Employee("abhijit", "kumar", 22, 50000)  
        self.emp2 = Employee("aditi", "bharti", 23, 60000)
    
    def test_email(self):
        
        self.assertEqual(self.emp1.email(), "abhijit.kumar22@gmail.com")
        self.assertEqual(self.emp2.email(), "aditi.bharti23@gmail.com")
        
        self.emp1.fname = "ankit"
        self.emp2.lname = "kumari"
        
        self.assertEqual(self.emp1.email(), "ankit.kumar22@gmail.com")
        self.assertEqual(self.emp2.email(), "aditi.kumari23@gmail.com")
    
    def test_fullName(self):
        
        self.assertEqual(self.emp1.fullName(), "abhijit kumar")
        self.assertEqual(self.emp2.fullName(), "aditi bharti")
        
        self.emp1.fname = "ankit"
        self.emp2.lname = "kumari"
        
        self.assertEqual(self.emp1.fullName(), "ankit kumar")
        self.assertEqual(self.emp2.fullName(), "aditi kumari")
    
    def test_raisedSalary(self):
        
        self.emp1.raisedSalary()
        self.emp2.raisedSalary()
        
        self.assertEqual(self.emp1.salary, 75000)
        self.assertEqual(self.emp2.salary, 90000)
    
if __name__ == "__main__":
    unittest.main()    
