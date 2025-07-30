def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

def student_mark_entry():
    name = input("Enter student name: ")
    m1 = int(input("Enter mark 1: "))
    m2 = int(input("Enter mark 2: "))
    m3 = int(input("Enter mark 3: "))

    total = m1 + m2 + m3
    avg = total / 3
    grade = calculate_grade(avg)

    result = f"\nName: {name}\nTotal: {total}\nAverage: {avg:.2f}\nGrade: {grade}\n"

    with open("student_results.txt", "a") as file:
        file.write(result)

    print(result)

def view_results():
    try:
        with open("student_results.txt", "r") as file:
            print("\n=== Saved Results ===")
            print(file.read())
    except FileNotFoundError:
        print("No records found yet.")

while True:
    print("\n1. Enter Marks")
    print("2. View Saved Results")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        student_mark_entry()
    elif choice == "2":
        view_results()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
