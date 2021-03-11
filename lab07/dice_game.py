from game_controller import GameController


def rules():
    print("-------------------------")
    print("Welcome to street craps!")
    print("")
    print("Rules:\nIf you roll 7 or 11 on your first roll, you win.\n"
          "If you roll 2,3, or 12 on your first role,you lose.\n"
          "If you roll anything else, that's your 'point and\n"
          "you keep rolling until you either roll your point\n"
          "again (win) or roll a 7 (lose)")


def main():
    gc = GameController()
    rules()
    gc.start_play()


main()
