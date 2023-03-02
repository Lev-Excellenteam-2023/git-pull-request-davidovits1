# David Ovits
# exercise 5.2 slice of cake


def get_recipe_price(prices, optionals=[], **ingredients):
    """
    Receives prices of ingredients for a cake per 100 grams and the quantity consumed per cake of each ingredient
     and returns the price
    :param prices: dict prices ingredients
    :param optionals: ingredients to ignore (optionals)
    :param ingredients: Quantity consumed of each product
    :return: price of a cake
    """
    price_cake = 0.0
    for i in prices:
        if i not in optionals:
            price_product = prices[i]
            price_cake += ingredients[i] / 100 * price_product
    if price_cake.is_integer():
        price_cake = int(price_cake)

    print(price_cake)


get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=37, milk=100)
get_recipe_price({})
