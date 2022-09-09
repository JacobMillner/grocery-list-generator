import pprint
from recipe_scrapers import scrape_me
from util import parse_ingredient_string

pp = pprint.PrettyPrinter(indent=2)

recipes = ['https://www.allrecipes.com/recipe/274894/chicken-bryan-with-chicken-leg-quarters/',
        'https://www.allrecipes.com/recipe/8462068/sheet-pan-buttermilk-pancakes/',
        'https://www.allrecipes.com/recipe/275055/grilled-teriyaki-shrimp-and-pineapple-skewers/',
        'https://www.melskitchencafe.com/thai-chicken-crunch-wraps/',
        'https://www.maangchi.com/recipe/bibimbap']

for recipe in recipes:
    try:
        scraper = scrape_me(recipe)
        ingred = scraper.ingredients()
        for ingred_str in ingred:
            parsed_ingred = parse_ingredient_string(ingred_str)
            pp.pprint(parsed_ingred)
    except Exception as e:
        print('Scraping error ' + str(e))
        print('trying wild mode for: ', recipe)
        try:
            scraper = scrape_me(recipe, wild_mode=True)
            ingred = scraper.ingredients()
            if ingred:
                for ingred_str in ingred:
                    parsed_ingred = parse_ingredient_string(ingred_str)
                    pp.pprint(parsed_ingred)
            else:
                print('Nothing found for: ', recipe)
        except:
            print('Nothing found for: ', recipe)

