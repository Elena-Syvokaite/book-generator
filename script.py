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

book_container = page_soup.findAll("div", {"class":"book-preview book-preview-grid-item span3 tablet-span6 mobile-span6"})
print(len(book_container))

# all_books = page_soup.find(id="all_votes")

# book_titles = all_books.find_all(class_= "bookTitle").get_text()
# print(book_titles)

# author_name = all_books.find_all(class_= "authorName")
# print(author_name)