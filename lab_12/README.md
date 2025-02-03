Разработка пакета для расчёта количества и стоимости отделочных материалов
В данном примере мы разработаем пакет finishing_materials, содержащий три модуля:
 * calculator.py: модуль, содержащий функции для расчёта количества и стоимости отделочных материалов.
 * gui.py: модуль, содержащий функции для создания графического интерфейса пользователя на основе guizero.
 * report_generator.py: модуль, содержащий функции для сохранения результатов в отчёт.
1. Модуль calculator.py
# calculator.py
``` py
def calculate_material_quantity(area, material_type):
    """
    Функция для расчёта количества материала в зависимости от площади и типа.
    """
    if material_type == "Обои":
        # Пример: считаем, что ширина рулона обоев 0.5 м, длина 10 м
        roll_area = 0.5 * 10
        rolls = (area + roll_area - 1) // roll_area  # Округляем в большую сторону
        return rolls
    elif material_type == "Плитка":
        # Пример: считаем, что размер плитки 0.3 м * 0.3 м
        tile_area = 0.3 * 0.3
        tiles = (area + tile_area - 1) // tile_area
        return tiles
    elif material_type == "Ламинат":
        # Пример: считаем, что одна упаковка ламината покрывает 2 кв.м.
        package_area = 2
        packages = (area + package_area - 1) // package_area
        return packages
    else:
        return 0

def calculate_material_cost(quantity, material_type):
    """
    Функция для расчёта стоимости материала в зависимости от количества и типа.
    Цены условные, необходимо заменить на актуальные.
    """
    if material_type == "Обои":
        price_per_roll = 500  # руб. за рулон
        return quantity * price_per_roll
    elif material_type == "Плитка":
        price_per_tile = 50  # руб. за плитку
        return quantity * price_per_tile
    elif material_type == "Ламинат":
        price_per_package = 1000  # руб. за упаковку
        return quantity * price_per_package
    else:
        return 0
```
2. Модуль gui.py
# gui.py

from guizero import App, Text, TextBox, Combo, PushButton, error
from .calculator import calculate_material_quantity, calculate_material_cost
from .report_generator import save_to_docx, save_to_excel

def create_gui():
    app = App(title="Расчёт отделочных материалов")
    ``` py
    area_text = Text(app, text="Площадь помещения (кв.м):")
    area_input = TextBox(app)

    material_text = Text(app, text="Тип материала:")
    material_combo = Combo(app, options=["Обои", "Плитка", "Ламинат"])

    def calculate_and_display():
        try:
            area = float(area_input.value)
            material_type = material_combo.value

            if area <= 0:
                raise ValueError("Площадь должна быть больше нуля.")

            quantity = calculate_material_quantity(area, material_type)
            cost = calculate_material_cost(quantity, material_type)

            result_text.value = f"Необходимо: {quantity} {get_unit(material_type)}, Стоимость: {cost} руб."

        except ValueError as e:
            error(title="Ошибка", text=str(e))
        except Exception as e:
            error(title="Ошибка", text="Произошла ошибка при расчёте.")

    def get_unit(material_type):
        if material_type == "Обои":
            return "рулонов"
        elif material_type == "Плитка":
            return "плиток"
        elif material_type == "Ламинат":
            return "упаковок"
        else:
            return ""

    calculate_button = PushButton(app, text="Рассчитать", command=calculate_and_display)

    result_text = Text(app, text="Результат:")

    def save_report(format):
        try:
            area = area_input.value
            material_type = material_combo.value
            result = result_text.value

            if format == "docx":
                save_to_docx(area, material_type, result)
            elif format == "xlsx":
                save_to_excel(area, material_type, result)

            # Optionally, provide feedback to the user
            # app.info("Отчёт сохранён")

        except Exception as e:
            error(title="Ошибка", text=f"Ошибка сохранения: {e}")

    save_docx_button =
PushButton(app, text="Сохранить в .docx", command=lambda: save_report("docx"))
    save_excel_button = PushButton(app, text="Сохранить в .xlsx", command=lambda: save_report("xlsx"))

    app.display()
```
#3. Модуль report_generator.py (остаётся без изменений, как в предыдущем примере)
#4. Основная программа (main.py)
# main.py
``` py
from finishing_materials.gui import create_gui

if __name__ == "__main__":
    create_gui()
```
Инструкция по запуску
 * Создайте папку с именем finishing_materials.
 * Поместите в неё файлы calculator.py, gui.py и report_generator.py.
 * Создайте файл main.py в той же папке, где находится папка finishing_materials.
 * Установите необходимые библиотеки: pip install guizero python-docx openpyxl.
 * Запустите файл main.py.
В результате будет создан графический интерфейс, позволяющий вводить площадь помещения, выбирать тип материала, рассчитывать необходимое количество и стоимость, а также сохранять результаты в отчёт.
Важные замечания:
 * Цены на материалы в модуле calculator.py являются условными. Необходимо заменить их на актуальные.
 * Размеры рулонов обоев, плитки и упаковок ламината также являются примерными. Уточните их перед использованием.
 * Код использует простые алгоритмы расчёта. В реальном проекте может потребоваться более сложная логика, учитывающая особенности помещения и материалов.
 * Для корректной работы с кириллицей в docx и xlsx файлах, убедитесь, что ваша система поддерживает русский язык.
