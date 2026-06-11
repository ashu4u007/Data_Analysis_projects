def display_menu():
    print("\n=== Academy of Magical Creatures: Grade Book ===")
    print("1. Add New Student / Add Grade")
    print("2. Update an Existing Grade")
    print("3. View Student Summary & Averages")
    print("4. View Overall Class Average")
    print("5. Exit Academy Ledger")
    print("================================================")

def main():
    # Initializing the ledger with some exemplary magical students
    grade_book = {
        "Ignis the Dragon": [85, 92, 78],
        "Breeze the Pegasus": [95, 98, 92],
        "Glimmer the Pixie": [70, 88, 82]
    }

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        # 1. Add New Student or Add a Grade
        if choice == '1':
            name = input("Enter the creature's name: ").strip()
            try:
                grade = float(input(s"Enter grade for {name}: "))
                if name in grade_book:
                    grade_book[name].append(grade)
                    print(f"✨ Added grade {grade} to {name}'s record.")
                else:
                    grade_book[name] = [grade]
                    print(f"📜 Registered {name} with an initial grade of {grade}.")
            except ValueError:
                print("❌ Invalid input! Grades must be a number.")

        # 2. Update an Existing Grade
        elif choice == '2':
            name = input("Enter the student's name to update: ").strip()
            if name in grade_book:
                print(f"Current grades for {name}: {grade_book[name]}")
                try:
                    idx = int(input(f"Which grade index would you like to change (0 to {len(grade_book[name])-1})? "))
                    if 0 <= idx < len(grade_book[name]):
                        new_grade = float(input("Enter the new grade: "))
                        old_grade = grade_book[name][idx]
                        grade_book[name][idx] = new_grade
                        print(f"🔮 Successfully transmuted {old_grade} into {new_grade} for {name}!")
                    else:
                        print("❌ That index does not exist in their record.")
                except ValueError:
                    print("❌ Please enter valid numbers for index and grade.")
            else:
                print(f"🔍 '{name}' is not found in the ledger. Perhaps check the sorting hat records?")

        # 3. View Student Summary
        elif choice == '3':
            if not grade_book:
                print("The ledger is currently empty.")
                continue
            
            print("\n--- Student Progress Report ---")
            for name, grades in grade_book.items():
                avg = sum(grades) / len(grades) if grades else 0
                print(f"• {name}: Grades: {grades} | Average: {avg:.2f}")
            print("-------------------------------")

        # 4. View Overall Class Average
        elif choice == '4':
            if not grade_book:
                print("No students registered yet!")
                continue
            
            all_grades = []
            for grades in grade_book.values():
                all_grades.extend(grades)
            
            if all_grades:
                class_avg = sum(all_grades) / len(all_grades)
                print(f"\n🏰 Overall Academy Class Average: {class_avg:.2f}")
            else:
                print("\nNo grades have been entered yet.")

        # 5. Exit
        elif choice == '5':
            print("\nClosing the ledger. May your spells succeed and your dragons fly straight! 🐉✨")
            break
        
        else:
            print("❌ Invalid choice. Please gaze into the crystal ball and select 1-5.")

if __name__ == "__main__":
    main()