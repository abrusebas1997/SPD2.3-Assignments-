# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.

def get_price():
    if base() > 1000: 
        discount_factor = 0.95
    else: 
        discount_factor = 0.98
    return base_price * discount_factor

def get_base_price():
    base_price = quantity * item_price
    discount_factor = 0
    return base_price