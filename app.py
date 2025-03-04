from flask import Flask
from scraping.scraper import scraper

app = Flask(__name__)

@app.route('/api/categories')
def returnCategories():
  categories = scraper.getCategories()
  return categories

app.run(debug=True)
