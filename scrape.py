# The script file that does the actual web scraping


from bs4 import BeautifulSoup
import requests
from csv import writer

# creating a var for the initial url along with the initial page count
page_cnt = 1
url = f"http://books.toscrape.com/catalogue/page-{page_cnt}.html"

# creating the csv file we are going to write to
with open('books.csv','w', encoding= 'utf8',newline= '') as f:
    
    # creating my writer and writing my header to csv
    writer = writer(f)
    header = ['Title', 'Product Link', 'Price', 'Availability']
    writer.writerow(header)

    # using a while loop to keep running through the script for every page of data
    while url:
        #building the page with the url of the current page
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')


        # find all the articles in the html file with the class name "product_pod" and save them to a list of books
        books = soup.find_all('article', class_= "product_pod")
            
        # grabbing the info from each of the books on the page and saving them to our CSV file
        for book in books:

            #finds the 'h3' tag, then for the 'a' tag within that and extracts the value of the 'title' attribute
            title = book.find('h3').find('a').attrs['title']

            #builds the link for the book's page using the base url plus its slug
            prod_link = 'http://books.toscrape.com/' + book.find('h3').find('a').attrs['href']

            #find the price of the book from the 'price_color' class
            price = book.find(class_='price_color').text

            #find the availability of the book from the 'instock availability' class, stripping away the newline operators and unnecessary whitespace
            availability = book.find(class_='instock availability').text.strip()
            
            # gathers all the info about this specific book to write to CSV all at once
            info = [title, prod_link, price, availability]
            writer.writerow(info)

        # if the 'next' button isnt found on the page, we've reached the final page and are done!
        if not soup.find(class_='next'):
            break

        # if the next button is found, we increment the page count up by one and build our new URL to use next loop
        page_cnt = page_cnt + 1
        url = f"http://books.toscrape.com/catalogue/page-{page_cnt}.html"

        #needless print of the URL for testing purposes, 
        #leaving this intentionally because it gives the user feedback that the program is running during its long runtime
        print(url)
