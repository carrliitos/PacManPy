from gameMaze import GameMaze
from pacman import Pacman
from exceptions import KillGhostException
from exceptions import KillPlayerException

class Game(object):
	'''
	Game Class
	Create a new instance, resulting in a new game
	'''
	def __init__(self, difficulty = 4, gameMaze = GameMaze(randomMaze = True), score = 0):
		object.__init__(self)
		self.difficulty = difficulty
		self.gameMaze
		self.ghosts = []
		self.pacman = Pacman(
			(gameMaze.sizeX / 2, gameMaze.sizeY * 3 / 4), score)

	def pacmanMoveNext(self, pacman):
		'''Move next for Pacman'''
		gamePoint = pacman.getCurrent()
		if not self.gameMaze.checkWall(pacman.getNext()):
			pacman.moveNext()

		if self.gameMaze.getAttribute(pacman.getCurrent()) == GameMaze.MAZE['ghost'] or self.gameMaze.getAttribute(pacman.getCurrent()) == GameMaze.MAZE['coinghost']:
			raise KillGhostException

		if self.gameMaze.getAttribute(pacman.getCurrent()) == GameMaze.MAZE['coin']:
			pacman.changeScore(1)
			self.gameMaze.coinCount = self.gameMaze.coinCount - 1

		self.gameMaze.clearAll(gamePoint)
		self.gameMaze.setAttribute(pacman.getCurrent(), GameMaze.MAZE['pacman'])

	def ghostMoveNext(self, ghost):
		'''Move next for ghost'''
		gamePoint = ghost.getCurrent()
		ghost.thinkNext(self.gameMaze, self.pacman)
		if not self.gameMaze.checkWall(ghost.getNext()) and self.gameMaze.getAttribute(ghost.getNext()) != GameMaze.MAZE['ghost'] and self.gameMaze.getAttribute(ghost.getNext()) != GameMaze.MAZE['coinghost']:
			ghost.moveNext()
		
		if self.gameMaze.getAttribute(ghost.getCurrent()) == GameMaze.MAZE['pacman']:
			raise KillPlayerException

		if self.gameMaze.getAttribute(gamePoint) == GameMaze.MAZE['coinghost']:
			self.gameMaze.setAttribute(gamePoint, GameMaze.MAZE['coin'])
		else:
			self.gameMaze.clearAll(gamePoint)

		if self.gameMaze.getAttribute(ghost.getCurrent()) == GameMaze.MAZE['coin']:
			self.gameMaze.setAttribute(ghost.getCurrent(), GameMaze.MAZE['coinghost'])
		else:
			self.gameMaze.setAttribute(ghost.getCurrent(), GameMaze.MAZE['ghost'])

	def multipleMoveNext(self, thing):
		'''Move next for all entities'''
		if thing.__class__.__name__ == 'Pacman':
			self.pacman.moveNext(thing)
		elif thing.__class__.__name__ == 'Ghost':
			self.ghost.moveNext(thing)
		else:
			print("Stop!")

	def checkGhost(self):
		'''Check if the gost is on the spot'''
		return self.gameMaze.getAttribute(self.pacman.getCurrent()) == GameMaze.MAZE['ghost']