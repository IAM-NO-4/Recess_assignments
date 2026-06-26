class Restaurant:
    def __init__(self,rest_name, cuisine_name):
        self.rest_name = rest_name
        self.cuisine_name = cuisine_name
    
    def describe_restaurant(self):
        print(
            f"""
            The restaurant name is: {self.rest_name} 
            the cuistine name is: {self.cuisine_name}
            """
        )
    def open_restaurant(self):
        print(f"{self.rest_name} is open" )
    
restaurant = Restaurant("Hot fresh", "Cuistin")
print(f"The name is {restaurant.rest_name}")
print(f"The cuistin is {restaurant.cuisine_name}")
restaurant.describe_restaurant()
restaurant.open_restaurant()
           