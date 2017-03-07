class Clock:
	def __init__(self, hours, minutes):
		self.hr = hours % 24
		if minutes >= 60:
			self.hr = (self.hr + (minutes % 60)) % 24
		self.min = minutes % 60
		print self.hr
		print self.min

	def __repr__(self):
		return "%02d:%02d" % (self.hr, self.min)

	def add(self, min_to_add):
		if (min_to_add + self.min) >= 60:
			self.hr = (self.hr + (int((self.min + min_to_add)/60))) % 24
		self.min = (self.min + min_to_add) % 60
		return self