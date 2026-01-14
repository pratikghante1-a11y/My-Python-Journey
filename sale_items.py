items = [
    {"name": "Milk", "price": 50},
    {"name": "Chocolate", "price": 10},
    {"name": "Bread", "price": 40},
    {"name": "Candy", "price": 5}
]

sale_items = []
for i in items:
    if i["price"] > 20:
        sale_items.append(i["name"])
        
    print("Sale hue item:", sale_items)
