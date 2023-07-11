#quizlet_reboot
# remaking quizlet so I can study for my exams this semester :) 

import json

terms = {}

def add_terms():
    while True:
        term = input("Enter a term (or 'q' to quit adding terms): ")
        if term == 'q':
            break
        definition = input("Enter the definition: ")
        terms[term] = definition

def save_terms(filename):
    with open(filename, 'w') as file:
        json.dump(terms, file)

def load_terms(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def quiz_terms():
    print("\nLet's begin the quiz!")
    for term, definition in terms.items():
        user_input = input("Return the term describing: {}\n".format(definition))
        while user_input != term:
            print("Incorrect! Try again.")
            user_input = input("Return the term describing: {}\n".format(definition))
        print("Correct!\n")

# File to store the terms and definitions
data_file = "terms_data.json"

# Load existing terms from the file
terms = load_terms(data_file)

# Main program loop
while True:
    print("1. Add term")
    print("2. Quiz terms")
    print("3. Save and exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        add_term()
    elif choice == "2":
        if len(terms) == 0:
            print("Please add terms before starting the quiz.\n")
        else:
            quiz_terms()
    elif choice == "3":
        save_terms(data_file)
        print("Terms saved successfully. Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.\n")