# **Scraping do mercado livre**

webservice que raspara o mercado livre e mostrara informaçoes sobre o que foi raspado.

## **Como funcionará o processo de scraping:**


tera uma API que ficara responsavel por raspar os dados e devolver eles para o front-end.
a API tera endpoints expecificos, como por exemplo um endpoint que raspa por categoria e a categoria sera definida pelo front-end, mas antes, o back-end raspara as categorias do mercado-livre e mandara para o front-end para nao ter erros e se caso tiver alguma auteração no mercado-livre isso reflita no webservice.

### **Parametros de busca:**


busca por itens: https://lista.mercadolivre.com.br/<item>

busca por categoria: https://lista.mercadolivre.com.br/<category>


### **O que o Scraper precisa?**


- precisa de função para obter o html
- precisa de função para obter links com parametros
- precisa de funções para obter preço, nome, avaliação, freete, localidade, etc

