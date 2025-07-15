from project import Project
import datetime

def load_projects(filename):
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split('\t')
            name, start_date, priority, cost_estimate, completion = parts
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion)))
    return projects

def save_projects(filename, projects):
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                           f"{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    print("Incomplete projects: ")
    for project in sorted([p for p in projects if not p.is_complete()]):
        print(f"  {project}")
    print("Completed projects: ")
    for project in sorted([p for p in projects if p.is_complete()]):
        print(f"  {project}")

def filter_projects(projects, date_string):
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in sorted(projects, key=lambda p: datetime.datetime.strptime(p.start_date, "%d/%m/%Y").date()):
        project_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if project_date > date:
            print(project)

def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion))

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_completion:
        project.completion_percentage = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)

def main():
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")
    menu = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n" \
           "(A)dd new project\n(U)pdate project\n(Q)uit"
    print(menu)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects(projects, date_string)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        print(menu)
        choice = input(">>> ").lower()
    if input("Would you like to save to projects.txt? ").lower() in ('yes', 'y'):
        save_projects("projects.txt", projects)
    print("Thank you for using custom-built project management software.")

main()
