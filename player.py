#################################################################
 #
 #		Author: Melih Furkan Güneş
 #		Github: https://github.com/furkangunes/Snakex
 #		Project: SNAKEX
 #		
 #		Player class to manage player actions in game
 #
#################################################################

import pickle

from snake import Snake
import util

class Player:
	def __init__(self, id, connection):
		self.id = id
		self.connection = connection
		self.snake = Snake(id)
		self.alive = True
		self.connected = True

	def getMessage(self):
		return pickle.loads(self.connection.recv(util.Constants.DATA_SIZE))

	def sendMessage(self, objects):
		self.connection.sendall(pickle.dumps(objects))

	def quit(self):
		try:
			self.sendMessage({util.JSONKeys.QUIT: True})
		except:
			pass

		self.connected = False