"""
CP1404/CP5632 - Practical 07
Callum Bennett

Estimate: 70 minutes
Actual: 190 minutes
"""
from xml.sax.handler import property_interning_dict

# import datetime
from project import Project
from operator import itemgetter

MENU_CHOICES = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit\n"


def main():
    print("Welcome to Pythonic Project Management")
    filename = 'projects.txt'
    projects = load_projects(filename)
    choice = input(f"{MENU_CHOICES}\n>>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter file name (leave blank to cancel): ")
            if filename != "":
                file = open(filename, 'r')
                projects.append(load_projects(file))
                file.close()
        elif choice == "S":
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            projects.append(add_project())
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice.")
        choice = input(f"{MENU_CHOICES}\n>>> ").upper()
    save_to_file = input(f"Would you like to save to {filename}? ").upper()
    if save_to_file == "YES" or save_to_file == "Y":
        save_projects(filename, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load and return projects from file."""
    projects = []
    try:
        file = open(filename, 'r')
        file.readline()  # Ignore header
        for line in file:
            parts = line.strip().split('	')
            # print(parts) # Debugging
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            # print(project) # Debugging
            projects.append(project)
        print(f"Loaded {len(projects)} projects from {file}")
        file.close()
    except FileNotFoundError:
        print("File not found!")
    return projects



def save_projects(filename, projects):
    """Save project to file."""
    file = open(filename, 'w')
    print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=file)
    for project in projects:
        print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=file)
    file.close()
    print(f"Saved to file!")


def display_projects(projects):
    """Display incomplete and complete projects sorted by priority."""
    incomplete_projects = []
    complete_projects = []
    for project in projects:
        # print(project.completion_percentage) # Debugging
        if project.is_complete():
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(project)
    print("Complete projects: ")
    for project in complete_projects:
        print(project)


def filter_projects(projects):
    """Get date and display projects which start after date, sorted by date."""
    # This function is unfinished - I did not have time to learn how to utilize datetime to filter and sort by start_date
    date = input("Show projects that start after date (dd/mm/yy): ")
    for project in sorted(projects):
        if project.start_date >= date:
            print(project)


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


def update_project(projects):
    """Modify project's completion % and/or priority."""
    for number, project in enumerate(projects):
        print(number, project)
    choice = int(input("Project choice: "))
    chosen_project = projects[choice]
    print(chosen_project)
    try:
        percentage =  int(input("New Percentage: "))
        chosen_project.completion_percentage = percentage
        # print(chosen_project)   # Debugging
        priority = int(input("New Priority: "))
        chosen_project.priority = priority
        # print(chosen_project)  # Debugging
    except ValueError:
        return
    projects[choice] = chosen_project
    # for project in file:    # Debugging
    #     print(project) # Debugging



main()