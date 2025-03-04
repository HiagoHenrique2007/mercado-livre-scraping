from flask import Flask, render_template, url_for
from scraping.scraper import scraper

app = Flask(__name__)

@app.route('/')
def returnCategories():
  categories = scraper.getCategories()
  product = scraper.getDatasProduct('https://www.mercadolivre.com.br/teclado-soft-silence-preto-com-fio-teclas-baixas-multilaser-idioma-portugus-brasil/p/MLB22833016#polycard_client=recommendations_home_navigation-trend-recommendations&reco_backend=machinalis-homes-univb&wid=MLB3815285341&reco_client=home_navigation-trend-recommendations&reco_item_pos=2&reco_backend_type=function&reco_id=f4ab0ad6-1c7f-4e9d-be6c-b2cacca4c2ed&sid=recos&c_id=/home/navigation-trend-recommendations/element&c_uid=bfc46f02-e1fe-4150-80a8-4eff93b534f5')
  if categories['sucess'] == True and product['sucess'] == True:
    return render_template('index.html', categories=categories, result=product)

app.run(debug=True)
