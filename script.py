toppings = ['pepperoni', 'pinapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
print("We sell "+str(num_pizzas)+" kinds of pizza!")
pizzas = list(zip(prices, toppings))
print(pizzas)
pizzas.sort()
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
print("Our three cheapest pizzas are "+str(three_cheapest))
num_two_dollar_slices = prices.count(2)
