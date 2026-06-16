x = ("samsung", "iphone", "tecno", "redmi")
print("Original list: ",x)
print("my favorite phone is: ",x[0])
print("the second last item is: ",x[-2])

x = list(x)
x[1] = "itel"
print("after updating: ",x) 
x.append("Huawei")
x = tuple(x)
print("Phones available: ")
for phone in x:
    print(phone)
x = list(x)
x.pop(0)
print("After removing the 1st item: ", x)
x =tuple(x)

cities = tuple(("Jinja","Kampala","Masaka", "mukono"))
print("Cities: ",cities)

city1, city2,city3,city4 = cities
print("City1: ",city1)
print("City2: ",city2)


print("The 2nd, 3rd and 4th items are: ",cities[1:4])
tp1 = ("Amir","Kabejja")
tp2 = ("Iam", "No_4")

compbined_tp = tp1 + tp2
print("The combined tuple is: ",compbined_tp)

colors = ("Blue", "Red", "White")
colors2 = colors * 3
print(colors2)

this_tuple = (1,3,7,8,7,5,4,6,8,5)
print("Eight appears: ", this_tuple.count(8)," times")

