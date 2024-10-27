import csv
import re

filename = "example.csv"

sales = []

with open(filename, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)

    next(reader)

    for row in reader:
        print(row)

        if row[1].isdigit():
            sales.append(int(row[1]))

total_sales = sum(sales)
average_sales = total_sales / len(sales) if sales else 0

print(f"\nСумарний обьем продаж: {total_sales}")
print(f"Среднiй обьем продаж: {average_sales:.2f}")
