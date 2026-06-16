beverages = set(("cocacola","pepsi","fanta"))
print("The original set is: ",beverages)
beverages.update(("Novida","Lavita"))
print("After updating: ",beverages)

my_set = {"oven","kettle","microwave","refrigerator"}
print("Original second set: ",my_set)
if "microwave" in my_set:
    print("microwave present")
else:
    print("Microwave not present")

my_set.remove("kettle")
print("After removing kettle: ",my_set)
print('Items in my new set: ')
for item in my_set:
    print(item)


set1 = {1,2,3,4}
list1 = [5,6,7,8]
set1.update(list1)
print("Updated set: ",set1)

names = {"iam", "kabejja"}
ages = {12,43}

names_and_ages = names.union(ages)
print(names_and_ages)