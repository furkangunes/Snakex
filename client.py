#################################################################
 #
 #		Author: Melih Furkan Güneş
 #		Github: https://github.com/furkangunes/Snakex
 #		Project: SNAKEX
 #		
 #		Client code to play the game
 #
 #		Can connect to a server on LAN if exists
 #
 #		Usage: Run the script and wait for the game to get started
 #			   Use arrow keys to move
 #
#################################################################

import socket
from threading import Thread
from os import _exit
import pickle
import pygame
import atexit
from time import sleep

import util
import obj

class Client:
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.board = None
		try:
			self.socket.connect((util.Constants.IP, util.Constants.PORT))
			atexit.register(self.disconnect)
		except:
			print("Cannot connect to the server")
			exit()

	def disconnect(self):
		try:
			self.sendMessage({util.JSONKeys.QUIT: True})
			self.socket.close()
		except:
			pass

	# Messages are sent or received with pickle

	def getMessage(self):
		return pickle.loads(self.socket.recv(util.Constants.DATA_SIZE)) # Change pickle to use it after msg

	def sendMessage(self, message):
		self.socket.sendall(pickle.dumps(message)) # Change pickle to use it after msg
		
	def drawObject(self, obj):
		obj_size = util.Constants.OBJECT_SIZE
		pygame.draw.rect(self.board, obj.color, pygame.Rect(obj.y, obj.x, obj_size, obj_size))

	def initBoard(self):
		pygame.init()
		initial_msg = None
		width = None
		height = None
		try:
			initial_msg = self.getMessage()
			width = initial_msg[util.JSONKeys.WIDTH]
			height = initial_msg[util.JSONKeys.HEIGHT]
		except BrokenPipeError:
			print("Broken pipe")
			exit()
		except Exception as e:
			print("Error in initialization. Terminating...")
			exit()

		self.board = pygame.display.set_mode((width, height))
		self.board.fill(util.Constants.GAME_WINDOW_COLOR)
		
		pygame.display.set_caption(util.Constants.GAME_WINDOW_CAPTION)
		pygame.display.update()

	def updateBoard(self, objects):
		self.board.fill(util.Constants.GAME_WINDOW_COLOR)
		for obj in objects:
			self.drawObject(obj)

		pygame.display.update()

	def exitGame(self, thread = None):
		print("Quitting Game...")

		if thread:
			thread._delete()
		
		self.disconnect()

		sleep(2)

		pygame.quit()
		_exit(0)

	def sendInput(self):
		try:
			while True:
				direction = None
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						self.exitGame()

					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_LEFT:
							direction = util.Directions.LEFT
						
						elif event.key == pygame.K_RIGHT:
							direction = util.Directions.RIGHT
						
						elif event.key == pygame.K_UP:
							direction = util.Directions.UP
						
						elif event.key == pygame.K_DOWN:
							direction = util.Directions.DOWN

						if direction != None:
							self.sendMessage({util.JSONKeys.DIRECTION: direction})
		except Exception as e:
			return

	def run(self):
		self.initBoard()
		thread = Thread(target = self.sendInput)
		thread.setDaemon(True)
		thread.start()

		while True:
			msg = None
			try:
				msg = self.getMessage()
				if type(msg) is dict and util.JSONKeys.QUIT in msg.keys():
					print("Message got to quit")
					break

				else:
					self.updateBoard(msg)

			except BrokenPipeError:
				print("Broken pipe in run")
				break

			except Exception as e:
				print(e)
				break

		self.exitGame(thread)

Client().run()
