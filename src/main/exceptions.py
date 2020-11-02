'''Custom exceptions defined for the game'''

class KillGhostException(Exception):
	'''Exception when player attemtpts to kill a ghost'''
	def __init__(self):
		Exception.__init__(self)

class KillPlayerException(object):
	'''docstring for KillPlayerException when ghost successfully
		kills a player
	'''
	def __init__(self):
		Exception.__init__(self)
