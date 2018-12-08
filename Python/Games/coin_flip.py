from random import random

# def flip_coin():
#     # generate random number 0-1
#     flip = random()
#     if flip > 0.5:
#         return "Heads"
#     else:
#         return "Tails"

# print(flip_coin())

def flip_coin():
    # generate random number 0-1
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"
    # it helps to write similar functions with different capitalizations or other small differences, to be able to identify it upon running the function (for tweaks and stuff)

print(flip_coin())