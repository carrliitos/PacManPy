from random import randint
from .Person import Person

class Ghost(Person):
	'''AI based Ghost with a greedy approach'''
	def __init__(self, position, intelligence = 0):
		Person.__init__(self, position)
		self.intelligence = intelligence

	def moveTowardsPacmanGreedy(self, pacman):
		pass # TODO

	def moveTowardsPacmanSmart(self, pacman, gameMaze):
		''' A* maze approach towards pacman'''
		pass # TODO

	def moveTowardsPacmanRandom(self):
		'''Random ghost movement'''
		randomNumber = randint(0, 4)
		if randomNumber == 0:
			self.moveUp()
		elif randomNumber == 1:
			self.moveDown()
		elif randomNumber == 2:
			self.moveLeft()
		elif randomNumber == 3:
			self.moveRight()

	def thinkNext(self, gameMaze, pacman):
		if self.intelligence == 0:
			self.moveTowardsPacmanRandom()
		else:
			pass # TODO