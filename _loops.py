students = ["sathak","harry","ommi"]

for student in students:
    print(f'sending email in students {student}')
    
fruits = {"banana","kiwi","cherry"}
for x in fruits:
    print(x)
    
for i in range(1,6):
    print(f"Attempt number {i}")
    
scores = {"harry":78,"sarthak":82}
for name, marks in scores.items():
    print(f'{name} scores {marks}')

for number in range(1,11):
    x = number * 2
    print(f'2 x {number} = {x}')
    
number = 1
while number <= 10:
    x = number * 5
    print(f'2 x {number} = {x}')
    number += 1
    
battary = 3

while battary > 0:
    print(f'Phone is on. Battery level: {battary}%')
    battary = battary - 1
    print(f'Phone is shut down. Battery percentage is {battary}%')
    
items_in_cart = ["apple", "banned_item", "banana"]

for item in items_in_cart:
    if item == "banned_item":
        print("Security alert! Banned item found. Stopping checkout.")
        break
    print(f"Processing {item}")

orders = [100, 0, 45, 0, 90]

for order in orders:
    if order == 0:
        continue
    print(f"Shipping order worth ${order}")

products = ["Laptop", "Phone", "Tablet"]

for index, item in enumerate(products, start=1):
    print(f"Item #{index}: {item}")

usernames = ["Harry", "Sarthak", "Rohit"]
scores = [78, 80, 92]

for name, mark in zip(usernames, scores):
    print(f"{name} achieved a score of {mark}")

notifications = ["Logged in", "Updated profile", "Logged out"]

for activity in reversed(notifications):
    print(f"Log event: {activity}")

students = ["Sarthak", "Rohit", "Harry"]

for student in sorted(students):
    print(f"Student: {student}")
