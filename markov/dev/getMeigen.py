import requests
from bs4 import BeautifulSoup
from time import sleep

def getMeigen(page: int):
  res = requests.get(f'http://www.meigensyu.com/quotations/index/page{page}.html')

  soup = BeautifulSoup(res.text, 'html.parser')

  quote_elms = soup.find_all('div', {'class': 'text'})

  quotes = []
  for quote_elm in quote_elms:
    quote = quote_elm.text
    if quote.replace(' ', '').replace("'", "").replace(".", "").replace(",", "").isalpha():
      continue
    quotes.append(quote)

  return quotes

if __name__ == '__main__':
  meigen = []
  for i in range(1, 99):
    meigen += getMeigen(i)
    print(f'page {i} done')
    sleep(2)
  with open('data/meigen.txt', 'w', encoding='utf_8_sig') as f:
    f.write('\n'.join(meigen))
