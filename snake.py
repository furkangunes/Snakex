#################################################################
 #
 #		Author: Melih Furkan Güneş
 #		Github: https://github.com/furkangunes/Snakex
 #		Project: SNAKEX
 #		
 #		Snake class for managing snakes in the game
 #
#################################################################

from copy import deepcopy

from obj import Obj
import util

width = util.Constants.GAME_WINDOW_WIDTH
height = util.Constants.GAME_WINDOW_HEIGHT
snake_len = util.Constants.SNAKE_LEN

left = util.Directions.LEFT
right = util.Directions.RIGHT
up = util.Directions.UP
down = util.Directions.DOWN

class Snake:
	def __init__(self, id):
		self.id = id
		self.pos = []
		self.dir = None
		self.color = None

		self.generateData(id)

	def generateData(self, id):
		obj_size = util.Constants.OBJECT_SIZE

		if id == 1:
			self.color = util.Colors.GREEN
			self.dir = right
			for i in range((snake_len + 1) * obj_size, obj_size, -obj_size):
				self.pos.append(Obj(obj_size, i, self.color))
		
		elif id == 2:
			self.color = util.Colors.RED
			self.dir = left
			for i in range(width - obj_size - snake_len * obj_size, width - obj_size, obj_size):
				self.pos.append(Obj(height - obj_size, i, self.color))

		elif id == 3:
			self.color = util.Colors.BLUE
			self.dir = up
			for i in range(height - obj_size - snake_len * obj_size, height - obj_size, obj_size):
				self.pos.append(Obj(i, obj_size, self.color))

		elif id == 4:
			self.color = util.Colors.YELLOW
			self.dir = down
			for i in range((snake_len + 1) * obj_size, obj_size, -obj_size):
				self.pos.append(Obj(i, width - obj_size, self.color))

		else:
			pass

	def changeDir(self, direction):
		if self.dir == left and direction == right:
			pass

		elif self.dir == right and direction == left:
			pass

		elif self.dir == up and direction == down:
			pass

		elif self.dir == down and direction == up:
			pass

		else:
			self.dir = direction

	# If eats food, returns none for tail else pos to delete

	def move(self, board, food):
		current_head = deepcopy(self.pos[0])
		head = current_head.next(self.dir)	# Obj.next
		tail = None

		if not self.posValid(head, board, food):
			return None, None

		if not head.equals(food):	# Obj.equals
			tail = deepcopy(self.pos[-1])
			del self.pos[-1]

		self.pos.insert(0, head)

		return head, tail

	def posValid(self, pos, board, food):
		if not pos.inLimits(width, height): # Obj.inLimits
			return False

		board_pos = board[pos.x][pos.y]

		if not (board_pos == None or board_pos.equals(food)):
			return False

		return True

	def print(self):
		for obj in self.pos:
			obj.print()
		print()