def line(katz_deli):
    if len(katz_deli) == 0:
        print ("The line is currently empty.")
    else:
        customers = []
        for idx, customer in enumerate(katz_deli):
            customers.append(f'{idx + 1}' + f'. {customer}')
        line_statement = ' '.join(customers)
        line_statement = "The line is currently: " + line_statement
        print(line_statement)

def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    print(f'Welcome, {new_customer}. You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli[0]}.')
        del(katz_deli[0])