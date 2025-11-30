from typing import TypedDict, Optional


class Student(TypedDict):
    """TypedDict representing a student."""

    name: str
    grades: list[int]


def main() -> None:
    """Main program loop for the Student Grade Analyzer.

    Continuously displays a menu and performs actions based on user input.
    """
    students: list[Student] = []

    while True:
        print("\n----- Student Grade Analyzer -----")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report (all students)")
        print("4. Find top performer")
        print("5. Exit")

        choice = get_menu_choise()

        if choice == 1:
            add_student(students)
        elif choice == 2:
            add_grades(students)
        elif choice == 3:
            show_report(students)
        elif choice == 4:
            find_top_performer(students)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid option selected")


def get_menu_choise() -> int:
    """Prompt the user to select a menu option and return it as an integer.

    Returns:
        int: The chosen menu option.
    """
    while True:
        try:
            return int(input("\nEnter your choice: "))
        except ValueError:
            print("Error")


def add_student(students: list[Student]) -> None:
    """Add a new student to the students list.

    Prompts the user for a student name and validates it. Adds the student
    if the name is valid and not already in the list.

    Args:
        students (list[Student]): The list of students to update.
    """
    name = input("Enter student name: ").strip()

    if not valid_string(name):
        print("Invalid input. Please enter a valid student name.")
        return

    if get_student(students, name):
        print("This student already exists.")
        return

    students.append(Student(name=name, grades=[]))
    print(f"Student '{name}' added successfully.")


def get_student(students: list[Student], name: str) -> Optional[Student]:
    """Return a student dictionary by name or None if not found.

    Args:
        students (list[Student]): List of students to search.
        name (str): Name of the student to find.

    Returns:
        Optional[Student]: The found student dictionary, or None if not found.
    """
    for s in students:
        if s["name"].lower() == name.lower():
            return s
    return None


def add_grades(students: list[Student]) -> None:
    """Add grades for an existing student.

    Prompts the user for a student name, validates it, and allows entering
    multiple grades. Typing 'done' ends grade entry.

    Args:
        students (list[Student]): The list of students to update.
    """
    name = input("Enter student name: ").strip()
    if not valid_string(name):
        print("Invalid input. Please enter a valid student name.")
        return

    student = get_student(students, name)
    if student is None:
        print("Student not found.")
        return

    while True:
        grade = input("Enter student grade(enter 'done' to stop): ")
        if grade.lower() == "done":
            break
        try:
            grade = int(grade)
            if 0 <= grade <= 100:
                student["grades"].append(grade)
            else:
                print("Invalid grade, please enter a valid grade(0 - 100)")
        except ValueError:
            print("Invalid input, please enter a grade(number)")


def show_report(students: list[Student]) -> None:
    """Print a report of all students and their average grades.

    Skips students without grades in overall statistics but reports them as 'N/A'.
    Also prints the maximum, minimum, and overall average grades.

    Args:
        students (list[Student]): List of students to report on.
    """
    print("----- Student Report -----")
    if not students:
        print("No students added yet.")
        return

    avg_list: list[float | None] = []

    for s in students:
        avg = average(s["grades"]) if s["grades"] else "N/A"

        if avg == "N/A":
            continue

        avg_list.append(avg)

    if len(avg_list) == 0:
        print("No student has any grades yet")
        return

    print(
        f"-------------------------------\n"
        f"Max Average: {max(avg_list):.1f}\n"
        f"Min Average: {min(avg_list):.1f}\n"
        f"Overall Average: {(sum(avg_list) / len(avg_list)):.1f}\n"
        f"-------------------------------"
    )


def find_top_performer(students: list[Student]) -> None:
    """Identify and print the top-performing student based on average grades.

    Args:
        students (list[Student]): List of students to evaluate.
    """
    if not students:
        print("There are no students")
        return

    students_with_grades = [s for s in students if average(s["grades"]) is not None]

    if len(students_with_grades) == 0:
        print("No student has any grades yet")
        return

    top = max(students_with_grades, key=lambda s: average(s["grades"]) or 0)
    avg = average(top["grades"])
    print(
        f"The student with the highest average is {top['name']} with a grade of {avg:.1f}"
    )


def valid_string(value: str) -> bool:
    """Check if a string is non-empty and not purely numeric.

    Args:
        value (str): The string to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return bool(value.strip()) and not value.isdigit()


def average(grades: list[int]) -> Optional[float]:
    """Calculate the arithmetic mean of a list of grades.

    Args:
        grades (list[int]): List of integer grades.

    Returns:
        Optional[float]: The average grade, or None if the list is empty.
    """
    if not grades:
        return None
    return sum(grades) / len(grades)


if __name__ == "__main__":
    main()
