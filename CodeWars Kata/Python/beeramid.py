def beeramid(bonus, price):
    max_cans = bonus // price
    total_cans = 0
    remaining = max_cans
    complete_levels = 0
    while True:
        level_cans = (complete_levels + 1) ** 2
        if level_cans <= max_cans:
            complete_levels += 1
            total_cans += level_cans
            max_cans -= level_cans
        else:
            break
    return complete_levels
