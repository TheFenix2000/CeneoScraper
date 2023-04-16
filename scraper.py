import requests
import json
from bs4 import BeautifulSoup

def get_cos():
    pass

# product_code = input("Enter Product Code: ")
product_code = "113897315"

# url = "https://www.ceneo.pl/" + product_code + "#tab=reviews"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
r = requests.get(url)

if r.ok:
    page_dom = BeautifulSoup(r.text, 'html.parser')
    opinions = page_dom.select("div.js_product-review")

    opinions_all = []
    for opinion in opinions:
        single_opinion = {
            "opinion_id": opinion['data-entry-id'],
            "author": opinion.select_one('span.user-post__author-name').get_text().strip(),
            "recommendation": opinion.select_one('span.user-post__author-recomendation > em').get_text().strip(),
            "score": opinion.select_one('span.user-post__score-count').get_text().strip(),
            "purchased": opinion.select_one('div.review-pz').get_text().strip(),
            "opinion_date": opinion.select_one('span.user-post__published > time:nth-child(1)')['datetime'].strip(),
            "purchase_date": opinion.select_one('span.user-post__published > time:nth-child(2)')['datetime'].strip(),
            "likes": opinion.select_one('button.vote-yes')['data-total-vote'].strip(),
            "dislikes": opinion.select_one('button.vote-no')['data-total-vote'].strip(),
            "content": opinion.select_one('div.user-post__text').get_text().strip(),
            "cons": [tag.text.strip() for tag in opinion.select('div.review-feature__title--negatives ~ div.review-feature__item')],
            "pros": [tag.text.strip() for tag in opinion.select('div.review-feature__title--positives ~ div.review-feature__item')]
        }
        opinions_all.append(single_opinion)
    print(json.dumps(opinions_all, indent=4, ensure_ascii=False))