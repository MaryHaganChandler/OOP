class RetailItem:

    def __init__(self, item_desc, inv, price):
        self.__item_desc = item_desc
        self.__inv = inv
        self.__price = price

    def set_item_desc(self, item_desc):
        self.__item_desc = item_desc
    
    def set_inv(self, inv):
        self.__inv = inv

    def set_price(self, price):
        self.__price = price

    def get_item_desc(self):
        return self.__item_desc

    def get_inv(self):
        return self.__inv

    def get_price(self):
        return self.__price