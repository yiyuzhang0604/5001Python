from player import Player
from bench import Bench


class Team:
    """A class representing a dodgeball team"""
    # All methods in Python include arguments representing the object
    # itself. In the method definition, this is represented by the
    # `self` parameter.
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []
        self.catcher = []
        self.corner = []
        self.sniper = []
        self.thrower = []

    # Another example of self. The method call only passes one argument,
    # the 'name; value. But the method definition must always include the
    # self parameter.

    def set_team_name(self, name):
        # TODO: set the team name
        self.name = name

    def add_position(self, Player):
        if(Player.player_position == 'catcher'):
            self.catcher.append(Player)
        elif(Player.player_position == 'corner'):
            self.corner.append(Player)
        elif(Player.player_position == 'sniper'):
            self.sniper.append(Player)
        elif(Player.player_position == 'thrower'):
            self.thrower.append(Player)

    # Note again that `self` is the first parameter.
    def add_player(self, player_name, player_number, player_position):
        # TODO: call the Player class constructor with the appropriate
        # values to create a new player object, then add that
        # player object to the team's players list.
        new_player = Player(player_name, player_number, player_position)
        self.players.append(new_player)
        print(new_player.player_name)
        self.add_position(new_player)

    def cut_player(self, player_name, the_bench):
        # TODO: Remove the player with the name player_name
        # from the players list.

        # Check if the team is empty:
        if(len(self.players) == 0):
            print("The team is empty, cannot cut player")
            return
        # check: if player is on the bench, can't cut the player
        for i in range(len(the_bench.bench)):
            if(the_bench.bench[i] == player_name):
                print("The player is on the bench, cannot cut the player.")
                return
        # For players that are not on the bench:
        for p in self.players:
            if(p.player_name == player_name):
                if(p.player_position == 'catcher'):
                    self.catcher.remove(p)
                if(p.player_position == 'corner'):
                    self.corner.remove(p)
                if(p.player_position == 'sniper'):
                    self.sniper.remove(p)
                if(p.player_position == 'thrower'):
                    self.thrower.remove(p)
            self.players.remove(p)

    def is_position_filled(self, position):
        # TODO: Write the method that checks whether
        # there is currently at least one player on the team
        # occupying the requested position
        val = getattr(self, position)
        if (len(val) == 0):
            print("No, the", position, "position is not filled")
        else:
            print("Yes, the", position, "posistion is filled")

    # TODO: Write any necessary methods to support the methods
    # above, and write the method that will display (print to screen)
    # the full team roster in the following format:
    #    The lineup for Seattle Scorpions is:
    #    15       Garcia          catcher
    #    55       Wiggins         corner
    #    99       McCann          sniper
    def print_rooster(self):
        if(len(self.players) == 0):
            print(f"The lineup for {self.name} is:")
            print("The team currently has no players")
        else:
            print(f"The lineup for {self.name} is:")
            for i in self.players:
                print(i.player_number.ljust(20) + i.player_name.ljust(20) +
                      i.player_position)
