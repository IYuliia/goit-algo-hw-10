from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem(name="maximize_drink_production", sense=LpMaximize)

lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

model += lemonade + fruit_juice, "Total_Products"

model += (2 * lemonade + 1 * fruit_juice <= 100), "Water_Constraint"
model += (1 * lemonade <= 50), "Sugar_Constraint"
model += (1 * lemonade <= 30), "Lemon_Juice_Constraint"
model += (2 * fruit_juice <= 40), "Fruit_Puree_Constraint"

status = model.solve()

print(f"Статус розв'язання: {model.status}")
print(f"Оптимальна кількість 'Лимонаду': {lemonade.value()} одиниць")
print(f"Оптимальна кількість 'Фруктового соку': {fruit_juice.value()} одиниць")
print(f"Максимальна кількість напоїв: {model.objective.value()}")
