from bs4 import BeautifulSoup as bs
import requests
import re

r = requests.get("https://en.wikipedia.org/wiki/Maharshi_(2019_film)")

soup = bs(r.content,'html.parser')

info_box = soup.find(class_ ='infobox vevent')


info_rows = info_box.find_all('tr')




def get_content_value(row_data):
    if row_data.find("li"):
        return [li.get_text().replace("\xa0"," ") for li in row_data.find_all("li")]
    else:
        return row_data.get_text().replace("\xa0"," ")

movie_info = {}
for index,row in enumerate(info_rows):
    if index == 0:
        movie_info['title'] = row.find("th").get_text()
    elif index == 1:
        continue
    else:
        content_key = row.find("th").get_text(" ", strip = True)
        content_value = get_content_value(row.find("td"))
        movie_info[content_key] = content_value

def synopsis(soup):
    content = soup.find(class_ = 'mw-parser-output').find_all('p')
    return [p.get_text() for p in content]

def cast(soup):
    cast  = []
    content = soup.find(class_ = 'div-col').find_all('li')
    for li in content:
        try:
           cast.append(li.a.attrs['title'])
        except Exception:
            cast.append(li.get_text())


    return cast






print(cast(soup))

print('--'*30)
print(movie_info)
print('--'*30)
print(synopsis(soup))