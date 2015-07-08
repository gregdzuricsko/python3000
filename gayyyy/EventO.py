import json
class EventO:

	def __init__(self, name, description, day, hours, cover, age):
		self.name = name
		self.description = description
		self.day = day
		self.hours = hours
		self.cover = cover
		self.age = age


	def printStuff(self):
		print("Now printing, the EventO!\n the name is {0}, the description is {1}, the day is {2}, the hours are {3}, the cover is {4}.".format(self.name, self.description, self.day, self.hours, self.cover))

	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
