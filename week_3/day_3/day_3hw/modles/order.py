class Order:
    def __init__(self, customer_name, order_date, quantity, book_title, description):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.book_title = book_title
        self.description = description


order1 = Order("larry", "30/Sep", "2", "Little Prince", "Haven't read it sorry")
order2 = Order("Tim", "2/July", "1", "Why I don't like CSS", "10000 reasons not like CSS")

orders = [order1, order2]