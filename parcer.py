import requests
import pandas
from bs4 import BeautifulSoup

products = []

def create(link):    
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')    
    return soup

#Все ценны
for web_number in range(1,229):
    soup =create(f"https://grafkolcov.ru/jewelry/kolca/?PAGEN_1={web_number}")    
    cards = soup.find_all(class_="catalog-content__item")
    
    
    


for card in cards:
         # product = {}
        current_price=card.find(class_="catalog-current__price").text
        # product["price"] = current_price.strip() 
    
#Картинка    
        
        # img = "https://grafkolcov.ru" + soup.find(class_="catalog-slider__img").select("img")[0]["src"]    
          
#Ссылки
        # product["link"] = cards[0].find(class_="catalog-content__more").find("a")["href"].strip()
        detail = create("https://grafkolcov.ru" + cards[0].find(class_="catalog-content__more").find("a")["href"])
        
        
        
#Размеры  
        # product["sizes"] = []
        for size in detail.find(class_="product-size__block").select(".product-size__item:not(.product-size_disabled)"):
            # product["sizes"].append(size.text)
            products.append(eval(size["data-json"]))
        
df = pandas.DataFrame(products)
df.to_excel("graf.xlsx",index=False)
print(df)