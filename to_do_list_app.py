import sys
from termcolor import colored

print("\nWelcome to the", end=" ")
print(colored(" To-Do List", "cyan", attrs=["bold"]), end=" ")
print(" App!\n")

tasks = []
incomplete_tasks = []
incomplete_tasks_high_priority = []
completed_tasks = []
due_dates = []


def to_do_list_menu():
    print(colored("\nMenu:", "grey", attrs=["underline"]))
    print(colored("1.", "cyan", attrs=["bold"]), end=" ")
    print(colored("Add a Task", "grey"))
    print(colored("2.", "cyan", attrs=["bold"]), end=" ")
    print(colored("View Tasks", "grey"))
    print(colored("3.", "cyan", attrs=["bold"]), end=" ")
    print(colored("Mark Task Complete", "grey"))
    print(colored("4.", "cyan", attrs=["bold"]), end=" ")
    print(colored("Delete Task", "grey"))
    print(colored("5.", "cyan", attrs=["bold"]), end=" ")
    print(colored("Quit", "grey"))
    

def menu_selections():
    from datetime import date, datetime
    while True:
        task = {}
        c_task = {}
        selection = input("\nPlease enter your selection: ")
        if selection == "1":
            try:
                new_task = input(str("Enter your new task: ")).title()
                task["name"] = new_task
                due_date_input = input(f"Would you like to add a due date to {new_task}? (yes/no): ").lower()
            except ValueError:
                print("Please enter your task using words only.")
            if due_date_input == "yes":
                try:
                    year = int(input("Enter a year using 4 numbers: "))
                    month = int(input("Enter a month using 2 numbers: "))
                    day = int(input("Enter a day using 2 numbers: "))
                    format_date = date(year, month, day)
                    task["due_date"] = format_date
                except ValueError:
                    print("Please enter the date using only numbers: year 0000, month 00, day 00")
            else:
                task["due_date"] = "-"
            priority_input = input(f"Is {new_task} high priority or low priority? (high/low): ").lower()
            if priority_input == "high":
                task["priority"] = "High Priority"
                print(f"{new_task} has been added to your HP tasks.")
            else:
                task["priority"] = "Low Priority"
                print(f"{new_task} has been added to your LP tasks.")
            tasks.append(task)
        elif selection == "2":
            try:
                print(colored("\nIncomplete Tasks:", "grey", attrs=["underline"]))
                for task in tasks:
                    print(colored(f"    • {task["name"]} ✧ DUE: {task["due_date"]} ✧ {task["priority"]}", "cyan"))
                # print(colored("\nIncomplete Tasks - Low Priority:", "grey", attrs=["underline"]))
                # for i_task in incomplete_tasks:
                #     print(colored(f"    • {i_task} ✧ {format_date}", "cyan"))
                print(colored("\nCompleted Tasks:", "grey", attrs=["underline"]))  
                for c_task in tasks:
                    print(colored(f"    • {c_task["name"]} ✧ DUE: {task["due_date"]} ✧ {task["priority"]}", "magenta"))
            except UnboundLocalError:
                print(colored("\nIncomplete Tasks - HIGH PRIORITY:", "grey", attrs=["underline"]))
                for in_task in incomplete_tasks_high_priority:
                    print(colored(f"    • {in_task}", "red"))
                print(colored("\nIncomplete Tasks - Low Priority:", "grey", attrs=["underline"]))
                for i_task in incomplete_tasks:
                    print(colored(f"    • {i_task}", "cyan"))
                print(colored("\nCompleted Tasks:", "grey", attrs=["underline"]))  
                for c_task in completed_tasks:
                    print(colored(f"    • {c_task}", "magenta"))
        elif selection == "3":
            finished_task = input(str("Enter your completed task: ")).title()
            c_task["name"] = finished_task
            try:
                completed_tasks.append(finished_task)
                for inc in [incomplete_tasks, incomplete_tasks_high_priority]:
                    inc.remove(finished_task)
            except ValueError:
                    print("Please enter your task in words only.")
            print(f"{finished_task} has been completed.")
        elif selection == "3":
            incomplete_tasks_high_priority.remove(finished_task)
        elif selection == "4":
            task_to_delete = input("Enter the task that you want to delete: ").title()
            if task_to_delete in incomplete_tasks:
                incomplete_tasks.remove(task_to_delete)
                print(f"{task_to_delete} has been removed from your tasks.")
            else:
                print(f"{task_to_delete} was not found in tasks.")
        elif selection == "5":
            print("Thank you for using the To-Do List App! 👋 🤠")
            break

to_do_list_menu()
menu_selections()
