import random


class Die:
    """ A playing die """
    def __init__(self):
        self.current_value = 0

    def roll(self):
        """ behavior, roll a random number from 1 to 6 """
        DICE_RANGE = (1, 6)
        self.current_value = random.randint(*DICE_RANGE)
