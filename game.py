#################################################################
 #
 #		Author: Melih Furkan Güneş
 #		Github: https://github.com/furkangunes/Snakex
 #		Project: SNAKEX
 #		
 #		Game code to manage the game
 #
#################################################################

from threading import Thread
import random
from time import sleep

from obj import Obj
import util

class Game:
	def __init__(self, players):
		self.players = players
		for player in self.players:
			player.alive = True

		self.threads = None

		self.food = None
		self.board = None
		self.initBoard()

	def placeObj(self, obj):
		self.board[obj.x][obj.y] = obj

	def generateFood(self):
		row = None
		col = None
		while True:
			row = random.randint(0, util.Constants.GAME_WINDOW_HEIGHT)
			col = random.randint(0, util.Constants.GAME_WINDOW_WIDTH)

			if self.board[row][col] == None:
				self.food = Obj(row, col, util.Constants.FOOD_COLOR)
				self.placeObj(self.food)
				return self.food

	def initBoard(self):
		self.board = [[None for _ in range(util.Constants.GAME_WINDOW_WIDTH)] for _ in range(util.Constants.GAME_WINDOW_HEIGHT)]
		for player in self.players:
			for obj in player.snake.pos:
				self.placeObj(obj) # Construct object class for player snake

		self.generateFood()

	def updateBoard(self):
		food_eaten = False 
		
		for player in self.players:
			if player.alive:
				head, tail = player.snake.move(self.board, self.food)
				if head == None:
					print("Player", player.id, "died", " Score:", len(player.snake.pos) - util.Constants.SNAKE_LEN)
					player.alive = False
					continue

				self.placeObj(head)

				# Tail is none if food not eaten by snake
				if not tail:
					food_eaten = True
				else:
					self.board[tail.x][tail.y] = None

			else:
				pass

		if food_eaten:
			self.generateFood()

	def broadcast(self, message):
		for player in self.players:
			if player.connected:
				try:
					player.sendMessage(message)
				except BrokenPipeError:
					player.connected = False
				except Exception:
					pass

	def broadcastBoard(self):
		objects = []
		for player in self.players:
			for obj in player.snake.pos:
				objects.append(obj)

		objects.append(self.food)

		self.broadcast(objects)

	def listenInput(self, player):
		while player.connected:
			try:
				inp = player.getMessage()
				keys = inp.keys()

				if util.JSONKeys.QUIT in keys:
					player.quit()	# set alive and connected to false
				
				elif util.JSONKeys.DIRECTION in keys:
					direction = inp[util.JSONKeys.DIRECTION]
					player.snake.changeDir(direction)
			except:
				pass

	def listenInputs(self):
		self.threads = [Thread(target = self.listenInput, args = (player, )) for player in self.players]
		for thread in self.threads:
			thread.setDaemon(True)
			thread.start()

	def endGame(self):
		#for thread in self.threads:
		#	thread._delete()

		for player in self.players:
			player.quit()

	def printBoard(self):
		for player in self.players:
			print("Player", player.id, ":")
			player.snake.print()
		print()


	def run(self):
		initial_msg = {util.JSONKeys.WIDTH: util.Constants.GAME_WINDOW_WIDTH, util.JSONKeys.HEIGHT: util.Constants.GAME_WINDOW_HEIGHT}
		self.broadcast(initial_msg)
		self.broadcastBoard()
		sleep(3)
		self.listenInputs()

		running = True
		while running:
			running = False
			for player in self.players:
				if player.alive:
					running = True
					continue
				
			self.updateBoard()
			self.broadcastBoard()
			sleep(1 / util.Constants.FPS)

		self.endGame()