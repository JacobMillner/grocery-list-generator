unit_strings = ['cup', 'cups', 'tablespoon', 'tablespoons', 'teaspoon', 'teaspoons',
        'pound', 'pounds', 'lb', 'lbs']
prep_type = ['chopped', 'diced', 'minced', 'prepared', 'grated', 
        'thinly sliced', 'sliced', 'julienned', 'thinly or julienned carrots',
        'packed']

def parse_ingredient_string(ingredient):
    # create a new dictionary to store parsed ingredient data
    parsed_ingredient = {}
    
    # setup data vars
    measurement = None
    unit = None
    prep = None
    ingredient_key = None
    
    # split the string in order to loop over each word and classify them
    # example string: "1 cup apple sauce"
    split_ingredients = ingredient.split()
    for text in split_ingredients:
        if is_measurement(text):
            # is measurement
            if measurement is None:
                measurement = text
            else:
                measurement = measurement + ' ' + text
        if text in unit_strings:
            # is unit
            unit = text
        if text in prep_type:
            # save the prep to remove later 
            prep = text
    # remove all the gathered words
    if measurement is not None:
        meas_list = measurement.split(' ')
        for mea in meas_list:
            split_ingredients.remove(mea)
    if unit is not None:
        split_ingredients.remove(unit)
    if prep is not None:
        split_ingredients.remove(prep)
    # leftover strings in array form the ingredient key
    # i.e. "apple sauce"
    ingredient_key = " ".join(split_ingredients)
    parsed_ingredient[ingredient_key] = {unit: measurement}
    return parsed_ingredient

def is_measurement(text):
    # isnumeric doesn't account for values like 2/3
    # so check for those
    if text.isnumeric():
        return True
    elif '/' in text:
        values = text.split('/')
        return len(values) == 2 and all(i.isdigit() for i in values)
    else:
        return False
