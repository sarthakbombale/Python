scores = {
    'harry': 78,
    'sarthak': 80,
    'rohit': 92
}

print(scores)
print(scores.get('rohit','Not Found'))
print(scores.get('rahul', 'Not Found'))
print(scores.get('harry', 'Not Found')) 
scores.update({'sarthak':98,'priya':100})
print(scores)

all_students = scores.keys()
print(all_students)

all_marks = scores.values()
print(all_marks)

for names,marks in scores.items():
 print(f"{names} scored {marks}")
 
remove_score = scores.pop('rohit')
print(scores)

marks = {"harry": 78, "sarthak": 80}


if "rohit" in marks:
    print(marks["rohit"])
else:
    print("Rohit does not exist in the record!")

if "harry" in marks:
    print(f"harry scores {marks['harry']}")
else:
    print("harry does not exist in the record!")
