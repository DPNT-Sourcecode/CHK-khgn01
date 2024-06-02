

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # create prices and offers
    price_table = {'A': 50, 'B':30, 'C':20, 'D': 15, 'E': 40}
    multi_offers = {'A':[(3,130), (5,200)], 'B':[(2,45)]}
    free_offers = {'E':(2, 'B')}

    for char in skus:
        if char not in price_table:
            return -1
    
    # count the number of each sku
    counts = {item: skus.count(item) for item in price_table}

    total_price = 0

    # do free offers first
    for item, (required_qty, free_item) in free_offers.items():
        if counts[item] >= required_qty:
            free_qty = (counts[item] // required_qty)
            counts[free_item] = max(0, counts[free_item] - free_qty)

    # apply multi offers
    for item, offers in multi_offers.items():
        for offer_count, offer_price in sorted(offers, key=lambda x: x[0], reverse=True):
            if counts[item] >= offer_count:
                total_price += (counts[item] // offer_count) * offer_price
                counts[item] %= offer_count 

    for item, count in counts.items():
        total_price += count * price_table[item]
    
    return total_price


