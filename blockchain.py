# initializing our empty blockchain list
blockchain = [[1]]


def get_last_blocchain_value():
    """ Returns the last value of the current blockchain. """
    return blockchain[-1]
# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_value(transaction_amount):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    blockchain.append([get_last_blocchain_value(), transaction_amount])


def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    return float(input('Please Enter your transaction amount:'))


tx_amount = get_user_input()
add_value(tx_amount)
tx_amount = get_user_input()
add_value(tx_amount)
tx_amount = get_user_input()
add_value(tx_amount)

print(blockchain)
