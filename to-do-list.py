def print_tasks():
    for i, row in enumerate(task_list):
        print(f"{i+1}. {row[0]} - Due: {row[1]} - Importance: {row[2]} - Details: {row[3]}")

def edit_task(task):
    task[0] = input("What do you want to change the task to: ")
    task[1] = input("When is it due now: ")
    task[2] = input("Enter the new importance(1-4): ")
    task[3] = input("Enter any new details about the task: ")
    return task

def mark_completed():
    task_to_mark = input("Which task do you want to mark as completed? ")
    for i, row in enumerate(task_list):
        if row[0] == task_to_mark:
            row.append("Done")
            print("Task marked as completed.")
            break

def save_tasks(task_list):
    with open("tasks.txt", "w") as f:
        for task in task_list:
            f.write(",".join(str(i) for i in task) + "\n")

def load_tasks():
    global task_list
    task_list = []
    with open("tasks.txt", "r") as f:
        for line in f:
            task = line.strip().split(",")
            # Convert importance value from string to integer
            task[2] = str(task[2])
            task_list.append(task)

task_list = []

while True:
    try:
        print("""TODO List Management System
        1: Add
        2: View
        3: Mark as Completed
        4: Edit
        5: Remove
        6: Save
        7: Load
        8: Exit
        """)
        w = int(input())
        if w == 1:
            add = input("What do you want to add: ")
            due = input("When it is due: ")
            impo = input("Importance(1-4): ")
            details = input("Enter any details about the task: ")
            row = [add, due, impo, details]
            task_list.append(row)
        elif w == 2:
            print_tasks()
        elif w == 3:
            mark_completed()
        elif w == 4:
            print_tasks()
            task_to_edit = input("Enter the number of the task you want to edit: ")
            if task_to_edit.isdigit() and int(task_to_edit) > 0 and int(task_to_edit) <= len(task_list):
                task_to_edit = int(task_to_edit) - 1
                task_list[task_to_edit] = edit_task(task_list[task_to_edit])
                print("Task edited successfully.")
            else:
                raise ValueError("Invalid task number.")
        elif w == 5:
            rem = input("What do you want to remove: ")
            task_list = [row for row in task_list if row[0] != rem]
            print("Task removed successfully.")
        elif w == 6:
            save_tasks(task_list)
            print("Saved Successfully!")
        elif w == 7:
            load_tasks()
        elif w == 8:
            print("Exiting...")
            break
        else:
            raise ValueError("Invalid choice, please choose a number between 1-6.")
    except ValueError as e:
        print(e)