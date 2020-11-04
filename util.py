#################################################################
 #
 #		Author: Melih Furkan Güneş
 #		Github: https://github.com/furkangunes/Snakex
 #		Project: SNAKEX
 #		
 #		A utility file for the game.
 #
 #		You can simply change game attributes from here
 #
#################################################################

import socket

class Directions:
	LEFT = "left"
	RIGHT = "right"
	UP = "up"
	DOWN = "down"

class Colors:
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)
	YELLOW = (0, 255, 255)

class Constants:
	IP = socket.gethostbyname(socket.gethostname())
	PORT = 5555
	DATA_SIZE = 8*2048

	OBJECT_SIZE = 5

	GAME_WINDOW = "game_window"

	GAME_WINDOW_WIDTH = 150 * OBJECT_SIZE #80 * OBJECT_SIZE
	GAME_WINDOW_HEIGHT = 150 * OBJECT_SIZE #60 * OBJECT_SIZE
	GAME_WINDOW_COLOR = Colors.BLACK
	GAME_WINDOW_CAPTION = "Snakes"

	SLEEP_TIME = 3

	FOOD_COLOR = Colors.WHITE
	SNAKE_LEN = 20

	FPS = 30
	

class JSONKeys:
	COLOR = "color"
	CONNECTION = "connection"
	ADDRESS = "address"

	GAME_STARTED = "game_started"
	GAME_OVER = "game_over"

	FPS = "fps"

	DIRECTION = "direction"

	WIDTH = "width"
	HEIGHT = "height"

	POS = "pos"

	BOARD = "board"

	QUIT = "quit"

	PLAYER_QUIT = "player_quit"
	PLAYER_DIED = "player_died"

	ATE_FOOD = "ate_food"
	FOOD = "food"

	MOVE = "move"