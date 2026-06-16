names = ["iam", "kabejja", "ernest","ibrahim","Amir"]
print("Original list", names)
print("The second item: ",names[1])
names[0] = "Taatawo"
names.append("Kato")
print("After adding: ", names)
names.insert(2,"Bathel")
print("After inserting Bathel: ",names)
names.pop(3)
print("After removing the forth element: ", names)
print("The last element: ", names[-1])
new_list = [1,2,3,4,5,6,7]
print("2nd,3rd and 4th items: ",new_list[2:5])

countries = ["Uganda", "Kenya", "USA"]
country_copy = countries.copy()
print("Countries: ",country_copy)

for country in countries:
    print(country)

animals = ["goat", "cow", "sheep", "dog"]
asce_sorted_animals = sorted(animals)
desc_sorted_animals = sorted(animals, reverse=True)

print("Animals sorted in asc: ",asce_sorted_animals)
print("Animals sorted in desc: ",desc_sorted_animals)

print("Animals with letter 'a': ")
for animal in animals:
    if "a" in animal:
        print(animal)
first_names = ["Kato", "iam"]
second_names = ["Abu","no_4"]

all_names = first_names + second_names
print(all_names)