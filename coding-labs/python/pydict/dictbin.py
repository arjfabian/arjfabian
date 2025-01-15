import json
from difflib import get_close_matches

SOURCE_DICT = 'data.json'

def binary_search_with_tolerance(sorted_keys, word):
  """
  Performs binary search on a sorted list of keys, with tolerance for case
  differences.

  Args:
    sorted_keys: A sorted list of keys.
    word: The word to search for.

  Returns:
    The index of the word in the list if found, otherwise -1.
  """
  left = 0
  right = len(sorted_keys) - 1

  while left <= right:
    mid = (left + right) // 2
    if sorted_keys[mid].lower() == word:
      return mid
    elif sorted_keys[mid].lower() < word:
      left = mid + 1
    else:
      right = mid - 1

  # Check for closest match after binary search
  if left < len(sorted_keys) and sorted_keys[left].lower() == word:
    return left
  elif right >= 0 and sorted_keys[right].lower() == word:
    return right
  return -1

def search_in_dictionary(word):
  """
  Searches for the given word in the dictionary.

  Args:
    word: The word to search for.

  Returns:
    A list: 
      - First element: "d" if found, "p" if not found.
      - Subsequent elements: Definitions of the word if found, 
                              or possible close matches if not found.
  """
  with open(SOURCE_DICT) as f:
    data = json.load(f)

  # Sort keys case-insensitively
  sorted_keys = sorted(data.keys(), key=str.lower) 

  word = word.lower()
  index = binary_search_with_tolerance(sorted_keys, word)

  if index != -1:
    return ["d"] + data[sorted_keys[index]] 
  else:
    possible = get_close_matches(word, sorted_keys)
    return ["p"] + possible

def print_definitions(word, definitions):
  """
  Prints the word and its definitions in a formatted manner.

  Args:
    word: The word to be printed.
    definitions: A list containing "d" or "p" followed by definitions or 
                  possible matches.
  """
  print()
  print(f"{word.upper()}.")
  for definition_id, definition in enumerate(definitions[1:]):
    print(f"  {definition_id+1}. {definition}")

if __name__ == '__main__':
  """
  Main function to handle user input and display results.
  """
  word = input('Enter word: ')

  if not word.isalpha():
    print('f"{word}" is not a valid word.')
    exit

  definitions = search_in_dictionary(word)

  if definitions[0] == 'p':
    print('Word not found.')
    if len(definitions) > 1:
      suggestion = definitions[1]
      confirmation = input(f'Did you mean "{suggestion}"? ')
      if confirmation.upper() == 'Y':
        print_definitions(suggestion, search_in_dictionary(suggestion))
    else:
      print(f'Please try again.')
  else:
    print_definitions(word, definitions)
