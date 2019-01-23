import unittest
from employee import Employee

class test_give_default_raise(unittest.TestCase):
	def setUp(self):
		second_name = 'Bob'
		first_name = 'Dayln'
		salary = 50000
		self.employee = Employee(second_name, first_name, salary)
		self.employee.defult_raise_salary = 5000
		
	def test_give_default_raise(self):		
		final_salary = self.employee.give_raise()
		expected_result = self.employee.salary + self.employee.defult_raise_salary
		self.assertEqual(final_salary, expected_result)

	def test_give_custom_raise(self):
		custom_raise_salary = 4000
		final_salary = self.employee.give_raise(custom_raise_salary)
		expected_result = self.employee.salary+custom_raise_salary
		self.assertEqual(final_salary, expected_result)	

unittest.main()	



