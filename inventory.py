# === Import Modules ===
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:
    '''Class representing one shoe product'''


    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    def get_cost(self):
        '''Returns cost of shoe product'''
        return self.cost


    def get_quantity(self):
        '''Returns quantity of shoe product'''
        return self.quantity


    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


#=============Shoe list===========
# List of Shoe objects
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    Reads data from inventory.txt (skipping header line) and creates new Shoe 
    objects from data in each line.
    Appends each Shoe object to shoe_list.
    '''
    with open("inventory.txt", "r", encoding="utf-8") as i_file:
        next(i_file) #skip header line
        for line in i_file:
            one_line = line.strip()
            one_line = one_line.split(",")
           # Create Shoes object
            one_shoe = Shoe(
                one_line[0],
                one_line[1],
                one_line[2],
                one_line[3],
                one_line[4]
               )
            shoe_list.append(one_shoe)


def capture_shoes():
    '''
    Allows a user to capture data about a shoe and use this data to create 
    a Shoe object and append this object inside the shoe_list.
    '''
    new_country = input("Enter country of product:\n").capitalize()
    new_code = input("Enter product code:\n") #starting with SKU?
    new_product = input("Enter product name:\n")
    new_cost = int(input("Enter product cost as whole number:\n"))
    new_quantity = int(input("Enter quantity of pruduct:\n"))

    new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
    shoe_list.append(new_shoe)
    return "Product data captured"

def view_all():
    '''
    Iterates over the shoes_list and prints the details of the shoes returned 
    from the __str__ function. Presents data in table format.
    '''
    product_list = [["Country","Code","Product","Cost","Quantity"]]
    
    for product in shoe_list:
        product = str(product)
        product = product.split(",")
        product_list.append(product)
    
    # Tabulate data in terminal
    print(tabulate(product_list, headers="firstrow"))

def re_stock():
    '''
    Finds the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. User is asked if they
    want to restock and the quantity of shoes to be added.
    This quantity is updated on the file for this shoe.
    '''
    lowest = int(shoe_list[0].quantity)
    for shoe_item in shoe_list:
        if lowest > int(shoe_item.quantity):
            lowest = int(shoe_item.quantity)
            low_stock = shoe_item

    print(str(low_stock))
    more_stock = input(f'''
    Product with the lowest stock:
    Product : {low_stock.product} 
    Code: {low_stock.code} 
    Stock level: {low_stock.quantity}
        Would you like to restock this item? Type 'y' or 'n'\n
''').lower()
    
    if more_stock == "y":
        while True:
            try:
                new_quantity = int(input("Enter new stock to be added :\n"))
                low_stock.quantity = int(low_stock.quantity) + new_quantity
                print("Product restocked")
                break
            except ValueError:
                print("Error, please enter a whole number")
    elif more_stock == "n":
        pass
    else:
        print("Error, that was not a valid key")



def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    search_code = input("Enter product code to search, e.g. 'SKU93222':\n")
    for shoe_obj in shoe_list:
        if search_code == shoe_obj.code:
            print(f'''
            Product:  {shoe_obj.product}
            Code:     {shoe_obj.code}
            Country:  {shoe_obj.country}
            Quantity: {shoe_obj.quantity}
            ''')
    print("Sorry, no such product. Please enter correct product code.")

def value_per_item():
    '''
    Calculates the total value for each item (value = cost * quantity)
    '''
    value_list = []
    for shoe in shoe_list:
        one_product = []
        value = int(shoe.cost) * int(shoe.quantity)
        one_product.append(shoe.product)
        one_product.append(str(value))
        value_list.append(one_product)

    print("\n" + tabulate(value_list, headers=["Product", "Total value"]))


def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    highest = int(shoe_list[0].quantity)
    for item in shoe_list:
        if highest < int(item.quantity):
            highest = int(item.quantity)
            high_stock = item
    print(highest) 
    print(f"{high_stock.product} is on sale!")
    


def re_write_file():
    with open("test.txt", "w", encoding="utf-8") as in_file:
        for shoe in shoe_list:
            in_file.write(str(shoe) + "\n")

    
#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

#while True:



# To avoid unnecessarily calling the dunder method itself, use the built-in
# function that calls them (str() calls __str__() method implemented in class object)
#print(str(shoe1))

read_shoes_data()
#view_all()
#re_stock()
#re_write_file()

#search_shoe()
#value_per_item()
highest_qty()