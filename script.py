# Author: Vernell Mangum
#
# Description: Simple Python program that organizes data using different functions and methods for lists.
#
# You work at Len’s Slice, a new pizza joint in the neighborhood. 
# You are going to use your knowledge of Python lists to organize some of your sales data.

# Toppings for pizzas we sell
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# Prices based on topping
prices = [2, 6, 1, 3, 2, 7, 2]

# Counting the number of occurrences of 2 in the prices list
num_two_dollar_slices = prices.count(2)

# Number of different toppings we have
num_pizzas = len(toppings)

# Printing the number of different pizzas we have
print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

# Combining toppings and prices into 2D list
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

# Testing to see if new list is correct
# print(pizza_and_prices)

