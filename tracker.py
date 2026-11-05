tasks = {}

while True:
    task_name = input("Введите свою задачу(q для выхода) :")
    if (task_name == "q"):
        break
    task_status = input("Введите статус/описание для задачи "+task_name+" : ")
    tasks[task_name] = task_status
    print(f"✓ Задача '{task_name}' успешно добавлена!\n")

for name, status in tasks.items():
    print(name, "-" , status)
