import requests
# product_code = input("Enter Product Code: ")
product_code = "113897315"
# url = "https://www.ceneo.pl/" + product_code + "#tab=reviews"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews".format(product_code)

r = requests.get(url)
print(r.status_code)