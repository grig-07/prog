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
