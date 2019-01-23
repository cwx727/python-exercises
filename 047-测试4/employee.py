class Employee():
	def __init__(self, second_name, first_name, salary):
		self.second_name = second_name
		self.first_name = first_name
		self.salary = salary
		
	def give_raise(self, raise_salary = 5000):
		self.final_salary = int(self.salary) + raise_salary
		return self.final_salary
		
	def show_employee(self):
		print(self.second_name + ' ' + self.first_name +"'s salary is "+ str(self.final_salary))

if __name__ == '__main__':	
	#类中自测，外部无法调用
	employee = Employee('a','b', 50000)
	employee.give_raise()
	employee.show_employee()
	employee.give_raise(4000)
	employee.show_employee()

