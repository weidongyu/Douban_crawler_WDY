import requests
import re
import Book_Info
import time
import numpy as np
import csv
import sys

from bs4 import BeautifulSoup

url = 'http://book.douban.com/people/asyanyang/wish?start=1665&sort=time&rating=all&filter=all&mode=grid'
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

bookNo = 1674 - 1
books = []
pattern = re.compile('\d{7,}')
page_num = 0
csvfile  = open('Chuxu_wish.csv', "w")
writer = csv.writer(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
#
# for row in reader:
#     writer.writerow(row)

response = requests.get(url)
print(response)

# response.headers['content-type']
content = response.content

currPage = BeautifulSoup(content, "html.parser")
# spanSet = soup.findAll('a', attrs = {"class": "nbg"})
# nextUrl = 'null'
# nextPageFlag = currPage.find(rel='next')
# print(nextPageFlag['href'])

while True:

    #    print("当前页面:"+url)
    #    print("下一页"+nextPageFlag['href'])
    #time.sleep(np.random.rand()*5)
    page_num += 1
    print ('Downloading Information From Page %d', page_num)
    content = requests.get(url, headers=hds[page_num%len(hds)]).content
    currPage = BeautifulSoup(content, "html.parser")
    bookLinkSet = currPage.find_all('a', attrs={"class": "nbg"})
    wishTimeSet = currPage.find_all('span', attrs={'class': "date"})
    # print(wishTimeSet)
    # print(bookLinkSet)

    for bookLink, wishTime in zip(bookLinkSet, wishTimeSet):
        subjectLink = bookLink['href']
        wish = wishTime.string
        bookID = re.search(pattern, subjectLink).group()
        book = Book_Info.BookInfo(book_id = bookID, wish_time = wish, bookLink = subjectLink)
        writer.writerow([book.bookID, book.title, book.numRaters, book.averageRate, book.numPages, book.bookLink])
        books.append(book)
        print(bookNo + book.bookCount)
        # print(bookID, wish)
        # print(subjectLink)

    if currPage.find(rel='next') is None:
        break
    else:
        url = currPage.find(rel='next')['href']
        #    print(nextPageFlag)
        # print(soup.prettify())

csvfile.close()

# workbook  = xlsxwriter.Workbook('Chuxu_wish.xlsx')
# worksheet = workbook.add_worksheet()
#
# worksheet.write(books)
#
# workbook.close()