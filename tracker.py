tasks = {}

while True:
    task_name = input("Введите свою задачу(q для выхода)")
    if (task_name == "q"):
        break
    task_status = input("Введите статус задачи "+task_name+" :")
    tasks[task_name] = task_status
    print(f"✓ Задача '{task_name}' успешно добавлена!\n")

print("Ваш список задач")
print(tasks)
