file = open('C:\PerfLogs\example.txt','r+')


l_tasks = file
inp1 = ""
list(l_tasks)
# if l_tasks == "":
#     l_tasks = []
def save_tasks(tasks):
    file.write(tasks)
def print_task(tasks):
    for i in tasks:
        print(f"{tasks.index(i) + 1} {i[0]}: {i[1]}")

def add_task(tasks,task):
    f_task = []
    f_task.append(task)
    f_task.append("не выполнено")
    tasks.append(f_task)
    return tasks

def del_task(tasks,idx):
    idx -= 1
    tasks.pop(idx)
    return tasks
# l_tasks = del_task(l_tasks,1)


def change_stat(tasks,idx=1):
    idx -= 1
    print(tasks[idx][1])
    if tasks[idx][1] == "не выполнено":
        tasks[idx][1] = "выполнено"
    else:
        tasks[idx][1] = "не выполнено"
    return tasks
# l_tasks = change_stat(l_tasks,2)
# print_task(l_tasks)

while True:
    print(f"1.Вывод таблицы\n2.Добавление задачи\n3.Удаление задачи\n4.Изменение статуса задачи\n5.Сохранить таблицу")
    inp = input("Выбирете один из вариантов: ")
    if inp == "1":
        print_task(l_tasks)
    elif inp == "2":
        inp1 = input("Какую задачу Вы хотите добавить?: ")
        l_tasks = add_task(l_tasks, inp1)
    elif inp == "3":
        inp1 = int(input("Введите номер удаляемой задачи: "))
        l_tasks = del_task(l_tasks, inp1)
    elif inp == "4":
        inp1 = int(input("Введите номер задачи для именения статуса"))
        l_tasks = change_stat(l_tasks, inp1)
    elif inp == "5":
        save_tasks(l_tasks)