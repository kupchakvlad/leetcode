class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration


def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")


def maxExpirationDay(fridge: list):
    if len(fridge) == 0: return -1
    exp = 0
    for food in fridge:
        if food.expiration > exp:
            exp = food.expiration
    return exp


def histogramOfExpirations(fridge):
    maxExpiration = maxExpirationDay(fridge)
    exp_list = [0] * (maxExpiration + 1)
    if len(exp_list) == 0: return []
    for food in fridge:
        exp_list[food.expiration] += 1
    return exp_list


def cumulativeSum(histogram):
    histogram_copy = histogram[:]
    exp_list = [0] * len(histogram_copy)

    if len(histogram_copy) == 0: return []

    exp_list[0] = histogram_copy[0]

    for i in range(1, len(histogram_copy)):
        exp_list[i] = exp_list[i - 1] + histogram_copy[i]

    return exp_list


def sortFoodInFridge(fridge):
    cumulative_sum = cumulativeSum(histogramOfExpirations(fridge))
    fridge_copy = fridge[:]
    sorted_fridge = [None] * len(fridge_copy)

    for food in fridge_copy:
        exp = food.expiration
        posInd = cumulative_sum[exp] - 1
        sorted_fridge[posInd] = food
        cumulative_sum[food.expiration] -= 1

    return sorted_fridge


def reverseFridge(fridge):
    if len(fridge) == 0: return []
    return fridge[::-1]


def eatFood(name, fridge):
    new_fridge = fridge[:]
    took = []
    minimal = float('inf')
    if len(new_fridge) == 0: return []
    for i in range(len(new_fridge)):
        if new_fridge[i].name == name:
            took.append(new_fridge[i])
    for i in range(len(took)):
        if took[i].expiration < minimal:
            minimal = took[i].expiration
    for food in took:
        if minimal == food.expiration:
            new_fridge.remove(food)
    return new_fridge
