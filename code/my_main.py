import my_code

def main():
    try:
        choice = int(input("enter 1 to add to the dictionary"))
        if choice == 1:
        #calls the function add from my code and stores it in orders
            orders = my_code.add()
        #calls the function output and processes order in it.
            my_code.output(orders)
        else:
            print("empty")
    except TypeError as e:
        print(f"error {e}")
main()
