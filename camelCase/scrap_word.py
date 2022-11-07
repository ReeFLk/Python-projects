import requests
from bs4 import BeautifulSoup


def scrap():
    """
    Scraping method
    """
    request=requests.get('https://www.listesdemots.net/touslesmots.htm')
    content=request.content
    soup = BeautifulSoup(content,features="lxml")
    p = soup.find_all("span", {"class": "mot"})
    list_words = [elt.string.strip() for elt in p]
    with open('motlettres.txt', 'a') as f :
        f.write(list_words[0])
    
    for i in range(2,918) :
        request=requests.get('https://www.listesdemots.net/touslesmotspage'+str(i)+'.htm')
        content=request.content
        soup = BeautifulSoup(content,features="lxml")
        p = soup.find_all("span", {"class": "mot"})
        list_words = [elt.string.strip() for elt in p]
        with open('motlettres.txt', 'a') as f :
            f.write(list_words[0])
        
scrap()