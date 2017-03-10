# pangram
import string
alph = list(string.ascii_letters)

def is_pangram(sentence):
	if not sentence:
		return False
	sent = sentence.lower()
	sent = list(set(sent))
	sent.sort()
	i = 0
	for s in sent:
		if (s.isalpha() is False) or (s == ' '):
			next
		else:
			if s == alph[i]:
				i += 1
			else:
				return False
	return True
