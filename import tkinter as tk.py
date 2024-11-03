import tkinter as tk
from tkinter import messagebox
import os

# Функция для создания структуры проекта с правильной обработкой вложенности
def create_structure_from_text(structure_text, base_path="."):
    project_root = os.path.join(base_path, "project")  # Создаем корневую папку "project"
    stack = [project_root]  # Стек для отслеживания текущего пути
    os.makedirs(project_root, exist_ok=True)  # Создаём папку "project" в указанной директории

    for line in structure_text.splitlines():
        # Очищаем от лишних символов и определяем вложенность
        clean_line = line.lstrip(' │├──└').strip()  # Убираем символы дерева и пробелы
        indent_level = (len(line) - len(line.lstrip(' │'))) // 4  # Уровень вложенности по отступам

        # Если строка заканчивается на '/', значит это папка
        if clean_line.endswith('/'):
            folder_name = clean_line.rstrip('/')
            # Обновляем текущий стек для правильной вложенности
            while len(stack) > indent_level + 1:
                stack.pop()
            # Создаем путь к папке
            current_path = os.path.join(*stack, folder_name)
            os.makedirs(current_path, exist_ok=True)
            stack.append(current_path)  # Добавляем текущую папку в стек
        elif clean_line:  # Если это файл
            file_name = clean_line
            # Обновляем текущий стек для правильной вложенности
            while len(stack) > indent_level + 1:
                stack.pop()
            # Создаем путь к файлу
            file_path = os.path.join(*stack, file_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Создаем папки, если они не существуют
            with open(file_path, 'w') as f:
                pass  # Создаем пустой файл

    messagebox.showinfo("Success", f"Project structure created successfully in {project_root}")

# Функция для обработки нажатия кнопки
def on_generate():
    structure_text = input_textbox.get("1.0", "end-1c")  # Получаем текст из текстового поля
    base_path = base_path_entry.get().strip() or "."  # Получаем базовый путь для создания проекта
    
    # Проверка на пустой ввод
    if not structure_text.strip():
        messagebox.showwarning("Warning", "Please enter a project structure.")
        return
    
    # Создаём структуру проекта по введённому описанию
    try:
        create_structure_from_text(structure_text, base_path)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Настройка окна приложения
root = tk.Tk()
root.title("Project Structure Generator")

# Поле для ввода базового пути
base_path_label = tk.Label(root, text="Base Path (по умолчанию: текущая директория):")
base_path_label.pack()

base_path_entry = tk.Entry(root, width=50)
base_path_entry.insert(0, "C:\\Users\\alex2\\Desktop\\test")  # Указан путь для Windows
base_path_entry.pack()

base_path_help = tk.Label(root, text="Например: C:\\Users\\alex2\\Desktop\\test", font=("Arial", 8), fg="grey")
base_path_help.pack()

# Поле для ввода структуры проекта
input_label = tk.Label(root, text="Введите структуру проекта в формате дерева:")
input_label.pack()

input_textbox = tk.Text(root, height=20, width=60)
input_textbox.insert("1.0", """\
project/
├── app/
│   ├── agents/
│   │   ├── user_interaction.py
│   │   ├── resource_search.py
│   │   ├── code_generation.py
│   │   └── testing.py
│   ├── api/
│   │   └── main.py
│   ├── models/
│   │   ├── model_manager.py
│   │   ├── self_hosted/
│   │   └── remote/
│   ├── workflows/
│   │   └── workflow_builder.py
│   ├── validators/
│   │   ├── code_validator.py
│   │   ├── code_generator.py
│   │   └── executor.py
│   └── utils/
├── config/
│   └── settings.py
├── requirements.txt
├── tests/
│   ├── test_agents/
│   ├── test_models/
│   ├── test_validators/
│   └── test_workflows/
└── main.py
""")
input_textbox.pack()

structure_help = tk.Label(root, text="Пример структуры проекта для вставки в поле выше", font=("Arial", 8), fg="grey")
structure_help.pack()

# Кнопка для запуска генерации
generate_button = tk.Button(root, text="Generate Structure", command=on_generate)
generate_button.pack()

# Запуск приложения
root.mainloop()
