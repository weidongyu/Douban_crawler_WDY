from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Book_Info

BrowserObj_dirver = webdriver.Chrome()

BrowserObj_dirver.get("http://book.douban.com/people/asyanyang/wish?start=0&sort=time&rating=all&filter=all&mode=grid")

BrowserObj_dirver.implicitly_wait(3)

EditObj_element = BrowserObj_dirver.find_element_by_name('wd')

EditObj_element.send_keys("Hello WebDriver!")
EditObj_element.send_keys(Keys.RETURN)

print (BrowserObj_dirver.title)

BrowserObj_dirver.close()