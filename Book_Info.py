import requests
import time
import numpy as np

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

class BookInfo:
    bookCount = 0

    def __init__(self,  book_id = None,
                        wish_time = None,
                        title = None,
                        price = None,
                        pub = None,
                        num_raters = None,
                        numPages = None,
                        average_rate = None,
                        bookLink = None):

        self.bookID   = book_id
        self.wishTime = wish_time
        self.title    = title
        self.price    = price
        self.pub      = pub
        self.numRaters = num_raters
        self.numPages  = numPages
        self.averageRate = average_rate
        self.bookLink = bookLink

        self.get_book_api()

        BookInfo.bookCount += 1

    def displayCount(self):
        print("Total Book %d" % BookInfo.bookCount)

    def display_book_info(self):
        print("Title: ", self.title,  ", 想读时间:", self.wishTime)

    def get_book_api(self):
        bookApiUrl = 'https://api.douban.com/v2/book/' + self.bookID + '?fields=title,rating,pages'
        #time.sleep(np.random.rand()*5)
        resp = requests.get(bookApiUrl, headers=hds[np.random.randint(3)%len(hds)])
        bookApiWeb = resp.json()
        print(bookApiWeb)
        self.title = bookApiWeb['title']
        self.numRaters = bookApiWeb['rating']['numRaters']
        self.averageRate = bookApiWeb['rating']['average']
        self.numPages = bookApiWeb['pages']
