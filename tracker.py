import json

tasks = {}

while True:
    task_name = input("Введите свою задачу(q для выхода) : ")
    if (task_name == "q"):
        break
    task_status = input("Введите статус/описание для задачи "+task_name+" : ")
    tasks[task_name] = task_status
    print(f"✓ Задача '{task_name}' успешно добавлена!\n")

with open("tasks.json","w",encoding = 'utf-8') as f:
    json.dump(tasks,f,ensure_ascii = False)

for name, status in tasks.items():
    print(name, "-" , status)
