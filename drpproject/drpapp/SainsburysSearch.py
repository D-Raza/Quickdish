import requests
import json

def constructSainsburysGetRequest(item):
    params = {
        "page_number" : "1",
        "page_size" : "1",
        "filter[keyword]" : item,
        "sort_order" : "FAVOURITES_FIRST"
    }
    url = "https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?"
    paramString = [(param + "=" + val) for (param, val) in params.items()]
    delim = "&"
    url += delim.join(paramString)
    return url

def searchSainsburys(item):
    request = constructSainsburysGetRequest(item)
    print("GET request URL:\n" + request)
    response = requests.get(request)
    
    if response.status_code == 200:
        parsed = response.json()
        formatted = json.dumps(parsed, indent=2)
        print("\n==========START OF RESPONSE==========\n")
        print(formatted)
        print("==========END OF RESPONSE==========\n")
    first = response.json().get('products')[0]
    return first
# Sample GET request for "egg" search
# https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[keyword]=egg&page_number=1&page_size=5&sort_order=FAVOURITES_FIRST