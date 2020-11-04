#################################################################
 #
 #		Author: Melih Furkan Güneş
 #		Github: https://github.com/furkangunes/Snakex
 #		Project: SNAKEX
 #		
 #		Server code to run the game
 #
 #		Can accept players in LAN
 #
 #		Usage: Run the script and wait for up to 4 clients
 #			   Type start to run the game with current players
 #				 or quit to shutdown the server
 #
 #			   Change attributes in the util.py to make changes in the game
 #
#################################################################


import socket
from threading import Thread
import os
from sys import argv

from player import Player
from game import Game
import util

ip = util.Constants.IP
port = util.Constants.PORT
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((ip, port))
socket.listen(4)

id = 1
players = []
game_running = False

def getConnections():
	global id
	global players

	while True:
		print("Waiting for connections...")
		connection, address = socket.accept()
		players.append(Player(id, connection))
		print("New connection")
		id += 1
		if id > 4:
			break

def cleanUp():
	global id
	global players
	
	id = 1

	for player in players:
		player.quit()

	players = []

def disconnect():
	global socket

	cleanUp()
	socket.close()

def run():
	thread = Thread(target = getConnections)
	thread.setDaemon(True)
	thread.start()

	global players
	global socket

	while True:
		inp = input()
		
		if game_running:
			continue
		
		try:
			inp = inp.lower()
		except:
			continue

		if inp == "start":
			thread._delete()
			print("Starting Game...")
			return startGame()
			id = 1
			#thread.start()

		if inp == "quit":
			disconnect()
			break

def startGame():
	global players
	global game_running

	game_running = True
	Game(players).run()
	game_running = False
	
	print("Game is over")
	print()

	cleanUp()
	run()

run()