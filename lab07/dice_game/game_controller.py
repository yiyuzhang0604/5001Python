from pair_of_dice import PairOfDice


class GameController:
    """ A controller for street craps game """

    def __init__(self):
        self.shooter = PairOfDice()
        self.point = 0

    def start_play(self):
        """ Start the game """
        # First round
        start = input("Press enter to roll the dice...")
        print("")
        self.shooter.roll_dice()
        self.point = self.shooter.current_value()
        FIRST_ROUND_WIN = 7
        FIRST_ROUND_WIN2 = 11
        FIRST_ROUND_LOSE = 2
        FIRST_ROUND_LOSE2 = 3
        FIRST_ROUND_LOSE3 = 12
        LOSE = 7

        if(self.point == FIRST_ROUND_WIN or self.point == FIRST_ROUND_WIN2):
            print(f"You rolled {self.point}. You win!")
            return

        if(self.point == FIRST_ROUND_LOSE or self.point == FIRST_ROUND_LOSE2 or
                self.point == FIRST_ROUND_LOSE3):
            print(f"You rolled {self.point}. You lose.")
            return

        print(f"Your point is {self.point}.")
        self.shooter.roll_dice()
        # Second round
        next = True
        while True:
            input("Press enter to roll the dice...")
            self.shooter.roll_dice()

            if(self.shooter.current_value() == LOSE):
                print(f"You rolled {self.shooter.current_value()}. You lose.")
                next = False
                return

            if(self.shooter.current_value() == self.point):
                print(f"You rolled {self.point}. You win!")
                next = False
                return
            print(f"You rolled {self.shooter.current_value()}.")
