class room:
	def __init__(self, topX, topY):
		self._validateProperties(topX, topY)
		self._topX = topX
		self._topY = topY
		self._bottomX = 0
		self._bottomY = 0

	@property
	def topCoordinates(self):
		return (self._topX, self._topY)

	@property
	def bottomCoordinates(self):
		return (self._bottomX, self._bottomY)

	def _validateProperties(self, x, y):
		pass


if __name__ == "__main__":
	r = room(5,5)
	print r.bottomCoordinates,r.topCoordinates