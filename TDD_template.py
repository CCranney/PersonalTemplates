import unittest
# import files/functions to test here, such as 'from mycode import *''

class MyTest(unittest.TestCase):

    #example code
    def test_hello(self): self.assertEqual(hello_world(), 'hello world')


#don't alter - this allows running 'python TDD_template.py' to run the test cases
if __name__ == '__main__':
    unittest.main()
