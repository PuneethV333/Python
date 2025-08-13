from bs4 import BeautifulSoup as bs
import requests
link = 'https://www.flipkart.com/apple-iphone-16-pro-max-black-titanium-256-gb/product-reviews/itm7e75db4f27bd5?pid=MOBH4DQFNXH8SZ9D&lid=LSTMOBH4DQFNXH8SZ9DUXE3QP&marketplace=FLIPKART'
page = requests.get(link)
print(page)
soup = bs(page.content,'html.parser')
#print(soup)
print(soup.prettify())
name = soup.find_all("p",class_="_2NsDsF AwS1CA")
print(name)
cust_name = []
for i in range(0,len(name)):
    cust_name.append(name[i].get_text())
    len(cust_name)
    print(cust_name)

title = soup.find_all("p",class_ = "z9E0IG")
review_tile = []
for i in range(0,len(title)):
    review_tile.append(title[i].get_text())
    review_tile

statment = soup.find_all("p",class_ = "ZmyHeo")
review_statment = []
for i in range(0,len(statment)):
    review_statment.append(statment[i].get_text())
    review_statment

rating = soup.find_all("p",class_ = "XQDdHH Ga3i8K")
cust_rating = []
for i in range(0,len(rating)):
    cust_rating.append(rating[i].get_text())
    cust_rating

import pandas as pd

df = pd.DataFrame()
df['cust_name']
df['review_tile']
df['review_statment']
df['cust_rating']
df.to_csv('reviewdefset.csv', index=False, encoding='utf-8')

print("Scraping complete. Saved to reviewdefset.csv")