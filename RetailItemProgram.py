import RetailItemClass as ric

def main():
    item_1 = ric.RetailItem("Jacket",12,59.95)
    item_2 = ric.RetailItem("Designer Jeans",40,34.95)
    item_3 = ric.RetailItem("Shirt",20,24.95)

    print("Item #:\t","Description\t","Units in Inventory\t","Price")
    print("Item 1: ", item_1.get_item_desc(),"\t\t", item_1.get_inv(), "\t\t",item_1.get_price())
    print("Item 2: ", item_2.get_item_desc(),"\t", item_2.get_inv(), "\t\t",item_2.get_price())
    print("Item 3: ", item_3.get_item_desc(), "\t\t\t", item_3.get_inv(), "\t\t",item_3.get_price())

main()