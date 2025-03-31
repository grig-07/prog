# Лабораторная работа №12
## Задания для самостоятельного выполнения
Сложность: Rare
По своему варианту задания и GUI фреймворка создайте пакет, содержащий 3 модуля, и подключите его к основной программе. Основная программа должна предоставлять:
- графический пользовательский интерфейс с возможностями ввода требуемых параметров и отображения результатов расчёта,
- возможность сохранить результаты в отчёт формата .doc или .xls (например, пакеты python-docx и openpyxl).графический пользовательский интерфейс с возможностями ввода требуемых параметров и отображения результатов расчёта,
## Мой GUI-ФРЕЙМВОРК - guizero.
# Задание варианта 9:
Отделочные материалы
- Обои
- Плитка
- Ламинат
- Расчёт количества и стоимости для закупки материалов в зависимости от площади.
### Решение:
## 1. Создание директории проекта
- Откройте командную строку и выполните следующие команды для создания директории проекта и перехода в нее:
```
mkdir material_calculator
cd material_calculator
```
## 2. Создание пакета package
```
mkdir package
cd package
```
## 3. Создание необходимых файлов
# 3.1. __init__.py
```
type nul > __init__.py
```
# 3.2. calculations.py
```
type nul > calculations.py
notepad calculations.py
```
- Теперь в открытом блокноте нужно вставить следующий код:
``` py
# package/calculations.py

class Material:
    def __init__(self, name, unit_price, area_per_unit):
        self.name = name
        self.unit_price = unit_price  # цена за единицу материала
        self.area_per_unit = area_per_unit  # площадь, покрываемая одной единицей материала

    def calculate_quantity(self, area):
        return (area / self.area_per_unit) + 0.5  # округляем вверх

    def calculate_cost(self, quantity):
        return quantity * self.unit_price
```
# 3.3. gui.py
```
type nul > gui.py
notepad gui.py
```
- В открытом блокноте должен быть следующий код:
``` py
# package/gui.py

from guizero import App, Text, TextBox, Combo, PushButton, Picture
from report import save_report
from calculations import Material

class MaterialApp:
    def __init__(self, app):
        self.app = app
        self.app.title("Расчет материалов")
        self.app.width = 400
        self.app.height = 300

        self.material_types = ["Обои", "Плитка", "Ламинат"]
        self.selected_material = None

        Text(self.app, text="Выберите материал:")
        self.material_choice = Combo(self.app, options=self.material_types, command=self.update_material)

        self.parameters = {}
        self.create_material_fields()

        self.calculate_button = PushButton(self.app, text="Рассчитать", command=self.calculate)
        self.save_button = PushButton(self.app, text="Сохранить отчет", command=self.save_report)

    def create_material_fields(self):
        for widget in self.app.children[2:]:
            widget.destroy()

        if self.selected_material:
            self.parameters = {}
            Text(self.app, text=f"Площадь ({self.selected_material.name}):")
            self.parameters['area'] = TextBox(self.app)

            Text(self.app, text="Цена за единицу:")
            self.parameters['unit_price'] = TextBox(self.app)

            Text(self.app, text="Площадь, покрываемая одной единицей:")
            self.parameters['area_per_unit'] = TextBox(self.app)

    def update_material(self, choice):
        self.selected_material = Material(
            name=choice,
            unit_price=0,  # значения будут введены пользователем
            area_per_unit=0
        )
        self.create_material_fields()

    def calculate(self):
        try:
            area = float(self.parameters['area'].value)
            unit_price = float(self.parameters['unit_price'].value)
            area_per_unit = float(self.parameters['area_per_unit'].value)

            self.selected_material.unit_price = unit_price
            self.selected_material.area_per_unit = area_per_unit

            quantity = self.selected_material.calculate_quantity(area)
            cost = self.selected_material.calculate_cost(quantity)

            result_text = f"Количество: {quantity:.2f} единиц\nСтоимость: {cost:.2f} руб."
            Text(self.app, text=result_text)
        except ValueError:
            error_text = "Пожалуйста, введите корректные числовые значения."
            Text(self.app, text=error_text, color="red")

    def save_report(self):
        try:
            area = float(self.parameters['area'].value)
            unit_price = float(self.parameters['unit_price'].value)
            area_per_unit = float(self.parameters['area_per_unit'].value)

            quantity = self.selected_material.calculate_quantity(area)
            cost = self.selected_material.calculate_cost(quantity)

            report_content = f"Материал: {self.selected_material.name}\nПлощадь: {area} кв.м.\nЦена за единицу: {unit_price} руб.\nКоличество: {quantity:.2f} единиц\nСтоимость: {cost:.2f} руб."

            save_report(report_content)
            success_text = "Отчет успешно сохранен."
            Text(self.app, text=success_text, color="green")
        except Exception as e:
            error_text = f"Ошибка при сохранении отчета: {e}"
            Text(self.app, text=error_text, color="red")
```
# 3.4. report.py
```
type nul > report.py
notepad report.py
```
В блокноте должен быть следующий код:
``` py
# package/report.py

import openpyxl
from datetime import datetime

def save_report(content):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Отчет"

    ws['A1'] = "Отчет о расчете материалов"
    ws['A2'] = f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    ws['A4'] = content

    wb.save("report.xlsx")
```
# 4. Создание основного файла main.py
```
cd ..
type nul > main.py
notepad main.py
```
- Вставить следующий код:
``` py
# main.py

from package.gui import MaterialApp
from guizero import App

def main():
    app = App()
    MaterialApp(app)
    app.display()

if __name__ == "__main__":
    main()
```
## 6. Установка зависимостей
Установите необходимые пакеты Python с помощью pip.Выполните следующие команды:
```
pip install guizero openpyxl
```
Если несколько версий Python:
```
python -m pip install guizero openpyxl
```
### Значения файлов проекта:
# 1. main.py
## Назначение: Это основной файл программы, который служит точкой входа для выполнения приложения.
## Функциональность:
- Импорт модулей: Импортирует класс MaterialApp из модуля gui внутри пакета package.
- Создание приложения: Создает экземпляр приложения с помощью guizero.App().
- Инициализация GUI: Создает экземпляр MaterialApp, передавая ему созданное приложение.
- Отображение интерфейса: Запускает главный цикл приложения с помощью app.display(), который отображает графический интерфейс и обрабатывает события пользователя.
# 2. package/__init__.py
## Назначение: Этот файл делает директорию package пакетом Python. Он может быть пустым или содержать инициализационный код.
## Функциональность:
- Импорт модулей: Может использоваться для импорта необходимых модулей или инициализации переменных, если это необходимо.
- Инициализация пакета: В данном случае файл оставлен пустым, так как дополнительная инициализация не требуется.
# 3. package/calculations.py
## Назначение: Этот модуль содержит логику для расчета количества и стоимости материалов.
## Функциональность:
- Класс Material: Определяет материал с его характеристиками.
## Методы:
- __init__: Инициализирует объект с именем, ценой за единицу и площадью, покрываемой одной единицей.
- calculate_quantity: Вычисляет количество единиц материала, необходимых для покрытия заданной площади.
- calculate_cost: Вычисляет общую стоимость материала на основе количества.
# 4. package/gui.py
##Назначение: Этот модуль отвечает за создание и управление графическим интерфейсом пользователя (GUI).
## Функциональность:
-Класс MaterialApp: Управляет компонентами интерфейса и логикой взаимодействия с пользователем.
## Методы:
- __init__: Инициализирует интерфейс, создает элементы управления (выпадающий список, текстовые поля, кнопки) и связывает их с соответствующими методами.
- create_material_fields: Обновляет интерфейс в зависимости от выбранного материала, отображая необходимые поля для ввода данных.
- update_material: Обрабатывает выбор материала и обновляет интерфейс.
- calculate: Выполняет расчет количества и стоимости материала на основе введенных данных.
- save_report: Сохраняет результаты расчета в файл отчета.
# 5. package/report.py
## Назначение: Этот модуль отвечает за сохранение результатов расчета в файл отчета.
## Функциональность:
- Функция save_report: Принимает содержимое отчета и сохраняет его в файл формата .xlsx или .docx в зависимости от реализации.
- Для .xlsx: Использует библиотеку openpyxl для создания и заполнения файла Excel.
- Для .docx: Использует библиотеку python-docx для создания и заполнения файла Word.
  
### Пример отчета:
- Отчет будет содержать информацию о выбранном материале, введенной площади, цене за единицу, рассчитанном количестве и стоимости.
```
Отчет о расчете материалов
Дата: 2025-03-30 15:30:45
Материал: Обои
Площадь: 50 кв.м.
Цена за единицу: 500 руб.
Количество: 10.50 единиц
Стоимость: 5250.00 руб.
```
