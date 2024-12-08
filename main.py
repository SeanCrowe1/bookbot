def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print("--- Begin report of books/frankstein.txt ---")
    count_words(file_contents)
    print("")
    count_characters(file_contents)
    print("--- End report ---")


def count_words(file_contents):

    individual_words = file_contents.split()
    number_of_words = len(individual_words)

    print(f"{number_of_words} words found in the document")

def count_characters(file_contents):
        
    character_list = {}
    lowercase_string = file_contents.lower()

    for character in lowercase_string:
        
        if character.isalpha():
        
            current_count = character_list.get(character, 0)
            character_list[character] = current_count + 1
    
    sorted_chars = sorted(character_list.items(), key=lambda x: x[1], reverse=True)
        
    for char, count in sorted_chars:
        print(f"The '{char}' character appears {count} times")
    
if __name__ == "__main__":
    main()
