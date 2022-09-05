unit_strings = ['cup', 'tablespoon', 'teaspoon']
prep_type = ['chopped', 'diced']

def parse_ingredient_string(ingredient):
    # create a new dictionary to store parsed ingredient data
    parsed_ingredient = {}
    
    # setup data vars
    measurement = None
    unit = None
    ingredient_key = None
    
    # split the string in order to loop over each word and classify them
    # example string: "1 cup apple sauce"
    split_ingredients = ingredient.split()
    for text in split_ingredients:
        if text.isnumeric():
            # is measurement
            measurement = text
            split_ingredients.pop(0)
            pass
        if text in unit_strings:
            # is unit
            unit = text
            split_ingredients.pop(0)
            pass
        if text in prep_type:
            # ignore and remove prep type
            split_ingredients.pop(0)
            pass
    # leftover strings in array form the ingredient key
    # i.e. "apple sauce"
    ingredient_key = " ".join(split_ingredients)
    parsed_ingredient[ingredient_key] = {unit: measurement}
    return parsed_ingredient

