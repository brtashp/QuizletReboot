#quizlet_reboot
# remaking quizlet so I can study for my exams this semester :) 

terms = {}

def add_term():
    term = input("Enter a term: ")
    definition = input("Enter the definition: ")
    terms[term] = definition

def quiz_terms():
    print("\nLet's begin the quiz!")
    for term, definition in terms.items():
        user_input = input("What is {} based on the definition: {}\n".format(term, definition))
        while user_input != term:
            print("Incorrect! Try again.")
            user_input = input("What is {} based on the definition: {}\n".format(term, definition))
        print("Correct!\n")

# Main program loop
while True:
    print("1. Add term")
    print("2. Quiz terms")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        add_term()
    elif choice == "2":
        if len(terms) == 0:
            print("Please add terms before starting the quiz.\n")
        else:
            quiz_terms()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.\n")