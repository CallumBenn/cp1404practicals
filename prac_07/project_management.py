"""
CP1404/CP5632 - Practical 07
Callum Bennett

Estimate: 70 minutes
Actual: xx minutes
"""
from xml.sax.handler import property_interning_dict

# import datetime
from project import Project
from operator import itemgetter

MENU_CHOICES = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n - (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit\n"
FILENAME = 'projects.txt'

def main():
    print("Welcome to Pythonic Project Management")
    in_file = open(FILENAME, 'r')
    default_file = load_project(in_file)
    get_choice(default_file)
    in_file.close()


def get_choice(file):
    choice = input(f"{MENU_CHOICES}\n>>> ").upper()
    while choice != "Q":
        if choice == "L":
            new_file_name = get_valid_file("Enter file name (leave blank to cancel): ")
            if new_file_name != "":
                new_file = open(new_file_name, 'r')
                file.append(load_project(new_file))
        elif choice == "S":
            save_project(file)
        elif choice == "D":
            display_project(file)
        elif choice == "F":
            filter_project(file)
        elif choice == "A":
            file.append(add_project())
        elif choice == "U":
            updated_file = update_project(file)
            if updated_file != None:
                file = updated_file
        else:
            print("Invalid choice.")
        choice = input(f"{MENU_CHOICES}\n>>> ").upper()
    save_to_file = input(f"Would you like to save to {file}? ").upper
    if save_to_file == "YES" or save_to_file == "Y":
        save_project(file)
    print("Thank you for using custom-built project management software.")


def get_valid_file(instruction):
    """Get and return file if file exists."""
    while True:
        try:
            string = input(instruction)
        except FileNotFoundError:
            print("File not found!")
        return string


def load_project(file):
    """Load and return projects from file."""
    projects = []
    file.readline()  # Ignore header
    for line in file:
        parts = line.strip().split('	')
        # print(parts) # Debugging
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        # print(project) # Debugging
        projects.append(project)
    print(f"Loaded {len(projects)} projects from {file}")
    return projects


def save_project(filename):
    """Save project to file."""
    file = open(filename, 'a')
    for line in file:
        item = " ".join(str(i) for i in line)
        print(item, file=file)
    print(f"Saved to file!")


def display_project(file):
    """Display incomplete and complete projects sorted by priority."""
    incomplete_projects = []
    complete_projects = []
    for project in sorted(file, key=itemgetter(file.priority)):
        if not file.is_complete():
            incomplete_projects.append(project)
        if file.is_complete():
            complete_projects.append(project)
    print("Incomplete projects: ")
    for item in incomplete_projects:
        print(item)
    print("Complete projects: ")
    for item in complete_projects:
        print(item)


def filter_project(file):
    """Get date and display projects which start after date, sorted by date."""
    # projects = []
    date = input("Show projects that start after date (dd/mm/yy): ")
    for line in file.sorted():
        if line.start_date >= date:
            print(line)


def add_project():
    """Get new project details to append to file."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority"))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    return project


def update_project(file):
    """Modify project's completion % and/or priority."""
    for number, project in enumerate(file):
        print(number, project)
    choice = int(input("Project choice: ")) 
    chosen_project = file[choice]
    print(chosen_project)
    try:
        percentage =  int(input("New Percentage: "))
        chosen_project.completion_percentage = percentage
        # print(chosen_project)   # Debugging
        priority = int(input("New Priority: "))
        chosen_project.priority = priority
        # print(chosen_project)  # Debugging
    except ValueError:
        return None
    file[choice] = chosen_project
    # for project in file:    # Debugging
    #     print(project) # Debugging
    return file



main()