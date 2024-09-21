
def add():
    my_dict = {}
    order = 1
    item = 'fod'
    quantity = 3
    my_dict['Order number'] = order
    my_dict['Item Name'] = item
    my_dict['Quantity'] = quantity
    return my_dict

def output(my_dict):
    #Checks to see if the datatype is correct
    if not isinstance(my_dict['Order number'], int) or not isinstance(my_dict['Item Name'],str) or not isinstance(my_dict['Quantity'],int):
        #prints error if invalid data type
        raise TypeError("invalid input type")

    if not my_dict:
        #the following message if the inventory is empty
        print("inventory is empty")
    else:
        #prints the order number, item name, and the quantity
        print(f"Order Number: {my_dict['Order number']} " f"Item Name: {my_dict['Item Name']} " f"Quantity: {my_dict['Quantity']}", flush=True)
