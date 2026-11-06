import json

#----------------- БЛОК ЧТЕНИЯ ФАЙЛА ----------------
try:
    with open('tasks.json','r',encoding='utf-8') as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = {}
except json.JSONDecodeError:
    tasks = {}
    print("Файл поврежден. Программа запущена без старых задач.")


#--------- БЛОК ЗАПИСИ ЗАДАЧ И ИХ СТАТУСА ------------
while True:
    task_name = input("Введите свою задачу(q для выхода) : ")
    if (task_name == "q"):
        break
    task_status = input("Введите статус/описание для задачи "+task_name+" : ")
    tasks[task_name] = task_status
    print(f"✓ Задача '{task_name}' успешно добавлена!\n")

with open("tasks.json","w",encoding = 'utf-8') as f:
    json.dump(tasks,f,ensure_ascii = False)


#---------------- БЛОК ВЫВОДА ЗАДАЧ ----------------------
answer = input("Желаете посмотреть какие задачи у вас есть? (Y/N): ")

if answer.lower() == 'y':
    print("\nВаши задачи:")
    for name, status in tasks.items():
        print(name, "-", status)