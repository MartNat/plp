import json
import difflib

# Load JSON data into a Python dictionary
def load_dictionary():
    with open('data_dictionary/dictionary.json') as file:
        data = json.load(file)
    return data

# Function to get definition of a word
def get_definition(word, dictionary):
    # Convert the word to lowercase for case-insensitive search
    word = word.lower()

    # If the word is in the dictionary, return its definition
    if word in dictionary:
        return dictionary[word]
    else:
        # Find similar words using difflib
        similar_words = difflib.get_close_matches(word, dictionary.keys(), n=1)
        if similar_words:
            suggestion = similar_words[0]
            suggestion_confirmation = input(f"Did you mean '{suggestion}' instead of '{word}'? (yes/no): ").lower()
            if suggestion_confirmation == 'yes':
                return dictionary[suggestion]
            else:
                return "Word not found. Please try again."
        else:
            return "Word not found. Please try again."

# Main function
def main():
    # Load the dictionary data
    dictionary = load_dictionary()

    # Input word from the user
    word = input("Enter a word to get its definition: ")

    # Get definition of the word
    definition = get_definition(word, dictionary)
    print(definition)

if __name__ == "__main__":
    main()
