from bs4 import BeautifulSoup as bs
import requests
import json

my_stocks= ['CAMP','CRNT','FCEL','FLT','GBML.V','HIVE.V','IDEX','IGT','OEG','PLUG','RESN','SCOR','SUNW','TRIL','TS']

def getStock(symb):
    r = requests.get(f"https://ca.finance.yahoo.com/quote/{symb}?p={symb}")
    soup = bs(r.content, 'html.parser')
    try:
        stock = soup.find('div', {'class': 'D(ib) Mend(20px)'})
        stock_value = {
                'company':soup.find('h1', {'class' : 'D(ib) Fz(18px)'}).get_text(),
                'price': stock.find_all('span')[0].get_text(),
                'change_value': stock.find_all('span')[1].get_text()
            }
        return stock_value
    except Exception:
        print("check the symbol")

for symb in my_stocks:
    print(getStock(symb))


#for symb in my_stocks:
   # with open('mystocks.json','a') as file:
        #json.dump(getStock(symb),file)




