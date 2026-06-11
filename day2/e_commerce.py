tax_rate = 0
coupon = None
discount = 0
coupon_codes = ["abc", "aaa", "www"]
locations = ['Kampala', "jinja", "Mbarara"]
subtotal = 14000


products = {
    "Tv": 20000,
    "Radio": 30000,
    "Fridge":45000
}

for item in products:
    print(f"{item} : {products[item]}")


while True:
    product = input("Type Product name : ")
    product = product.title()
    if product in products:
        subtotal = products[product]
        break
    else:
        print("invalid Selection, Try Again")



while True:
    coupon = input("Enter coupon code if any else press 1 to skip : ")
    if coupon:
        if coupon in coupon_codes:
            discount = 10
            print(f"Coupon discount applied : {discount}%")
        elif coupon == "1":
            break
        else:
            print("Invalid coupon")
    else:
        print("No coupon entered")
    break
else:
    print("No coupon entered")
print("")


print("Available locations")
for city in locations:
    x = locations.index(city) +1
    print(f"{x}.{city}")
print("")



y = True
while y:
    choice = input("Select in your location : ")
    match choice:
        case "1":
            tax_rate = 10
            y = False
        case "2":
            tax_rate = 12
            y = False
        case "3":
            tax_rate= 15
            y = False

        case _:
            print("invalid input")

match subtotal:
    case n if (10000 <=n <= 20000):
        discount += 10
    case n if (20001 <=n < 30000):
        discount += 15
    case n if (30001 <=n < 45000):
        discount += 20
    case _:
        print("")

discountAmount = subtotal * (discount/100)
taxAmount = subtotal * (tax_rate/100)
finalPrice = subtotal + taxAmount - discountAmount

print(".........summary...........")
print(f"product : {product}")
if coupon and coupon in coupon_codes:
    print(f"coupon code : {coupon}")
print(f"subtotal : {subtotal}")
print(f"discount : {discount}%")
print(f"tax rate : {tax_rate}%")
print(f"final price is : {finalPrice}")
print(".............Thank you.............")