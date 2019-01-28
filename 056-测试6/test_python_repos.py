from python_repos import url_code
import unittest




class test_python_repos(unittest.TestCase):
		
	def test_status_code(self):
		code = url_code()
		self.assertEqual(code, 200)

unittest.main()


