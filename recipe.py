import requests
from bs4 import BeautifulSoup

Url = "https://www.10000recipe.com/recipe/list.html?q="

def Crawling(recipeUrl):
    url = Url+recipeUrl

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    recipe_title = []

    try:
        ul = soup.select_one('ul.rcp_m_list2')
        titles = ul.select('div.common_sp_caption_tit')

        for title in titles:
            recipe_title.append(title.get_text())
    except (AttributeError):
        return
    
    return recipe_title
