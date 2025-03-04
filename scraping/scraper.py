import requests
from bs4 import BeautifulSoup as Soup

class Scraper:

  home_page = 'https://www.mercadolivre.com.br/'
  categories_ul_class = 'nav-categs-departments'


  sucess_false =  {
    'sucess': False,
  }

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
      return 
    
    soup = Soup(html, 'html.parser')
    categories_list = soup.find('ul', class_=self.categories_ul_class)
    if categories_list is None:
      print('Nao foi possivel obter as categorias!')
      return self.sucess_false
    
    categories_list = categories_list.find_all('li')    
    categories = [ category.text.strip() for category in categories_list ]
    categories.pop()
    return {
      'sucess': True,
      'categories': categories
    }
  
  def getLinkProduct(self, url)

  def getDatasProduct(self, url):
    html = self.getHtml(url)
    soup = Soup(html, 'html.parser')
    product_name = soup.find('h1')
    price = soup.find('meta', itemprop='price')
    rating = soup.find('span', class_='ui-pdp-review__rating')
    if product_name and price and rating:
      product = {
        'name': product_name.text,
        'price': price['content'],
        'rating': rating.text
      }
      return {
        'sucess': True,
        'product': product
      }
    
    else:
      return self.sucess_false

    






scraper = Scraper()
