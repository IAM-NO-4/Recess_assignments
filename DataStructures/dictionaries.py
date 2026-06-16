shoes = {
    "brand" : "nick",
    "color" : "black",
    "size" : 30
}
print("Before changing: ",shoes)
shoes["brand"] = "adidas"
print("After chaning:",shoes)
shoes["type"] = "sneakers"
print("After adding: ",shoes)


keys = shoes.keys()
print(keys)
values = shoes.values()
print(values)

if "size" in shoes.keys()
    print("the key exists")
else:
    print("The key is missing")