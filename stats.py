# Accepts text as string and return number of words in the string
def word_count(text):
	word_list = text.split()
	word_count = len(word_list)
	print(f'Found {word_count} total words')
	return word_count

def character_count(text):
	char_count = {} 
	lower_text = text.lower()
	for char in lower_text:
		if char in char_count:
			char_count[char] += 1 
		else:
			char_count[char] = 1
		
	return char_count
		
	
	
def sorted_dict_list(total_char):
	sorted_items = sorted(total_char.items(), key=lambda x: x[1], reverse=True)
	new_dict_list = []
	for char, num in sorted_items:
		if char.isalpha():
			new_dict_list.append({'char': char, 'num': num})
		else:
			continue

	for char, num in sorted_items:
		print(f"{char}: {num}")


	


