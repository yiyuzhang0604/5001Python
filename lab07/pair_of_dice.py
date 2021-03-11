from die import Die


class PairOfDice:
    """" Constructor of a pair of dice, has 2 attributes, which is two dices"""
    def __init__(self):
        self.dice1 = Die()
        self.dice2 = Die()

    def roll_dice(self):
        """ roll the dice, and get the current_value respectively """
        self.dice1.roll()
        self.dice2.roll()

    def current_value(self):
        """ sum up two current_values from two dices """
        return self.dice1.current_value + self.dice2.current_value
