# The add_prices function returns the total price of all of the groceries in the  dictionary. 
# Fill in the blanks to complete this function.

def add_prices(groceries):
	groceries = groceries.values()
	groceries = sum(groceries)
	return round(groceries, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44


