from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.waterstones.com/category/fiction/classic-fiction/page/1e'
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

# parsing 

# parsing info from 1 item
container = bookInfo[0]

bookTitle = container.div.a.get_text() # prints The Plague
print(bookTitle) 

bookAuthor = container.span.get_text() # prints Albert Camus 
print(bookAuthor) 

