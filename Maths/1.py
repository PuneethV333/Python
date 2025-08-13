from bs4 import BeautifulSoup as bs
import requests
link = 'https://www.flipkart.com/apple-iphone-16-pro-max-black-titanium-256-gb/product-reviews/itm7e75db4f27bd5?pid=MOBH4DQFNXH8SZ9D&lid=LSTMOBH4DQFNXH8SZ9DUXE3QP&marketplace=FLIPKART'
page = requests.get(link)
print(page)
soup = bs(page.content,'html.parsar')
#print(soup)
print(soup.prettify())
name = soup.find_all("p",class_="_2NsDsF AwSlcA")
print(name)
cust_name = []
for i in range(0,len(name)):
    cust_name.append(name[i].get_text())
    len(cust_name)
    print(cust_name)