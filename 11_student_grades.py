# Student Gradebook
# Store student names and marks in a dictionary. Allow user to query by name to get marks.

def student_gradebook():
    grades = {}

    while True:
        print("\n--- Student Gradebook Menu ---")
        print("1. Add a student's marks")
        print("2. Get a student's marks")
        print("3. View all students and marks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter student name: ").strip().title()
            try:
                marks = float(input(f"Enter marks for {name}: "))
                if 0 <= marks <= 100:
                    grades[name] = marks
                    print(f"Marks for {name} added successfully.")
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input for marks. Please enter a number.")
        elif choice == '2':
            name = input("Enter student name to query: ").strip().title()
            # Check if the student's name exists in our gradebook.
            if name in grades:
                print(f"Marks for {name}: {grades[name]}")
            else:
                print(f"Student '{name}' not found in the gradebook.")
        elif choice == '3':
            if grades: # Check if the gradebook is not empty.
                print("\n--- All Student Marks ---")
                for name, marks in grades.items():
                    print(f"{name}: {marks}")
            else:
                print("Gradebook is empty.")
        elif choice == '4':
            print("Exiting Student Gradebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    student_gradebook()