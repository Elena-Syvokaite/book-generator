from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd

my_url = 'https://www.waterstones.com/category/fiction/classic-fiction/page/2e'
# opens connection, grabs the page
urlGet = uReq(my_url)
# variable with raw html text
page_html = urlGet.read()
# closes the connection
urlGet.close()

page_soup = soup(page_html, "html.parser")

# grabs info from page_soup variable
bookInfo = page_soup.findAll("div", {"class":"info-wrap"})
print(len(bookInfo)) # prints 24 

# testing parsing for 1 item
bookTitle = bookInfo[0].div.a.get_text() # prints The Plague
bookAuthor = bookInfo[0].span.get_text() # prints Albert Camus 

# list comprehension for items in bookInfo
bookTitles = [item.div.a.get_text() for item in bookInfo]
bookAuthors = [item.span.get_text().strip() for item in bookInfo] 

# tidies info into table
bookStuff = pd.DataFrame(
    {
        'Book_title': bookTitles,
        'Book_author': bookAuthors,
    })
print(bookStuff)