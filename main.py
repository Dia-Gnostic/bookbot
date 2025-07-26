from stats import get_wordcount, count_characters, sort_char_dict
import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path = sys.argv[1]
	frankenstein_text = get_book_text(path)
	num_words = get_wordcount(frankenstein_text)
	#print(f"{num_words} words found in the document")
	chars = sort_char_dict(count_characters(frankenstein_text))
	#print(chars)
	report(path, num_words, chars)

def get_book_text(file_path):
	with open(file_path) as file:
		file_contents = file.read()
		return file_contents

def report(file_path, word_count, char_list):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_path}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for pair in char_list:
		if pair["char"].isalpha():
			print(f'{pair["char"]}: {pair["num"]}')
main()

