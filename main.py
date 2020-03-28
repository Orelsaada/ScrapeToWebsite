from Scraper.BugScraper import scrape
from mail import mail
# from index import app


def mainLoop():
    scrape()
    # mail()
    # app.run()


if __name__ == '__main__':
    mainLoop()