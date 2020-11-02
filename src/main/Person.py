class Person(object):
	'''Generic object for persons'''
	def __init__(self, position):
		object.__init__(self)
		self.position = list(position)
		self.directionVector = (0, 0)

	def moveUp(self):
		'''Moves up'''
		self.directionVector = (0, -1)

	def moveDown(self):
		'''Moves down'''
		self.directionVector = (0, 1)

	def moveLeft(self):
		'''Moves left'''
		self.directionVector = (-1, 0)

	def moveRight(self):
		'''Moves right'''	
		self.directionVector = (1, 0)

	def getCurrent(self):
		'''Gets current position'''
		return self.position[::]

	def moveNext(self):
		'''Moves next position'''
		self.position[0] += self.directionVector[0]
		self.position[1] += self.directionVector[1]

	def getNext(self):
		'''Gets tentative next position'''
		return (self.position[0] + self.directionVector[0], self.position[1] + self.directionVector[1])