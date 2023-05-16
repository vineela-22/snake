def change(pos, snakes, ladders):
    newposition = pos
    if pos in snakes:
        newposition = snakes[pos]
    elif pos in ladders:
        newposition = ladders[pos]
    return newposition

def check(initialposition, diceroll):
    #newpostion = initialposition
    if initialposition + diceroll <= 32:
        newposition = initialposition + diceroll
    else:
        newposition = initialposition
    return newposition                  
