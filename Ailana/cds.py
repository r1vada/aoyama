import json

with open('products.json', 'r') as file:
    products = json.load(file)

# 3.2.1 Фильтрация print ("Товары в наличии:")
for product in products:
    if product["in_stock"] == True:
        print(product["name"])
# 3.2.2 Агрегация
total_price = 0
for product in products:
    if product["in_stock"] == True:
        total_price += product["price"]
print("Общая стоимость товаров в наличии:", total_price)
most_expensive = products[0]
for product in products:
    if product["price"] > most_expensive["price"]:
        most_expensive = product

print ( "Самый дорогой товар:", most_expensive["name"]) 
# 3.2.3 Работа с категориями
electronics = []
for product in products:
    if product["category"] == "electronics":
        electronics.append(product["name"])
print ("Товары категории electronics:")
for name in electronics:
    print(name)

# 3.2.4 Добавление данных
new_product = {
    "id": 6,
    "name": "Планшет",
    "price": 180000,
    "category": "electronics",
    "in_stock": True
}
products.append(new_product)

# 3.3 Изменение данных
for product in products:
    if product["id"] == 2:
        product["in_stock"] = False
        product["price"] = int(product["price"] * 0.9)  

with open('updated_products.json', 'w', encoding='utf-8') as file:
    json.dump(products, file, ensure_ascii=False, indent=2)