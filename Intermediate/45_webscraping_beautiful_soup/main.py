from bs4 import BeautifulSoup

with open("website.html") as f:
    soup = BeautifulSoup(f)

print(soup.prettify())

print(soup.title)


class Foo():
    def __init__(self):
        pass


foo = Foo()
