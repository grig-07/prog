from modules.material_data import material_data

def calculate_cost(material, area):
    if material not in material_data:
        return "Материал не найден"

    price_per_unit = material_data[material]["цена"]
    unit = material_data[material]["ед. изм."]

    if unit == "м2":
        quantity = area
    elif unit == "рулон":
        roll_width = 1.06  # Стандартная ширина рулона обоев
        quantity = (area // roll_width**2) + 1  # Кол-во рулонов
    else:
        return "Неподдерживаемая единица измерения"

    cost = quantity * price_per_unit
    return {"quantity": quantity, "cost": cost, "unit": unit}