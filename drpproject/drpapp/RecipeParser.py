from recipe_scrapers import scrape_me
from urllib.parse import urlparse
import requests

def get_recipe_details(search_input):
    if is_url(search_input):
        scraper = scrape_me(search_input)
        return scraper.ingredients(), scraper.title(), scraper.image(), scraper.instructions_list()
    else:
        spoonacular_api_key = "80e9ed44acfc47cb94004a918658e768"
        url = f'https://api.spoonacular.com/recipes/complexSearch?query={search_input}&apiKey={spoonacular_api_key}&number=1'
        response = requests.get(url)
        data = response.json()
        if data['totalResults'] > 0:
            recipe = data['results'][0]
            recipe_id = recipe['id']
            # Get recipe details
            url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={spoonacular_api_key}'
            response = requests.get(url)
            data = response.json()

            ingredients = [ingredient['original'] for ingredient in data['extendedIngredients']]
            title = data['title']
            image = data['image']
            instructions = [step['step'] for step in data['analyzedInstructions'][0]['steps']]

            return ingredients, title, image, instructions
        else:
            return None, None, None, None # or None?
        

# is_url("http://www.google.com") =  True
# is_url("not a url") = False
# is_url("www.google.com") = False (should this be intended behaviour?)
def is_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
    