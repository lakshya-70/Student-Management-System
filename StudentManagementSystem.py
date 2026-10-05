# 14th Github Project --> Student Management System
print("----------Student Management System----------")
students = []

def add_student():
    """Add a new student to the list."""
    print("\n--- Add Student ---")
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    grade = input("Enter student grade: ").strip()

   
    if not student_id or not name:
        print("❌ ID and Name cannot be empty!")
        return

   
    for s in students:
        if s["id"] == student_id:
            print(f"❌ A student with ID {student_id} already exists!")
            return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)
    print(f"✅ Student '{name}' added successfully!")


def view_students():
    """Display all students."""
    print("\n--- All Students ---")
    if not students:
        print("No students found.")
        return

    print(f"{'ID':<10}{'Name':<20}{'Age':<6}{'Grade':<6}")
    print("-" * 42)
    for s in students:
        print(f"{s['id']:<10}{s['name']:<20}{s['age']:<6}{s['grade']:<6}")


def search_student():
    """Find a student by ID or name."""
    print("\n--- Search Student ---")
    keyword = input("Enter ID or Name to search: ").strip().lower()

    found = [s for s in students
             if keyword in s["id"].lower() or keyword in s["name"].lower()]

    if not found:
        print("❌ No matching student found.")
        return

    print(f"\nFound {len(found)} result(s):")
    for s in found:
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")


def update_student():
    """Update an existing student's details."""
    print("\n--- Update Student ---")
    student_id = input("Enter student ID to update: ").strip()

    for s in students:
        if s["id"] == student_id:
            print(f"Current details: {s}")
            s["name"] = input(f"New name [{s['name']}]: ").strip() or s["name"]
            s["age"] = input(f"New age [{s['age']}]: ").strip() or s["age"]
            s["grade"] = input(f"New grade [{s['grade']}]: ").strip() or s["grade"]
            print("✅ Student updated successfully!")
            return

    print("❌ Student not found.")


def delete_student():
    """Remove a student from the list."""
    print("\n--- Delete Student ---")
    student_id = input("Enter student ID to delete: ").strip()

    for s in students:
        if s["id"] == student_id:
            confirm = input(f"Delete '{s['name']}'? (y/n): ").strip().lower()
            if confirm == "y":
                students.remove(s)
                print("✅ Student deleted.")
            else:
                print("Cancelled.")
            return

    print("❌ Student not found.")


def show_menu():
    """Print the main menu."""
    print("\n" + "=" * 40)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")



while True:
    show_menu()
    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter 1-6.")


