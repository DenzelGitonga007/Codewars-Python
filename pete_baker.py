"""
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

"""


def cakes(recipe, available):
    # List to store how many cakes can be made from each ingredient...
    max_cakes_per_ingredient = []
    
    # Loop through each ingredient in the recipe
    for ingredient in recipe:
        # If ingredient is missing, return 0 immediately
        if ingredient not in available:
            return 0
        
        # Calculate how many cakes can be made with this ingredient
        max_cakes = available[ingredient] // recipe[ingredient]
        
        # Store this value
        max_cakes_per_ingredient.append(max_cakes)
    
    # Return the minimum value from the list (smallest limiting factor)
    return min(max_cakes_per_ingredient)

# Test cases
print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))  # Output: 2
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))  # Output: 0
