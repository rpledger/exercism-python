class Clock:
	def __init__(self, hours, minutes):
		self.hr = hours % 24
		if minutes >= 60:
			self.hr = (self.hr + 1) % 24
		self.min = minutes % 60

	def __repr__(self):
		return "%02d:%02d" % (self.hr, self.min)

	def add(self, min_to_add):
		if (min_to_add + self.min) >= 60:
			print self.hr
			self.hr = (self.hr + 1) % 24
			print self.hr
		self.min = (self.min + min_to_add) % 60
		return self