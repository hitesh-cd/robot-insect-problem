import unittest
from buildings import room
from buildings import clearSingleton


class TestStringMethods(unittest.TestCase):
	# testing only public method of insect
	def test_topCoordinates(self):
		roomObj = room(5, 5)
		self.assertEqual(roomObj.topCoordinates, (5, 5))
		clearSingleton()
		with self.assertRaises(Exception) as context:
			roomObj = room(5, -5)
		self.assertTrue('Improper Input' in str(context.exception))
		clearSingleton()

	def test_bottomCoordinates(self):
		roomObj = room(5, 5)
		self.assertEqual(roomObj.bottomCoordinates, (0, 0))
		clearSingleton()


if __name__ == '__main__':
	unittest.main()
