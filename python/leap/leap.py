#
# Leap function
# is_leap_year(year)
# Input: Year
# Output: True of False
#

def is_leap_year(year):
	# Divisible by 4
	if year % 4 == 0:
		# Divisible by 100
		if year % 100 == 0:
			# Divisible by 400
			if year % 400 == 0:
				return True
			return False
		return True
	# Not divisible by 4
	else:
		return False