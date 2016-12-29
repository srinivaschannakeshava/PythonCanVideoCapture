import Employee
import class1

#"This would create first object of Employee class"
emp1 = Employee.Employee("Zara", 2000)
#"This would create second object of Employee class"
emp2 = Employee.Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
Employee.Employee.setStatus(True)
print "Total Employee %d" % Employee.Employee.empCount

print "Status of employee" ,Employee.Employee.getStatus()

class1.class1.changeStatus()

print "Status of employee2" ,Employee.Employee.getStatus()

class1.class1.changeStatus()

print "Status of employee3" ,Employee.Employee.getStatus()
