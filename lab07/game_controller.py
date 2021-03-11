from pair_of_dice import PairOfDice


class GameController:
    """ A controller for street craps game """

    def __init__(self):
        self.shooter = PairOfDice()
        self.point = 0

    def start_play(self):
        """ Start the game """
        # First round
        print("Press enter to roll the dice...")
        self.shooter.roll_dice()
        self.point = self.shooter.current_value()

        if(self.point == 7 or self.point == 11):
            print(f"You rolled {self.point}. You win!")
            return

        if(self.point == 2 or self.point == 3 or self.point == 12):
            print(f"You rolled {self.point}. You lose.")
            return

        print(f"Your point is {self.point}.")
        self.shooter.roll_dice()
        # Second round
        next = True
        while True:
            input("Press enter to roll the dice...")
            self.shooter.roll_dice()

            if(self.shooter.current_value() == 7):
                print(f"You rolled {self.shooter.current_value()}. You lose.")
                next = False
                return

            if(self.shooter.current_value() == self.point):
                print(f"You rolled {self.point}. You win!")
                next = False
                return
            print(f"You rolled {self.shooter.current_value()}.")
