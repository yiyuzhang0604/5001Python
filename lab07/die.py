import random


class Die:
    """ A playing die """
    def __init__(self):
        self.current_value = 0

    def roll(self):
        """ behavior, roll a random number from 1 to 6 """
        dice_begin = 1
        dice_end = 6
        self.current_value = random.randint(dice_begin, dice_end)
