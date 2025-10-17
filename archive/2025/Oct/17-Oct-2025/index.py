# Create calculating formula to go over a list of groceries, and calculate how much we spent on groceries
# based on a cetogenetic diet average intakes.

import json

Dayli_Intake_Per_Person = [
     {
        "name": "Eggs",
        "intake": 5,
        "qty": "pcs",
        "price": 0.14,
        "supermarket": "Tesco"
    },
    {
        "name": "Avocado",
        "intake": 1,
        "qty": "pcs",
        "price": 1,
        "supermarket": "Aldi"
    },
    {
        "name": "Water",
        "intake": 2,
        "qty": "1.5L Bottle",
        "price": 3.75/6,
        "supermarket": "Tesco"
    },
    {
        "name": "Dark Chocolate",
        "intake": 10,
        "qty": "gr.",
        "price": 3/90,
        "supermarket": "Name"
    },
    {
        "name": "Feta",
        "intake": 100,
        "qty": "gr.",
        "price": 4.25/1000,
        "supermarket": "Tesco"
    },
    {
        "name": "Meet",
        "intake": 400,
        "qty": "gr.",
        "price": 10/1000,
        "supermarket": "Butcher"
    },
    {
        "name": "Nuts",
        "intake": 50,
        "qty": "gr.",
        "price": 10/1000,
        "supermarket": "Aldi"
    },
    {
        "name": "Milk subtitute",
        "intake": 1,
        "qty": "gr.",
        "price": 1.20,
        "supermarket": "Aldi"
    },
    {
        "name": "Butter",
        "intake": 25,
        "qty": "gr.",
        "price": 12.35/1000,
        "supermarket": "Asda"
    },
    {
        "name": "Olive Oil",
        "intake": 25,
        "qty": "gr.",
        "price": 12.50/1000,
        "supermarket": "Asda"
    },
    {
        "name": "Ocasional",
        "intake": 1,
        "qty": "gr.",
        "price": 2,
        "supermarket": "Asda"
    },
]

def calculate_monthly_cost(dict, people, days):
    a = []
    for key in dict:
        a.append(key["intake"] * key["price"])
    
    return(sum(a)*people * days)

def main():
    print(calculate_monthly_cost(Dayli_Intake_Per_Person, 1, 30))

if __name__ == "__manin__":
    main()