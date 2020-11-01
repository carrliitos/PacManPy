from .Gamemaze import GameMaze
from .Pacman import Pacman
from .Exceptions import KillGhostException
from .Exceptions import KillPlayerException

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

		