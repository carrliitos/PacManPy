#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''Main method for Pacman'''

from .Game import Game
from .GameMaze import GameMaze
from .Ghost import Ghost
from .Utils import clear, argumentParser, getch

def main():
	(sizeX, sizeY, difficulty) = argumentParser()
	gameMaze = GameMaze(1, (sizeX, sizeY))
	game = Game(difficulty, gameMaze)

	for _ in range(0, difficulty):
		game.ghosts.append(Ghost(game.gameMaze.placeEnemy()))
	character = getch()

	while True:
		clear()
		game.multipleMoveNext(game.pacman)
		for i in game.ghosts:
			game.multipleMoveNext(i)

		print("Score: " + str(game.pacman.score))
		print(game.gameMaze)
		character = getch()
		while character not in ['q', 'w', 'a', 's', 'd']:
			character = getch()
		if character == 'q':
			print("Exiting...")
			exit(0)
		elif character == 'w':
			game.pacman.moveUp()
		elif character == 'a':
			game.pacman.moveLeft()
		elif character == 's':
			game.pacman.moveDown()
		elif character == 'd':
			game.pacman.moveRight()
		if game.gameMaze.coinCount == 0:
			print("LEVEL WON! BOND!")
			character = getch()
			gameMaze = GameMaze(1, (sizeX, sizeY))
			game = Game(difficulty, gameMaze, game.pacman.score)
			for i in range(0, difficulty):
				game.ghosts.append(Ghost(game.gameMaze.placeEnemy()))

if __name__ == '__main__': main()