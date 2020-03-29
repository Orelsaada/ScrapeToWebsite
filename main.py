from Scraper.BugScraper import scrape
from mail import mail


def mainLoop():
    scrape()
    mail()


if __name__ == '__main__':
    mainLoop()