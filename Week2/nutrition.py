fruits_cal = {
    "apple": "130cal",
    "avocado": "50cal",
    "banana": "110cal",
    "cantaloupe": "50cal"
}
print("What kind of fruit's cal do you want to search? ")
fruit = input("Item:")
if fruit in fruits_cal:
    print(f"Calories:{fruits_cal[fruit]}")
else:
    print("Fruit not found in the database.")