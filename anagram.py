from binary_search_list_tree import BinarySearchListTree
import sys


def read_from_file(filename: str, my_tree: BinarySearchListTree[str, str]) -> None:
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            # Tests to see that only alphabetical characters are in the String
            if line.isalpha():
                # Converts the string to lowercase, sorts it as a list and converts back to a string
                sorted_string = "".join(sorted(line.lower()))
                print("Inserting:", line, "->", sorted_string)
                # TODO: Add word to my_tree
            else:
                print("Error: Input string %s from file %s" % (line, filename))


def menu() -> None:
    my_tree = BinarySearchListTree()
    quit_program = False
    options = ["Prac7 Anagram Tree Menu Options:",
               "Read String",
               "Read File",
               "List",
               "Search",
               "Quit"]

    while not quit_program:
        print()
        for i, option in enumerate(options):
            optnum = "%d. " % i if i > 0 else ""
            print(optnum, option, sep="")

        command = input("Please press a number, then <enter>: ").strip()

        if command == "1":                                   # Read string
            input_string = input("Please enter a string: ").strip()
            # Tests to see that only alphabetical characters are in the String
            if input_string.isalpha():
                # Converts the string to lowercase, sorts it as a list and converts back to a string
                sorted_string = "".join(sorted(input_string.lower()))
                print("Inserting:", input_string, "->", sorted_string)
                # TODO: Add string to my_tree
            else:
                print("ERROR: String not alphanumerical or zero length")

        elif command == "2":                                  # Read file
            filename = input("Filename: ")
            try:
                read_from_file(filename, my_tree)
            except IOError:
                print("Error reading from file:", filename)

        elif command == "3":                                  # List words in BST
            pass

        elif command == "4":                                  # Search
            input_string = input("Search string: ").strip()
            # Tests to see that only alphabetical characters are in the String
            if input_string.isalpha():
                # Converts the string to lowercase, sorts it as a list and converts back to a string
                sorted_string = "".join(sorted(input_string.lower()))
                print("Searching:", input_string)
                # TODO: Add search code
            else:
                print("Error: please enter a good string")

        elif command == "5":                                   # Quit
            quit_program = True

        else:
            print("Human Error: unrecognised command number!")

    sys.exit("YOU QUITTER")


if __name__ == '__main__':
    menu()
