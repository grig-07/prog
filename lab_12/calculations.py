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
