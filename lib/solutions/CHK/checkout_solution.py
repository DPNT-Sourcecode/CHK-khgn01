

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
    
    for group_name, (required_qty, group_price, items) in group_offers.items():
        group_count = sum(counts[item] for item in items)
        if group_count >= required_qty:
            total_price += (group_count // required_qty) * group_price
            remaining_items = group_count % required_qty

         
            sorted_items = sorted(items, key=lambda x: price_table[x], reverse=True)

            remaining_counts = {}
            for item in sorted_items:
                remaining_counts[item] = counts[item]

            for _ in range(group_count - remaining_items):
                for item in sorted_items:
                    if remaining_counts[item] > 0:
                        remaining_counts[item] -= 1
                        break

            # update counts after applying group discount
            for item in items:
                counts[item] = remaining_counts[item]

    # apply multi offers
    for item, offers in multi_offers.items():
        for offer_count, offer_price in sorted(offers, key=lambda x: x[0], reverse=True):
            if counts[item] >= offer_count:
                total_price += (counts[item] // offer_count) * offer_price
                counts[item] %= offer_count 
    
    # group offers
    
            

    for item, count in counts.items():
        total_price += count * price_table[item]
    
    return total_price
