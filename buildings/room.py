def singleton(cls):
	def getinstance(*args, **kwargs):
		if cls not in singleton.instances:
			singleton.instances[cls] = cls(*args, **kwargs)
		return singleton.instances[cls]

	return getinstance


singleton.instances = {}


def clearSingleton():
	# only for testing purposes
	singleton.instances = {}


@singleton
class room:
	# using decorator to make it singleton
	def __init__(self, topX, topY):
		self._validateProperties(topX, topY)
		self._topX = topX
		self._topY = topY
		self._bottomX = 0
		self._bottomY = 0

	@property
	def topCoordinates(self):
		"""
		:return: tuple of top coordinates of room
		"""
		return (self._topX, self._topY)

	@property
	def bottomCoordinates(self):
		"""
		:return: tuple of bottom coordinates of room
		"""
		return (self._bottomX, self._bottomY)

	def _validateProperties(self, x, y):
		"""
		This function will validate the coordinates taken by user input
		:param x:
		:param y:
		:return:
		"""
		flag = False
		if type(x) == int and type(y) == int:
			if x > 0 and y > 0:
				flag = True
		if flag == False:
			raise Exception("Improper Input for Room Properties")


if __name__ == "__main__":
	r1 = room(5, 5)
	print r1.bottomCoordinates, r1.topCoordinates
