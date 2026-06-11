"""
╔══════════════════════════════════════╗
║        TASK MANAGER APPLICATION      ║
║  Add · Remove · Complete · Prioritise ║
╚══════════════════════════════════════╝

Key Concepts: Lists, Dictionaries, Loops, Functions, I/O Handling
"""

import os
import datetime

# ──────────────────────────────────────────
# DATA STORE  (list of task dictionaries)
# ──────────────────────────────────────────
tasks = []          # Each task = { id, title, priority, completed, created_at }
_next_id = 1        # Auto-increment ID counter


# ──────────────────────────────────────────
# HELPER UTILITIES
# ──────────────────────────────────────────
PRIORITY_LABELS = {1: "🔴 HIGH", 2: "🟡 MEDIUM", 3: "🟢 LOW"}
PRIORITY_ORDER  = {"high": 1, "medium": 2, "low": 3}


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    print("=" * 55)
    print("          ✅  T A S K   M A N A G E R  ✅")
    print("=" * 55)


def find_task(task_id: int):
    """Return the task dict with the given ID, or None."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def display_tasks(task_list=None, title="ALL TASKS"):
    """Pretty-print a list of task dicts."""
    if task_list is None:
        task_list = tasks

    print(f"\n── {title} {'─' * max(0, 42 - len(title))}")
    if not task_list:
        print("  (no tasks to display)")
    else:
        for t in task_list:
            status   = "✔" if t["completed"] else "○"
            priority = PRIORITY_LABELS[t["priority"]]
            done_tag = " [DONE]" if t["completed"] else ""
            print(f"  [{status}] #{t['id']:>3}  {priority}  │  {t['title']}{done_tag}")
            print(f"              Created: {t['created_at']}")
    print("─" * 55)


# ──────────────────────────────────────────
# CORE FUNCTIONS
# ──────────────────────────────────────────

def add_task():
    """Prompt the user and add a new task."""
    global _next_id
    print("\n── ADD NEW TASK ─────────────────────────────────")
    title = input("  Task title: ").strip()
    if not title:
        print("  ⚠  Title cannot be empty. Task not added.")
        return

    print("  Priority  →  1) High   2) Medium   3) Low")
    choice = input("  Choose [1/2/3] (default=2): ").strip()
    priority = int(choice) if choice in ("1", "2", "3") else 2

    task = {
        "id":         _next_id,
        "title":      title,
        "priority":   priority,
        "completed":  False,
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    _next_id += 1
    print(f"  ✅ Task #{task['id']} '{title}' added successfully!")


def remove_task():
    """Remove a task by ID."""
    print("\n── REMOVE TASK ──────────────────────────────────")
    display_tasks()
    try:
        task_id = int(input("  Enter Task ID to remove (0 to cancel): "))
    except ValueError:
        print("  ⚠  Invalid input.")
        return

    if task_id == 0:
        return

    task = find_task(task_id)
    if task is None:
        print(f"  ⚠  No task found with ID #{task_id}.")
        return

    tasks.remove(task)
    print(f"  🗑  Task #{task_id} '{task['title']}' removed.")


def mark_completed():
    """Toggle the completed flag on a task."""
    print("\n── MARK TASK AS COMPLETED ───────────────────────")
    pending = [t for t in tasks if not t["completed"]]
    display_tasks(pending, "PENDING TASKS")

    try:
        task_id = int(input("  Enter Task ID to mark complete (0 to cancel): "))
    except ValueError:
        print("  ⚠  Invalid input.")
        return

    if task_id == 0:
        return

    task = find_task(task_id)
    if task is None:
        print(f"  ⚠  No task found with ID #{task_id}.")
        return

    task["completed"] = True
    print(f"  🎉 Task #{task_id} '{task['title']}' marked as completed!")


def view_tasks():
    """Show tasks filtered by status or priority."""
    print("\n── VIEW TASKS ───────────────────────────────────")
    print("  1) All tasks")
    print("  2) Pending only")
    print("  3) Completed only")
    print("  4) Sort by priority")
    choice = input("  Choose [1-4]: ").strip()

    if choice == "1":
        display_tasks()
    elif choice == "2":
        display_tasks([t for t in tasks if not t["completed"]], "PENDING TASKS")
    elif choice == "3":
        display_tasks([t for t in tasks if t["completed"]], "COMPLETED TASKS")
    elif choice == "4":
        sorted_tasks = sorted(tasks, key=lambda t: t["priority"])
        display_tasks(sorted_tasks, "TASKS BY PRIORITY")
    else:
        print("  ⚠  Invalid choice.")


def change_priority():
    """Update the priority of an existing task."""
    print("\n── CHANGE PRIORITY ──────────────────────────────")
    display_tasks()
    try:
        task_id = int(input("  Enter Task ID to reprioritise (0 to cancel): "))
    except ValueError:
        print("  ⚠  Invalid input.")
        return

    if task_id == 0:
        return

    task = find_task(task_id)
    if task is None:
        print(f"  ⚠  No task found with ID #{task_id}.")
        return

    print("  New Priority  →  1) High   2) Medium   3) Low")
    choice = input("  Choose [1/2/3]: ").strip()
    if choice not in ("1", "2", "3"):
        print("  ⚠  Invalid choice.")
        return

    old_label = PRIORITY_LABELS[task["priority"]]
    task["priority"] = int(choice)
    new_label = PRIORITY_LABELS[task["priority"]]
    print(f"  🔄 Task #{task_id} priority changed: {old_label} → {new_label}")


def show_summary():
    """Display a quick statistics summary."""
    total     = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending   = total - completed
    high      = sum(1 for t in tasks if t["priority"] == 1 and not t["completed"])

    print("\n── SUMMARY ──────────────────────────────────────")
    print(f"  Total tasks  : {total}")
    print(f"  ✔ Completed  : {completed}")
    print(f"  ○ Pending    : {pending}")
    print(f"  🔴 High-pri  : {high} pending")
    print("─" * 55)


# ──────────────────────────────────────────
# MENU & MAIN LOOP
# ──────────────────────────────────────────

MENU = """
  1 · Add a new task
  2 · Remove a task
  3 · Mark task as completed
  4 · View tasks
  5 · Change task priority
  6 · Summary
  0 · Exit
"""


def main():
    # Seed with a couple of sample tasks so the app isn't empty on first run
    global _next_id
    sample_data = [
        ("Buy groceries",         2),
        ("Finish project report", 1),
        ("Call dentist",          3),
    ]
    for title, pri in sample_data:
        tasks.append({
            "id":         _next_id,
            "title":      title,
            "priority":   pri,
            "completed":  False,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        })
        _next_id += 1

    while True:
        clear_screen()
        print_banner()
        show_summary()
        print(MENU)

        choice = input("  Enter choice: ").strip()

        if   choice == "1": add_task()
        elif choice == "2": remove_task()
        elif choice == "3": mark_completed()
        elif choice == "4": view_tasks()
        elif choice == "5": change_priority()
        elif choice == "6": show_summary()
        elif choice == "0":
            print("\n  👋 Goodbye! Stay productive!\n")
            break
        else:
            print("  ⚠  Invalid option. Please choose 0-6.")

        input("\n  Press Enter to continue…")


if __name__ == "__main__":
    main()
