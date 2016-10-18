import unittest
from buildings import room
from robots import insect


class TestStringMethods(unittest.TestCase):
	# testing only public method of insect
	def test_navigate(self):
		roomObj = room(5, 5)

		insectObj1 = insect(room=roomObj, initialX=1, initialY=2, initialDirection="N")
		insectObj1.navigate("LFLFLFLFF")
		self.assertEqual(insectObj1.coordinates, (1, 3, "N"))

		with self.assertRaises(Exception) as context:
			insectObj2 = insect(room=roomObj, initialX=6, initialY=2, initialDirection="N")
		self.assertTrue('out of Bounds of Room' in str(context.exception))

	def test_coordinates(self):
		roomObj = room(5, 5)
		insectObj1 = insect(room=roomObj, initialX=1, initialY=2, initialDirection="N")
		self.assertEqual(insectObj1.coordinates, (1, 2, "N"))


if __name__ == '__main__':
	unittest.main()
