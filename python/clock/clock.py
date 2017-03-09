import math

class Clock:
	def __init__(self, hours, minutes):

		self.hr = hours
		self.min = minutes
		self.correct_hours()
		self.correct_mins()

	def __str__(self):
		return "%02d:%02d" % (self.hr, self.min)

	def __eq__(self, other):
		return (self.min == other.min) and (self.hr == other.hr)

	def correct_hours(self):
		self.hr = self.hr % 24

	def correct_mins(self):
		self.hr += (self.min/60)
		self.hr = self.hr % 24
		self.min = self.min % 60


	def add(self, min_to_add):
		self.min += min_to_add
		self.correct_hours()
		self.correct_mins()
		return self