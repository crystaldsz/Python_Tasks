# CSV Reader
# Read a CSV file containing student marks and print names of students scoring above 75%.

import csv 
def analyze_marks(file_name="student_marks.csv", pass_threshold=75):
    high_scorers = []

    try:
        with open(file_name, mode='r', newline='') as csv_file:
            data_reader = csv.reader(csv_file)
            headers = next(data_reader)
            print(f"--- Reading data from '{file_name}' ---")
            try:
                name_col = headers.index("Student Name")
                marks_col = headers.index("Marks")
            except ValueError:
                print(f"Error: CSV must have 'Student Name' and 'Marks' columns.")
                print("Check if column names are exact (case-sensitive).")
                return 
            for row in data_reader:
                if len(row) > max(name_col, marks_col):
                    try:
                        s_name = row[name_col] 
                        s_marks = int(row[marks_col]) 
                        # Check if the student's score is above our set threshold.
                        if s_marks > pass_threshold:
                            high_scorers.append((s_name, s_marks))
                    except ValueError:
                        print(f"  Warning: Skipping row '{row}' due to marks not being a number.")
                    except IndexError:
                        print(f"  Warning: Skipping row '{row}' due to missing data.")
                else:
                    print(f"  Warning: Skipping malformed row '{row}' (too few columns).")
        print("\n" + "=" * 35)
        print(f"Students Scoring Above {pass_threshold}%:")
        print("=" * 35)

        if high_scorers:
            high_scorers.sort(key=lambda x: x[1], reverse=True)
            for name, score in high_scorers:
                print(f"• **{name}**: {score}%")
        else:
            print(f"No students scored above {pass_threshold}%.")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        print(f"Please ensure '{file_name}' is in the same folder as this script.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    analyze_marks("student_marks.csv", 75)