from robot import robot


class insect(robot):
	TURN_COMMAND_SET = set(['L', 'R'])  # permissible instruction set to turn
	MOVE_COMMAND_SET = set(['F'])  # permissible instruction set to move

	DIRECTIONS = ['N', 'E', 'S', 'W']  # permissible directions

	def __init__(self, initialX, initialY, initialDirection, room):
		super(insect, self).__init__(room=room)  # calling parent constructor
		self._validateProperties(initialX, initialY, initialDirection)
		self._posX = initialX
		self._posY = initialY
		self._indexDirection = insect.DIRECTIONS.index(initialDirection)
		self._validateCurrentPosition()

	@property
	def coordinates(self):
		"""
		Overridden Property
		:return: tuple of current coordinates of insect
		"""
		return (self._posX, self._posY, insect.DIRECTIONS[self._indexDirection])

	def _turnPosition(self, command):
		"""
		This function updates the coordinates based on command mentioned in TURN_COMMAND_SET
		:param command:
		:return:
		"""
		if command == 'R':
			self._indexDirection = (self._indexDirection + 1)
			if self._indexDirection == len(insect.DIRECTIONS):
				self._indexDirection = 0
		elif command == 'L':
			self._indexDirection = (self._indexDirection - 1)
			if self._indexDirection < 0:
				self._indexDirection = len(insect.DIRECTIONS) - 1
		else:
			raise Exception("Unknown Error: Insect")  # as this

	def _validateCurrentPosition(self):
		"""
		This function validates the current position of insect
		:return:
		"""
		if not (self._isValidCurrentPosition()):
			raise Exception("Insect Coordinates Are out of Bounds of Room")

	def _isValidCurrentPosition(self):
		"""
		:return: Bool value(T: if insect is in bounds of room else F)
		"""
		topCoordinatesRoom = self._deployedRoom.topCoordinates
		botttomCoordinatesRoom = self._deployedRoom.bottomCoordinates
		flag = False
		if self._posX >= botttomCoordinatesRoom[0] and self._posY >= botttomCoordinatesRoom[1] and self._posX <= \
				topCoordinatesRoom[0] and self._posY <= topCoordinatesRoom[1]:
			flag = True

		return flag

	def _movePosition(self, command):
		"""
		This function updates the coordinates based on command mentioned in MOVE_COMMAND_SET
		:param command:
		:return:
		"""
		_posX = self._posX
		_posY = self._posY
		if command == 'F':
			if self._indexDirection == 0:
				self._posY += 1
			elif self._indexDirection == 1:
				self._posX += 1
			elif self._indexDirection == 2:
				self._posY -= 1
			else:
				self._posX -= 1
			if not (self._isValidCurrentPosition()):
				# if going out of bound revert it back
				self._posY = _posY
				self._posX = _posX
				raise Exception("Invalid Instruction Set for Insect")
		else:
			raise Exception("Unknown Error: Insect")

	def _validateProperties(self, initialX, initialY, initialDirection):
		"""
		This function validates the 3 properties entered by user input
		:param initialX:
		:param initialY:
		:param initialDirection:
		:return:
		"""
		flag = False
		if type(initialX) == int and type(initialY) == int and type(initialDirection) == str:
			if initialDirection in insect.DIRECTIONS and initialX >= 0 and initialY >= 0:
				flag = True

		if flag == False:
			raise Exception("Improper Input Coordinates for Insect Properties")

	def _validateSequenceOfCommands(self, sequence):
		"""
		This function validates the instruction sequence, given by user input
		:param sequence:
		:return:
		"""
		for command in sequence:
			if command not in insect.TURN_COMMAND_SET and command not in insect.MOVE_COMMAND_SET:
				raise Exception("Invalid Input Sequence for Insect")

	def navigate(self, sequence):
		"""
		This function(overridden) will take instruction sequence as input, and move the insect to its new position
		:param sequence:
		:return:
		"""
		self._validateSequenceOfCommands(sequence)
		try:
			for command in sequence:
				if command in insect.TURN_COMMAND_SET:
					self._turnPosition(command)
				else:
					self._movePosition(command)
		except Exception as e:
			# most prob error occured because of index out of room bounds
			print e, " Error Occured: Can't move Further"
