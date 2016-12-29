class Employee:
   'Common base class for all employees'
   empCount = 0
   status=False

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   @staticmethod	
   def getStatus():
	return Employee.status
  
   @staticmethod	
   def setStatus(value):
	Employee.status=value
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


