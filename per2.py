import json

filename = "metals.json"

with open(filename, 'r') as file:
    metal_prices = json.load(file)

metal = input("Введіть назву металу (наприклад, gold, silver, platinum): ").strip().lower()
mass = float(input("Введіть масу виробу в грамах: "))

if metal in metal_prices:
    price_per_gram = metal_prices[metal]
    total_cost = price_per_gram * mass
    print(f"Вартість виробу з {metal}: {total_cost:.2f}")
else:
    print(f"Метал '{metal}' не знайдений у даних.")
