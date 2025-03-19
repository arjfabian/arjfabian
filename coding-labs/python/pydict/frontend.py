def print_definitions(word, definitions):
    print()
    print(f"{word.upper()}.")
    for definition_id, definition in enumerate(definitions[1:]):
        print(f"  {definition_id+1}. {definition}")


if __name__ == '__main__':
    """
    Main function to handle user input and display results.
    """
  query = input('Enter word: ')

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
