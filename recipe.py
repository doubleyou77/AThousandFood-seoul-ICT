import requests
from bs4 import BeautifulSoup

Url = "https://www.10000recipe.com/recipe/list.html?q="

def Crawling(recipeUrl):
    url = Url+recipeUrl

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    recipe = []
    try:
        ul = soup.select_one('ul.rcp_m_list2')
        title = ul.select_one('div.common_sp_caption_tit').getText()
        recipeLocation = ul.select_one('div.common_sp_thumb a')['href']

        recipe.append(title)
        recipe.append(recipeLocation)
    except (AttributeError):
        return
    
    return recipe
