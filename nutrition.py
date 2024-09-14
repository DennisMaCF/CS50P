fruits_cal = {
    "apple": "130cal",
    "avocado": "50cal",
    "banana": "110cal",
    "cantaloupe": "50cal",
    "grapefruit": "60cal",
    "grapes": "90cal",
    "honeydew Melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweetcherries": "100",
    "tangerine": "50",
    "watermelon": "80",
    }
print("What kind of fruit's cal do you want to search? ")
fruit = input("Item:").lower().strip()
if fruit in fruits_cal:
    print(f"Calories: {fruits_cal[fruit]}")
else:
    print("")