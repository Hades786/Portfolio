from collections import defaultdict
import time
import bisect

def load_dictionary(dictionary_file):
    """Load the dictionary from a file into a sorted list."""
    dictionary = []
    with open(dictionary_file, 'r') as file:
        for line in file:
            word = line.strip()
            if 3 <= len(word) <= 9:
                dictionary.append(word)
    return dictionary

def binary_search(word, dictionary):
    """Perform a binary search to check if the word is in the sorted dictionary."""
    index = bisect.bisect_left(dictionary, word)
    if index != len(dictionary) and dictionary[index] == word:
        return True
    return False

def build_letter_index(dictionary):
    """Build an index of words based on their letters for faster lookup."""
    letter_index = defaultdict(set)
    for word in dictionary:
        for char in set(word):  # Use set to avoid duplicate letters
            letter_index[char].add(word)
    return letter_index

def is_valid_word(word, anagram_count):
    """Checks if the word can be constructed from the anagram's letter counts."""
    word_count = defaultdict(int)
    for char in word:
        word_count[char] += 1
    
    for char in word_count:
        if word_count[char] > anagram_count[char]:
            return False
    return True

def contains_required_letter(word, required_letter):
    """Checks if the word contains the required letter."""
    return required_letter in word

def find_anagrams(anagram, dictionary, letter_index):
    """Finds valid words from the dictionary that can be made from the given anagram."""
    #sorted_anagram = ''.join(sorted(anagram)) #from previous testing
    valid_words = set()
    
    # Determine the 5th letter of the anagram as the required letter
    required_letter = anagram[4] if len(anagram) >= 5 else None
    
    if required_letter:
        anagram_count = defaultdict(int)
        for char in anagram:
            anagram_count[char] += 1
        
        # Retrieve words that contain the required letter
        possible_words = letter_index.get(required_letter, [])
        
        for word in possible_words:
            if len(word) >= 3 and is_valid_word(word, anagram_count) and contains_required_letter(word, required_letter):
                if binary_search(word, dictionary):
                    valid_words.add(word)
    
    return list(valid_words)
#preprocesses anagrams and writes to solutions
def process_anagrams(anagram_file, dictionary_file, output_file):
    dictionary = load_dictionary(dictionary_file)
    letter_index = build_letter_index(dictionary)
    
    #Read all anagrams from the txt file
    with open(anagram_file, 'r') as file:
        anagrams = [line.strip() for line in file]
    
    start_time = time.time()
    
    #Process each anagram
    with open(output_file, 'w') as output:
        for anagram in anagrams:
            valid_words = find_anagrams(anagram, dictionary, letter_index)
            # Write the anagram and numer of valid words
            output.write(f"Anagram: {anagram}\n")
            output.write(f"{len(valid_words)}\n")
            output.write("\n")

    end_time = time.time()
    print(f"Processing Time for processing anagram: {end_time - start_time} seconds")

# Timing the execution
if __name__ == "__main__":
    start_time = time.time()
    
    process_anagrams('anagrams.txt', 'dictionary.txt', 'solutions.txt')
    
    end_time = time.time()
    
    print(f"Processing Time: {end_time - start_time} seconds")
