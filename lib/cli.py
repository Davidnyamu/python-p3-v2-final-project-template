import sqlite3
import os

# SQLite database path
DATABASE_PATH = 'todo.db'

# Function to execute SQL queries
def execute_query(query, values=()):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    conn.close()

def create_tasks_table():
    query = '''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    );
    '''
    execute_query(query)

def add_task(title):
    create_tasks_table()  # Ensure tasks table exists
    execute_query('INSERT INTO tasks (title) VALUES (?)', (title,))

def list_tasks():
    create_tasks_table()  # Ensure tasks table exists
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

def update_task(task_id, title):
    create_tasks_table()  # Ensure tasks table exists
    execute_query('UPDATE tasks SET title = ? WHERE id = ?', (title, task_id))

def mark_task(task_id, completed):
    create_tasks_table()  # Ensure tasks table exists
    execute_query('UPDATE tasks SET completed = ? WHERE id = ?', (completed, task_id))

def delete_task(task_id):
    create_tasks_table()  # Ensure tasks table exists
    execute_query('DELETE FROM tasks WHERE id = ?', (task_id,))

if __name__ == '__main__':
    # Check if database file exists, create it if not
    if not os.path.exists(DATABASE_PATH):
        open(DATABASE_PATH, 'w').close()  # Create an empty file

    while True:
        print("\nTODO List CLI")
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
