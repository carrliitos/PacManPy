from .Person import Person

class Pacman(Person):
	'''Generic Pacman object'''
	def __init__(self, position, score):
		Person.__init__(self, position)
		self.score = score

	def changeScore(self, numer):
		''' Changes the score'''
		self.score += number

	def collectCoin(self, score):
		'''Duplicate of changeScore'''
		self.changeScore(score)