# Student Grade Calculator

# Student Grade Calculator

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! Keep improving."
    elif marks >= 60:
        return "D", "You passed. Try to do better!"
    else:
        return "F", "Don't give up! Work harder next time."


def get_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Please enter a valid number.")


while True:
    name = input("\nEnter student name: ")

    marks = get_marks()

    grade, message = calculate_grade(marks)

    print("\n📊 RESULT FOR", name.upper())
    print("Marks:", marks, "/100")
    print("Grade:", grade)
    print("Message:", message)

    again = input("\nDo you want to check another student? (yes/no): ").lower()
    if again != "yes":
        print("Program ended. Thank you! 😊")
        break