import requests
import sys
from bs4 import BeautifulSoup


def scrap_genre():
    """
    Scraping method
    """
    request = requests.get('https://myanimelist.net/anime.php')
    content = request.content
    soup = BeautifulSoup(content,"html.parser")
    a = soup.find_all("a", {"class": "genre-name-link"})
    list_words = [elt.string.strip() for elt in a]
    # with open('anime_decide/genres.txt', 'w') as f:
    #     for i in range(len(list_words)):
    #         f.write(list_words[i]+"\n")

def scrap():
    """
    Scraping method
    """
    for i in range(0,21000,50):
        request = requests.get('https://myanimelist.net/topanime.php?limit='+str(i))
        content = request.content
        soup = BeautifulSoup(content,"html.parser")
        a = soup.find_all("h3", {"class": "hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3"})
        list_words = [elt.string.strip() for elt in a]
        with open('anime_decide/anime.txt', 'a', encoding='utf-8-sig') as f:
            for i in range(len(list_words)):
                f.write(list_words[i]+"\n")
    
scrap()
