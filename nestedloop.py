food = [
    ["fried rice", 15000],
    ["egg fried rice", 20000],
    ["egg fried rice special", 30000]
]
drink = [
    ["sprite", 15000],
    ["monster", 25000],
    ["hot/cold tea", 12000]
]
print("="*40)
print("pilihan makanan dan tota harga")
print("="*40)

for foods_item in food:
    food_name = foods_item[0]
    food_price = foods_item[1]
    for drink_item in drink:
        drink_names = drink_item[0]
        drink_price = drink_item[1]
    
        total_price = food_price + drink_price
        print(f"food : {food_name}")
        print(f"drink : {drink_names}")
        print(f"total_price : Rp{total_price:,}")
        print("-" * 30)