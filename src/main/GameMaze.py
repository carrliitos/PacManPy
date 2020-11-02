from random import randint

class GameMaze(object):
	'''Main Maze module for the whole game'''

	MAZE = dict(
		wall = 'X',
		ghost = 'G',
		pacman = 'P',
		coint = 'C',
		nothing = '.',
		coinghost = 'CG'
		)

	COLORS = dict(
		wall = '\033[95m',
        ghost = '\033[37m',
        coin = '\033[33m',
        pacman = '\033[91m',
        coinghost = '\033[47m',
        nothing = '\033[36m',
        END = '\033[0m',
		)

	def __init__(self, randomMaze = False, size = (35, 15)):
		object.__init__(self)
		self.sizeX = size[0]
		self.sizeY = size[1]
		self.coinCount = 0
		self.gameMaze = [x[:] for x in [['.'] * self.sizeX] * self.sizeY]
		self.freeSpace = set()

		for i in xrange(0, self.sizeY):
			for j in [0, self.sizeX - 1]:
				self.gameMaze[i][j] = GameMaze.MAZE['wall']
		for i in xrange(0, self.sizeX):
			for j in [0, self.sizeY - 1]:
				self.gameMaze[j][i] = GameMaze.MAZE['wall']

		if randomMaze is False:
			pass
		else:
			self.fillWall()

		self.gameMaze[self.sizeY * 3 / 4][self.sizeX / 2] = GameMaze.MAZE['pacman']
		self.fillCoin([x[:] for x in [[0] * self.sizeX] * self.sizeY])

	def placeEnemy(self):
		'''Places the enemy in map'''
		sizeX = randint(1, self.sizeX - 1)
		sizeY = randint(1, self.sizeY - 1)
		while (self.checkWall((sizeX, sizeY)) is True 
					and self.getAttribute((sizeX, sizeY)) != GameMaze.MAZE['coinghost'] 
					and self.getAttribute((sizeX, sizeY)) != GameMaze.MAZE['ghost'] 
					and self.getAttribute((sizeX, sizeY)) != GameMaze.Maze['coin'] 
					and (sizeX, sizeY) not in self.freeSpace
				):
			sizeX = randint(1, self.sizeX - 1)
			sizeY = randint(1, self.sizeY - 1)
		attribute = self.getAttribute((sizeX, sizeY))
		if attribute == GameMaze.MAZE['coin']:
			self.setAttribute((sizeX, sizeY), GameMaze.MAZE['coinghost'])
		else:
			self.setAttribute((sizeX, sizeY), GameMaze.MAZE['ghost'])
		return (sizeX, sizeY)

	def fillWall(self, gamePoint = (2, 2), count = 0.0):
		'''Fills wall in map'''

		point1 = list(gamePoint)
		point2 = [gamePoint[0], self.sizeY - gamePoint[1] - 1]
		point3 = [self.sizeX - gamePoint[0] - 1, gamePoint[1]]
		point4 = [self.sizeX - gamePoint[0] - 1, self.sizeY - gamePoint[1] - 1]

		total = self.sizeX * self.sizeY

		while point1[0] < self.sizeX / 2 and point1[1] < self.sizeY / 2:
			count += 4.0
			self.makeWall(point1)
			self.makeWall(point2)
			self.makeWall(point3)
			self.makeWall(point4)
			if randint(0, 1) == 0:
				point1[0] += 1
				point2[0] += 1
				point3[0] -= 1
				point4[0] -= 1
			else:
				point1[1] += 1
				point2[1] -= 1
				point3[1] += 1
				point4[1] -= 1

		if count / total < 0.3:
			self.fillWall((randint(3, self.sizeX - 3), randint(3, self.sizeX - 3)), count)

	def fillCoin(self, visited, gamePoint = (1, 1)):
		'''Fills coins on map'''

		if (self.checkWall(gamePoint) is True 
			or visited[gamePoint[1]][gamePoint[0]] is True 
			or self.getAttribute(gamePoint) == GameMaze.MAZE['pacman']):
			return
		self.freeSpace.add(gamePoint)
		visited[gamePoint[1]][gamePoint[0]] = True
		if randint(0, 2) == 0: # Probabilisticly fill with coin
			self.makeCoint(gamePoint)
			self.coinCount = self.coinCount + 1

		self.fillCoin(visited, (gamePoint[0], gamePoint[1] + 1))
		self.fillCoin(visited, (gamePoint[0] + 1, gamePoint[1]))
		self.fillCoin(visited, (gamePoint[0], gamePoint[1] - 1))
		self.fillCoin(visited, (gamePoint[0] - 1, gamePoint[1]))

	def setAttribute(self, gamePoint, attribute):
		'''Sets attribute on point'''
		self.gameMaze[gamePoint[1]][gamePoint[0]] = attribute

	def getAttribute(self, gamePoint):
		'''Gets attribute on point'''
		return self.gameMaze[gamePoint[1]][gamePoint[0]]

	def checkWall(self, gamePoint):
		'''checks the wall'''
		return self.getAttribute(gamePoint) == GameMaze.MAZE['wall']

	def clearAll(self, gamePoint):
		'''Clears all on point'''
		self.setAttribute(gamePoint, GameMaze.MAZE['nothing'])

	def makeWall(self, gamePoint):
		'''Makes the wall'''
		self.setAttribute(gamePoint, GameMaze.MAZE['coin'])

	def __str__(self):
		string = ''
		for i in self.gameMaze:
			for j in i:
				if j == GameMaze.MAZE['wall']:
					string += GameMaze.COLORS['wall'] + j + GameMaze.COLORS['END'] + ' '
				elif j == GameMaze.MAZE['coin']:
					string += GameMaze.COLORS['coin'] + j + GameMaze.COLORS['END'] + ' '
				elif j == GameMaze.MAZE['pacman']:
					string += GameMaze.COLORS['pacman'] + j + GameMaze.COLORS['END'] + ' '
				elif j == GameMaze.MAZE['ghost']:
					string += GameMaze.COLORS['ghost'] + j + GameMaze.COLORS['END'] + ' '
				elif j == GameMaze.MAZE['coinghost']:
					string += GameMaze.COLORS['coinghost'] + GameMaze.MAZE['ghost'] + GameMaze.COLORS['END'] + ' '
				elif j == GameMaze.MAZE['nothing']:
					string += GameMaze.COLORS['nothing'] + j + GameMaze.COLORS['END'] + ' '
				else:
					string += j + ' '

			string += j + ' '
		return string

	__repr__ = __str__