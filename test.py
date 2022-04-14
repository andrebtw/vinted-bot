from re import I
from pyVinted import Vinted

vinted = Vinted("fr")

# search (url, number of items, page_number)
items = vinted.items.search("https://www.vinted.fr/femmes?order=newest_first&price_to=60&currency=EUR", 10, 1)

# returns a list of objects : item
item1 = items[0]

# title
item1.title

# id
item1.id

# photo url

item1.photo

# brand title
item1.brand_title

# price
item1.price

# url
item1.url

# currency
item1.currency

# Getting all the 10 items into a list
items_d = []
for i in items:
    items_d.append(i)

print(items_d[5].title)