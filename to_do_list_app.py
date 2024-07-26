import sys
from termcolor import colored
from datetime import date, datetime

print("\nWelcome to the", end=" ")
print(colored(" To-Do List", "cyan", attrs=["bold"]), end=" ")
print(" App!\n")

tasks = []
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

def incomplete_tasks():
    try:
        print(colored("\nIncomplete Tasks:", "grey", attrs=["underline"]))
        for index, task in enumerate(tasks):
            if task["status"] == "incomplete":
                print(colored(f"   {index + 1} • {task["name"]} ✧ DUE: {task["due_date"]} ✧ {task["priority"]}", "cyan"))
        print(colored("\nCompleted Tasks:", "grey", attrs=["underline"]))  
        for index, task in enumerate(tasks):
            if task["status"] == "complete":
                print(colored(f"   {index + 1} • {task["name"]} ✧ DUE: {task["due_date"]} ✧ {task["priority"]}", "magenta"))
    except ValueError:
            print("Please enter your task using only numbers.")
            incomplete_tasks()

def completed_tasks():
    try:
        print(colored("\nIncomplete Tasks:", "grey", attrs=["underline"]))
        for index, task in enumerate(tasks):
            if task["status"] == "incomplete":
                print(colored(f"   {index + 1} • {task["name"]} ✧ DUE: {task["due_date"]} ✧ {task["priority"]}", "cyan"))
        finished_task = int(input("Enter the number of completed task: "))
        tasks[finished_task - 1]["status"] = "complete"
        print("Your task was completed.")
    except IndexError:
        print("Your task was not found. Please enter the correct number of the task you have completed.")
        completed_tasks()
    except ValueError:
        print("Please enter your completed task using only numbers.")
        completed_tasks()

def delete_tasks():
    try:
        print(colored("\nIncomplete Tasks:", "grey", attrs=["underline"]))
        for index, task in enumerate(tasks):
            if task["status"] == "incomplete":
                print(colored(f"   {index + 1} • {task["name"]} ✧ DUE: {task["due_date"]} ✧ {task["priority"]}", "cyan"))
        print(colored("\nCompleted Tasks:", "grey", attrs=["underline"]))  
        for index, task in enumerate(tasks):
            if task["status"] == "complete":
                print(colored(f"   {index + 1} • {task["name"]} ✧ DUE: {task["due_date"]} ✧ {task["priority"]}", "magenta"))
        delete_task = int(input("Enter the number of the task you want to delete: "))
        tasks[delete_task - 1]["status"] = "delete"
        print("Task has been removed from your tasks.")
        del tasks[delete_task - 1]
    except IndexError:
        print("Your task was not found. Please enter the correct number of the task you are deleting.")
        delete_task()
    except ValueError:
        print("Please enter the task you are deleting using only numbers.") 
        delete_task()

def add_tasks(task):
    try:
        new_task = input(str("Enter your new task: ")).title()
        task["name"] = new_task
        due_date_input = input(f"Would you like to add a due date to {new_task}? (yes/no): ").lower()
    except ValueError:
        print("Please enter your task using words only.")
    if due_date_input == "yes":
        while True:
            try:
                year = int(input("Enter a year using 4 numbers: "))
                month = int(input("Enter a month using 2 numbers: "))
                day = int(input("Enter a day using 2 numbers: "))
                format_date = date(year, month, day)
                task["due_date"] = format_date
                break
            except ValueError:
                print("Unrecognized date format, please try again\n")
                continue
            except KeyError:
                print("Unrecognized date format, please try again\n")
                continue
    else:
        task["due_date"] = "-"
    priority_input = input(f"Is {new_task} high priority or low priority? (high/low): ").lower()
    if priority_input == "high":
        task["priority"] = "High Priority"
        print(f"{new_task} has been added as a high priority task.")
    else:
        task["priority"] = "Low Priority"
        print(f"{new_task} has been added as a low priority task.")
    task["status"] = "incomplete"
    tasks.append(task)

def menu_selections():
    while True:
        task = {}
        selection = input("\nPlease enter your selection: ")
        if selection == "1":
            add_tasks(task)
        elif selection == "2":
            incomplete_tasks()
        elif selection == "3":
            completed_tasks()
        elif selection == "4":
            delete_tasks()
        elif selection == "5":
            print("\nThank you for using the", end=" ")
            print(colored(" To-Do List", "cyan", attrs=["bold"]), end=" ")
            print(" App! 👋 🤠", end=" ")
            print(colored("TTFN\n", "magenta", attrs=["bold"]))
            break

to_do_list_menu()
menu_selections()
