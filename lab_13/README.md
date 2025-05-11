# Лабораторная работа №13
Перепишите свой вариант лабораторной работы №12 с использованием классов и объектов.
Задание то же, вариант GUI фреймворка возьмите следующий по списку.
В коде должны присутствовать:
- абстрактный базовый класс и соотвествующие декораторы для методов
- иерархия наследования
- managed - атрибуты
- минимум 2 dunder-метода у подклассов
## Ход работы:
перепишем  код, чтобы он соответствовал следующим критериям:
1. Абстрактный базовый класс с использованием модуля abc и соответствующих декораторов для методов.
2. Иерархия наследования, где подклассы наследуются от абстрактного базового класса.
3. Managed-атрибуты с использованием свойств (@property).
4. Минимум 2 dunder-метода у подклассов (например, __str__ и __repr__).
5. GUI с использованием guizero, который будет взаимодействовать с этими классами.
### Абстрактный базовый класс и иерархия наследования:
``` py
from abc import ABC, abstractmethod
import guizero
from guizero import App, Text, TextBox, Combo, PushButton, Text
import openpyxl
from datetime import datetime

class Material(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_quantity(self, area):
        pass

    @abstractmethod
    def calculate_cost(self, quantity):
        pass

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        if value >= 0:
            self._unit_price = value
        else:
            raise ValueError("Unit price must be non-negative")

    @property
    def area_per_unit(self):
        return self._area_per_unit

    @area_per_unit.setter
    def area_per_unit(self, value):
        if value > 0:
            self._area_per_unit = value
        else:
            raise ValueError("Area per unit must be positive")

    def __str__(self):
        return f"{self.name}Material(unit_price={self.unit_price}, area_per_unit={self.area_per_unit})"

    def __repr__(self):
        return self.__str__()

class Wallpaper(Material):
    def calculate_quantity(self, area):
        return (area / self.area_per_unit) + 0.5  # округляем вверх

    def calculate_cost(self, quantity):
        return quantity * self.unit_price

class Tile(Material):
    def calculate_quantity(self, area):
        return (area / self.area_per_unit) + 0.5  # округляем вверх

    def calculate_cost(self, quantity):
        return quantity * self.unit_price

class Laminate(Material):
    def calculate_quantity(self, area):
        return (area / self.area_per_unit) + 0.5  # округляем вверх

    def calculate_cost(self, quantity):
        return quantity * self.unit_price
```
### GUI с использованием guizetta
``` py
import guizetta
from guizetta import App, Text, TextBox, Combo, PushButton, Text

class MaterialApp:
    def __init__(self, app):
        self.app = app
        self.app.title("Расчет материалов")
        self.app.width = 400
        self.app.height = 400

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
        if choice == "Обои":
            self.selected_material = Wallpaper(name="Обои")
        elif choice == "Плитка":
            self.selected_material = Tile(name="Плитка")
        elif choice == "Ламинат":
            self.selected_material = Laminate(name="Ламинат")
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

            report_content = (
                f"Материал: {self.selected_material.name}\n"
                f"Площадь: {area} кв.м.\n"
                f"Цена за единицу: {unit_price} руб.\n"
                f"Количество: {quantity:.2f} единиц\n"
                f"Стоимость: {cost:.2f} руб."
            )

            self.save_to_excel(report_content)
            success_text = "Отчет успешно сохранен."
            Text(self.app, text=success_text, color="green")
        except Exception as e:
            error_text = f"Ошибка при сохранении отчета: {e}"
            Text(self.app, text=error_text, color="red")

    def save_to_excel(self, content):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Отчет"

        ws['A1'] = "Отчет о расчете материалов"
        ws['A2'] = f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        ws['A4'] = content

        wb.save("report.xlsx")

def main():
    app = App()
    MaterialApp(app)
    app.display()

if __name__ == "__main__":
    main()
```
### Основной файл main.py
``` py
from package.gui import MaterialApp
import guizetta

def main():
    app = guizetta.App(title="Расчет материалов", width=400, height=400)
    MaterialApp(app)
    app.display()

if __name__ == "__main__":
    main()
```

