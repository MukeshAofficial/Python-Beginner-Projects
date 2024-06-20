tasks=[]

def add_task(task):
    tasks.append(task)

def remove_task(task):
    tasks.remove(task)

def view_task():
    for task in tasks:
        print(f'-{task}')

while True:
    print('\n1. Add Task \n2. Remove task \n3. View task \n4. Exit')
    choice=input('Enter Your choice:')
    if choice=='1':
        task=input('Enter the task: ')
        tasks.append(task)
    elif choice=='2':
        task=input('Enter the task to remove: ')
        tasks.remove(task)
    elif choice=='3':
        view_task()
    elif choice=='4':
        print('GOodBye!')
        break
    else:
        print('Invalid options. Please try again')

