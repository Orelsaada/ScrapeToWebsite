from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import os

# Set the location to create the csv (ReadFromCSV directory)
os.chdir('..')
folderpath = os.path.join(os.getcwd(), 'ReadFromCSV')
print(folderpath)
global filepath
filepath = os.path.join(folderpath, 'BugData.csv')
print(filepath)


def scrape():
    # open a connection and grab the page
    my_url = "https://www.bug.co.il/fpage.asp?c=2331&t=123"
    uClient = urlopen(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")

    f = open(filepath, 'w')
    f.write('Game:, Price(il-coin):\n')

    divs = page_soup.findAll('div', {'class': 'bordered-product product-cube-inner-1'})
    number = 0
    for div in divs:

        number = number+1

        name = div.h4.a.text.strip().replace('"', '')
        # print(f'{number}) {name}', end='')

        price = div.findAll("span")[1].text.replace("₪", "")
        # print(f' ---- {price}')

        f.write(name + ',' + price + '\n')
    f.close()
    print("Scraped!")


if __name__ == '__main__':
    scrape()