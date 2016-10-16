from abc import ABCMeta, abstractmethod, abstractproperty


class robot:
	__metaclass__ = ABCMeta

	def __init__(self, room):
		self._deployedRoom = room

	@abstractproperty
	def coordinates(self):
		pass

	@abstractmethod
	def navigate(self):
		pass
