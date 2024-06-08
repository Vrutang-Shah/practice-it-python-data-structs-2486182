from collections import deque

class Task:
    def __init__(self, task_name, hasPriority = 'False'):
        self.task_name = task_name
        self.hasPriority = hasPriority

tasklist = deque()
def add_task(task):
    if task.hasPriority == True:
        tasklist.appendleft(task.task_name)
    else:
        tasklist.append(task.task_name)

def complete_task():
    return tasklist.popleft()

def print_task():
    for each in tasklist:
        print(each)

def main():
    #add code here
    print(tasklist)
    add_task(Task("Name List"))
    print(len(tasklist))
    print(tasklist)
    add_task(Task("Name List Priority", hasPriority=True))
    print(len(tasklist))
    print(tasklist)
    add_task(Task("Name List Non Priority"))
    print(len(tasklist))
    print(tasklist)
    complete_task()
    print(len(tasklist))
    print(tasklist)
    print_task()
    return

if __name__ == "__main__":
    main()