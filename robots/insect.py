class insect:
	TURN_COMMAND_SET = set(['L', 'R'])
	MOVE_COMMAND_SET = set(['F'])

	DIRECTIONS = ['N', 'E', 'S', 'W']

	def __init__(self, initialX, initialY, initialDirection):
		self._validateProperties(initialX, initialY, initialDirection)
		self._posX = initialX
		self._posY = initialY
		self._indexDirection = insect.DIRECTIONS.index(initialDirection)

	@property
	def coordinates(self):
		return (self._posX, self._posY, insect.DIRECTIONS[self._indexDirection])

	def _turnPosition(self, command):
		if command == 'R':
			self._indexDirection = (self._indexDirection + 1)
			if self._indexDirection == len(insect.DIRECTIONS):
				self._indexDirection = 0
		elif command == 'L':
			self._indexDirection = (self._indexDirection - 1)
			if self._indexDirection < 0:
				self._indexDirection = len(insect.DIRECTIONS) - 1
		else:
			raise Exception("some error")

	def _movePosition(self, command):
		if command == 'F':
			if self._indexDirection == 0:
				self._posY += 1
			elif self._indexDirection == 1:
				self._posX += 1
			elif self._indexDirection == 2:
				self._posY -= 1
			else:
				self._posX -= 1
		else:
			raise Exception("some error")

	def _validateProperties(self, initialX, initialY, initialDirection):
		pass

	def _validateSequenceOfCommands(self, sequence):
		for command in sequence:
			if command not in insect.TURN_COMMAND_SET and command not in insect.MOVE_COMMAND_SET:
				raise Exception("not a valid sequence")

	def navigate(self, sequence):
		self._validateSequenceOfCommands(sequence)
		for command in sequence:
			if command in insect.TURN_COMMAND_SET:
				self._turnPosition(command)
			else:
				self._movePosition(command)


if __name__ == "__main__":
	ins = insect(3, 3, 'E')
	ins.navigate("FFRFFRFRRF")
	print ins.coordinates()
