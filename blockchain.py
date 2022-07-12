# initializing our empty blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]
# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(transaction_amount):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    last_transaction = get_last_blockchain_value()
    if last_transaction == None:
        blockchain.append([1])
 
    blockchain.append([get_last_blockchain_value(), transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    return float(input('Please Enter your transaction amount:'))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockvhsin list to the console
    print('')
    for block in blockchain:
        print('Outputting Block')
        print(block)

# tx_amount = get_user_input()
# add_value(tx_amount)
# tx_amount = get_user_input()
# add_value(tx_amount)
# tx_amount = get_user_input()
# add_value(tx_amount)


def adding_transactions():
    while True:
        print('\n\nPlease choose')
        print('1: Add a new transaction value')
        print('2: Output the blockchain blocks')
        print('Q: to Exit')
        user_choice = get_user_choice()
        if user_choice == '1':
            tx_amount = get_transaction_value()
            add_transaction(tx_amount)
        elif user_choice == '2':
            print(blockchain)

        elif user_choice == 'q':
            break
        else:
            print('Invalid value, try again!')


adding_transactions()
print('Done!')
