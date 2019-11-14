import unittest
import Arithmetic_Operations as ao

class TestArithmetic_Operations(unittest.TestCase):

	def test_addition(self):
		self.assertEqual(ao.addition(2,3),5,"should be 5")
		self.assertEqual(ao.addition(100,-50),50,"should be 50")

	def test_subtraction(self):
		self.assertEqual(ao.subtraction(10,4),6,"should be 6")
		self.assertEqual(ao.subtraction(100,200),-100,"should be -100")

	def test_multiplication(self):
		self.assertEqual(ao.multiplication(5,2),10,"should be 10")
		self.assertEqual(ao.multiplication(30,-2),-60,"should be -60")

	def test_division(self):
		self.assertEqual(ao.division(15,5),3,"should be 3")
		self.assertEqual(ao.division(-45,5),-9,"should be -9")

if __name__ == '__main__':
    unittest.main()
