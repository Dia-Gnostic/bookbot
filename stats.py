def get_wordcount(text):
	return len(text.split())

def count_characters(text):
	char_counter = {}
	for char in text:
		char = char.lower()
		if char in char_counter:
			char_counter[char] += 1
		else:
			char_counter[char] = 1
	return char_counter

def sort_on(items):
	return items["num"]

def sort_char_dict(char_count):
	char_list = []
	for key in char_count:
		char_list.append({"char": key, "num": char_count[key]})
	char_list.sort(reverse=True, key=sort_on)
	return char_list
