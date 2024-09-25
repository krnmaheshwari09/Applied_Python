class Employee:
	count = 0
	def __init__(self, name, position, salary):
		self.name = name
		self.position = position
		self.salary = salary
		Employee.count += 1

	def displayCount(self):
		print(f"There are {Employee.count} employees")

	def displayDetails(self):
		print(f"Name : {self.name}, Position : {self.position}, Salary : {self.salary}")


emp1 = Employee("Karan", "HR", 10000000)
emp2 = Employee("CP", "CA", 3000000)

emp1.displayCount()

print("-------------Information About Employees-------------")
emp1.displayDetails()
emp2.displayDetails()
