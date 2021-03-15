

class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        # TODO: Initialize the bench object with whatever
        # attributes and values it will need
        self.bench = []

    def send_to_bench(self, player_name):
        # TODO: Put the player "onto the bench"
        self.bench.insert(0, player_name)

    def get_from_bench(self):
        # TODO: Return the name of the player who has
        # been on the bench longest.
        if(len(self.bench) == 0):
            print("The bench is empty.")
        else:
            get = self.bench.pop()
            print(f"get {get} from bench")

    # TODO: Write the function that will display the
    # current list of players on the bench
    def show_bench(self):
        if(len(self.bench) == 0):
            print("The bench is empty.")
        else:
            print("The bench currently includes:")
            for p in self.bench:
                print(p)

    # TODO: Write any other methods that might be used
    # by the methods above.
