from abc import ABCMeta, abstractmethod, abstractproperty


class robot:
	__metaclass__ = ABCMeta

	def __init__(self, room):
		self._deployedRoom = room  # as each robot will be deployed in some room only, although it is not clear the coordinate system of child robot

	@abstractproperty
	def coordinates(self):
		# each robot should have some coordinates, irrespective of the coordinate system
		pass

	@abstractmethod
	def navigate(self):
		# each robot is a spy, so will navigate
		pass
