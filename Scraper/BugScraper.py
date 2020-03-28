from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


def scrape():
    # open a connection and grab the page
    my_url = "https://www.bug.co.il/fpage.asp?c=2331&t=123"
    uClient = urlopen(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")

    filename = r"C:\Users\Orel\Desktop\ScrapingToWebsite\ReadFromCSV\BugData.csv"
    f = open(filename, 'w')
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
