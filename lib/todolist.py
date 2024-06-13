import sqlite3

# SQLite database path
DATABASE_PATH = 'todo.db'

# Function to initialize database and create tasks table
def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Create tasks table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()

# Function to execute SQL queries
def execute_query(query, values=()):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    conn.close()

# Function to add a new task
def add_task(title):
    execute_query('INSERT INTO tasks (title) VALUES (?)', (title,))

# Function to list all tasks
def list_tasks():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks ORDER BY id')
    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "Complete" if task[2] == 1 else "Incomplete"
            print(f"{task[0]}: {task[1]} - {status}")

# Function to update task title
def update_task(task_id, new_title):
    execute_query('UPDATE tasks SET title = ? WHERE id = ?', (new_title, task_id))

# Function to mark task as complete or incomplete
def mark_task(task_id, completed):
    execute_query('UPDATE tasks SET completed = ? WHERE id = ?', (completed, task_id))

# Function to delete a task
def delete_task(task_id):
    execute_query('DELETE FROM tasks WHERE id = ?', (task_id,))

# Main execution
if __name__ == '__main__':
    init_db()  # Initialize the database

    while True:
        print("\nTODO List Operations")
        print("1. Add task")
        print("2. List tasks")
        print("3. Update task title")
        print("4. Mark task as complete/incomplete")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
            print(f"Task '{title}' added successfully.")

        elif choice == '2':
            list_tasks()

        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_title = input("Enter new title: ")
            update_task(task_id, new_title)
            print(f"Task with ID {task_id} updated successfully.")

        elif choice == '4':
            task_id = int(input("Enter task ID to mark: "))
            completed = input("Mark as complete? (y/n): ").lower() == 'y'
            mark_task(task_id, 1 if completed else 0)
            status = "Complete" if completed else "Incomplete"
            print(f"Task with ID {task_id} marked as {status}.")

        elif choice == '5':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
            print(f"Task with ID {task_id} deleted successfully.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")
