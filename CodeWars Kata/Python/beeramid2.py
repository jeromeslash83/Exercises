def beeramid(bonus, price):
    beers = bonus // price
    level = 0
    used_beers = 0
    while beers >= (level + 1)**2:
        level +=1
        beers -= level**2
        used_beers += level**2
        
    return level
