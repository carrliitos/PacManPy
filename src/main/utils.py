import argparse

try:
	from msvcrt import getch
except ImportError:
	from sys import stdin
	from termios import tcgetattr, tcsetattr, TCSADRAIN
	from tty import setraw

	def getch():
		'''GetCh wrapper for linux'''
		fileDescriptor = stdin.fileno()
		oldSetting = tcgetattr(fileDescriptor)

		try:
			setraw(fileDescriptor)
			character = stdin.read(1)
		finally:
			tcsetattr(fileDescriptor, TCSADRAIN, oldSetting)
		return character

def clear(clearNum = 100):
	'''Clears the screen by printing too many blank lines'''
	for _ in range(clearNum):
		print

def sizeParser():
	try:
		sizeX = int(raw_input("Enter the size X (odd number)\n>"))
		sizeY = int(raw_input("Enter the size Y (odd number)\n>"))
		if sizeX < 8 or sizeY < 8:
			print("Larger values please!")
			raise ValueError()
		if sizeX > 80 or sizeY > 40:
			print("Value too large!")
			raise ValueError()
		if sizeX % 2 == 0:
			sizeX += 1
		if sizeY % 2 == 0:
			sizeY += 1	
	except ValueError:
		print("Invalid input. Using defaults (35, 15)")
		(sizeX, sizeY) = (35, 15)
	return (sizeX, sizeY)

def difficultyParser():
	try:
		difficulty = int(raw_input("Enter the difficulty level(# of Ghosts)\n>"))
		if difficulty < 0:
			print("No difficulty? No way!")
			raise ValueError()
		if difficulty > 18:
			print("TOO MANY GHOSTS!")
			raise ValueError()
	except ValueError:
		print("Invalid input. Using defaults = 4 Ghosts")
		difficulty = 4
	return difficulty

def argumentParser():
	'''Parse arguments from the commandline'''
	parser = argparse.ArgumentParser()
	parser.add_argument("--legacy", action='store_true')
	parser.add_argument('-d', '--difficulty', type=int, help="Enter the difficulty [0-10]", default=4)
	parser.add_argument('-x', '--size-x', type=int, help="Enter the width", default=35)
	parser.add_argument('-y', '--size-y', type=int, help="Enter the height", default=15)
	args = parser.parse_args()

	if args.legacy:
		sizeX, sizeY = sizeParser()
		difficulty = difficultyParser()
		return (sizeX, sizeY, difficulty)

	return (args.sizeX, args.sizeY, args.difficulty)