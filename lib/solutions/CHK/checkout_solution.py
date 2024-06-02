

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # create prices and offers
    price_table = {'A': 50, 'B':30, 'C':20, 'D': 15}
    offers = {'A':(3,130), 'B':(2,45)}

    for char in skus:
        if char not in price_table:
            return -1
    
    # count the number of each sku
    counts = {item: skus.count(item) for item in price_table}

    total_price = 0

    for item, (offer_count, offer_price) in offers.items():
        if counts[item] >= offer_count:
            total_price += (counts[item] // offer_count) * offer_price
            counts[item] %= offer_count 

    for item, count in counts.items():
        total_price += count * price_table[item]
    
    return total_price



