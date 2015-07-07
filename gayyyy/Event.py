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
			