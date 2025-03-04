import requests
from bs4 import BeautifulSoup as Soup

class Scraper:

  home_page = 'https://www.mercadolivre.com.br/'
  categories_ul_class = 'nav-categs-departments'

  def getHtml(self, url):
    try:
      response = requests.get(url, timeout=5, allow_redirects=False)
      if response.ok:
        html = response.text
        return html
      
      else:
        return None
    
    except requests.RequestException as e:
      print(f'Excessão ao fazer uma requisição GET na url: {url}; excessão: {e}')
      return None

  def getCategories(self):
    html = self.getHtml(self.home_page)
    if html is None:
      return None
    
    soup = Soup(html, 'html.parser')
    categories_list = soup.find('ul', class_=self.categories_ul_class)
    if categories_list is None:
      print('Nao foi possivel obter as categorias!')
      return None
    
    categories_list = categories_list.find_all('li')    
    categories = [ category.text.strip() for category in categories_list ]
    categories.pop()
    return categories
  
scraper = Scraper()
