import pprint
from recipe_scrapers import scrape_me

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
        pp.pprint(ingred)
    except:
        print('Recipe site not supported, trying wild mode for: ', recipe)
        try:
            scraper = scrape_me(recipe, wild_mode=True)
            ingred = scraper.ingredients()
            if ingred:
                pp.pprint(ingred)
            else:
                print('Nothing found for: ', recipe)
        except:
            print('Nothing found for: ', recipe)

