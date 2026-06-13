numbers = [5, 2, 9, 1, 5, 6]
persons = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

sorted_numbers = sorted(numbers, reverse=True, key=lambda x: x)
print("Sorted numbers:", sorted_numbers)

print(persons[0]["name"])
sorted_persons = sorted(persons, key=lambda x: x["age"])
print("Sorted persons by age:")
for person in sorted_persons:
    print(f"  {person['name']}: {person['age']}")