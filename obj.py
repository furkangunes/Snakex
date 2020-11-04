#################################################################
 #
 #		Author: Melih Furkan Güneş
 #		Github: https://github.com/furkangunes/Snakex
 #		Project: SNAKEX
 #		
 #		Simple class to represent objects on the board
 #
#################################################################

import util

class Obj:
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color

	def next(self, dir):
		obj_size = util.Constants.OBJECT_SIZE

		if dir == util.Directions.LEFT:
			return Obj(self.x, self.y - obj_size, self.color)

		if dir == util.Directions.RIGHT:
			return Obj(self.x, self.y + obj_size, self.color)

		if dir == util.Directions.UP:
			return Obj(self.x - obj_size, self.y, self.color)

		if dir == util.Directions.DOWN:
			return Obj(self.x + obj_size, self.y, self.color)

		return None

	# Does not compare color
	def equals(self, obj):
		obj_size = util.Constants.OBJECT_SIZE
		return abs(obj.x - self.x) < obj_size and abs(obj.y - self.y) < obj_size

	def inLimits(self, width, height):
		return 0 < self.y < width and 0 < self.x < height

	def print(self):
		print("(" + str(self.x) + ", " + str(self.y) + " -> " + str(self.color), end = " ")