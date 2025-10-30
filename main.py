import sys 
from stats import word_count, character_count, sorted_dict_list

print(f"main.py: {sys.argv[0]}")
if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
file_path = sys.argv[1]
	


	# open text file and print it out 
def get_book_text(): 
	with open(file_path) as f:
		file_contents = f.read()
		return file_contents
			
def main():
	text = get_book_text()
	print("=========== BOOKBOT ===========")
	print(f"Analyzing book from at {file_path}...")

	print("----------- Word Count -----------")
	word_count(text)	
	total_char = character_count(text)
	print("--------- Character Count ---------")
	sorted_dict = sorted_dict_list(total_char)
	print(sorted_dict)

main() 


