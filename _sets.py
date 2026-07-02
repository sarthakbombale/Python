numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print(unique_numbers)

fruits = {"apple", "banana"}
fruits.add("cherry")
fruits.remove("banana")
print(fruits)

cricket_players = {"Harry", "Sarthak", "Rohit"}
football_players = {"Rohit", "Rahul", "Amit"}

both_sports = cricket_players.intersection(football_players)
print(both_sports)

all_players = cricket_players.union(football_players)
print(all_players)

only_cricket = cricket_players.difference(football_players)
print(only_cricket)

names = {"Harry", "Sarthak"}
names.discard("Rohit")
print(names)

active_users = {"Harry", "Sarthak", "Rohit"}
active_users.clear()
print(active_users)

required_skills = {"Python", "Git"}
my_skills = {"Python", "Git", "SQL", "Java"}
is_qualified = required_skills.issubset(my_skills)wrong_set = {}
print(type(wrong_set))

correct_set = set()
print(type(correct_set))

print(is_qualified)

veg_food = {"Apple", "Banana", "Carrot"}
non_veg_food = {"Chicken", "Fish"}
print(veg_food.isdisjoint(non_veg_food))

wrong_set = {}
print(type(wrong_set))

correct_set = set()
print(type(correct_set))
