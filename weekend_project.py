class Task:
    def __init__(self, task_id, description, completed=False):
        self.task_id = task_id
        self.description = description
        self.completed = completed

    def display_task(self):
        status = "Completed" if self.completed else "Incomplete"
        print(f"Task {self.task_id}: {self.description} - {status}")

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.task_counter = 1

    def add_task(self, description):
        task = Task(self.task_counter, description)
        self.tasks.append(task)
        self.task_counter += 1
        print(f"Task added: {task.description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                task.display_task()
    
    def edit_task_status(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = not task.completed
                print(f"Task {task_id} status updated.")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} deleted.")
                return
        print(f"Task with ID {task_id} not found.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Edit task completion status")
        print("4. Delete a task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID# to edit completion status: "))
            todo_list.edit_task_status(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID# to delete: "))
            todo_list.delete_task(task_id)
        elif choice == '5':
            print("Have a good day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()

#i had to watch like all the vids again but we did it LOL
