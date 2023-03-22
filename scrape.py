# Analytic Index Assessment 
from bs4 import BeautifulSoup
import requests
from csv import writer

# saving the url of the page being scraped to a var and making a request to said url

# creating the csv file we are going to write to
with open('books.csv','w', encoding= 'utf8',newline= '') as f:
    
    # creating my writer and writing my header to csv
    writer = writer(f)
    header = ['Title', 'Product Link', 'Price', 'Availability']
    writer.writerow(header)

    url = "http://books.toscrape.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')


    # find all the articles in the html file with the class name "product_pod" and save them to a list
    lists = soup.find_all('article', class_= "product_pod")

    # creating while loop to loop through every page of the main site, when last page is reached we're done
        
    # building our CSV file
    for list in lists:
    # searches first for the h3 tag, then for the a tag within that, then extracts the value of the attribute 'title'
        title = list.find('h3').find('a').attrs['title']
        # print(title)

        prod_link = url + list.find('h3').find('a').attrs['href']
        # print(prod_link)

        price = list.find(class_='price_color').text
        # print(price)
        availability = list.find(class_='instock availability').text.strip()
        # print(availability)
        
        # test to check if it all worked
        info = [title, prod_link, price, availability]
        # print(info)
        writer.writerow(info)

    #next = soup.find(class_='next').find('a')['href']