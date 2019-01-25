import unittest
from country_codes import get_country_code

'''
16-8 测试模块country_codes ： 我们编写模块country_codes 时， 使用了print 语句来核实get_country_code() 能否按预期那样工作。 请利用你在第11
章学到的知识， 为这个函数编写合适的测试。
'''


class test_get_country_code(unittest.TestCase):
	def test_exit_code(self):
		code = get_country_code("Andorra")
		self.assertEqual(code, 'ad')
		
	def test_not_exit_code(self):
		code = get_country_code("A")
		self.assertFalse(code)
		
	def test_given_code(self):
		code = get_country_code("Yemen, Rep.")
		self.assertEqual(code, 'ye')
		
unittest.main()
		
		





