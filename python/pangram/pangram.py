# pangram

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def is_pangram(sentence):
	sent = sentence.lower()
	sent = list(sentence)
	sent.sort()
	i = 0
	for s in sent:
		if s.isalpha() is False:
			sent.remove(s)
			next
		else:
			if s == alph[i]:
				i += 1
			else:
				return False
	if not sent:
		return False
	else:
		return True
