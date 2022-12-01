class Book:
    def __init__(self, title, years, price, author, id=None):
        self.title = title
        self.years = years
        self.price = price
        self.author = author
        self.id = id