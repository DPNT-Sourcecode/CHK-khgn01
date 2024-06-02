

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # create prices and offers
    price_table = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
        'Y': 20, 'Z': 21
    }
    multi_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)]
    }
    free_offers = {'E':(2, 'B'), 'F': (2, 'F'), 'N':(3, 'M'), 'R': (3,'Q'), 'U':(3, 'U')}


    group_offers = {'g1': (3, 45, ['S', 'T', 'X', 'Y', 'Z'])}

    for char in skus:
        if char not in price_table:
            return -1
    
    # count the number of each sku
    counts = {item: skus.count(item) for item in price_table}

    total_price = 0

    # do free offers first
    for item, (required_qty, free_item) in free_offers.items():
        if item == free_item:
            if counts[item] >= required_qty + 1:
                free_qty = (counts[item] // (required_qty + 1))
                counts[item] -= free_qty
        else:
            if counts[item] >= required_qty:
                free_qty = (counts[item] // required_qty)
                counts[free_item] = max(0, counts[free_item] - free_qty)

    # apply multi offers
    for item, offers in multi_offers.items():
        for offer_count, offer_price in sorted(offers, key=lambda x: x[0], reverse=True):
            if counts[item] >= offer_count:
                total_price += (counts[item] // offer_count) * offer_price
                counts[item] %= offer_count 
    
    # group offers
    def apply_group_discount(group_items, group_price):
        group_counts = [counts[item] for item in group_items]
        min_count = min(group_counts)
        total_group_price = min_count * group_price
        for item in group_items:
            counts[item] -= min_count
        return total_group_price

    for group_name, (required_qty, group_price, group_items) in group_offers.items():
        group_counts = [counts[item] for item in group_items]
        while min(group_counts) >= required_qty:
            total_price += apply_group_discount(group_items, group_price)
            

    for item, count in counts.items():
        total_price += count * price_table[item]
    
    return total_price






