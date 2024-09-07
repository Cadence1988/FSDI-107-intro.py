print('hello world')


# let variable = 1;
variable = 1
variable = True
variable = 'hello'

array = [1, 2, 3, 4, 5] 
print(array[4])
array.append(6)
print(array)
array.pop()
print(array)

dict = {
    'name':'Ryan',
    'last_name':'Marlow'
    }

print(dict)
print(dict['name'])

# for(i=0; i<size; i++)
# let temp = array[i]
#console.log

for element in dict:
    print ('Ryan')

for i in dict:
    print(dict[i])

def hello():
    print('hello from python function')

hello()

input('pick a number 1 or 2: ')



# Assignment 2

# List of tasks, and each task is a dictionary
tasks = [
    {"id": 1, "title": "take trash to curb", "completed": False},
    {"id": 2, "title": "pull steak from freezer", "completed": True},
    {"id": 3, "title": "Call SDGKU", "completed": False}
]

# Function displaying all the tasks
def display_tasks(task_list):
    print("\nCurrent Tasks:")
    for task in task_list:
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"Task {task['id']}: {task['title']} - Status: {status}")

# Function to mark a task as completed
def complete_task(task_list, task_id):
    for task in task_list:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"\nTask '{task['title']}' has been marked as completed.")

# Function to add a new task
def add_task(task_list, task):
    task_list.append(task)
    print("\nNew task added!")

# Main execution
if __name__ == "__main__":
    display_tasks(tasks)

    # Complete a task
    complete_task(tasks, 1)

    # Display tasks after completing one
    display_tasks(tasks)

    # Adding a new task
    new_task = {"id": 4, "title": "Read a Python book", "completed": False}
    add_task(tasks, new_task)

    # Display all tasks again
    display_tasks(tasks)


