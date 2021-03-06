# Name: Yiyu Zhang
# Github: https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-YiyuZhang

from board import Board
from disk import Disk
import random

pressed = False
coordinates = []
player1 = True
d = None
col = None
over = False


class GameController:
    def __init__(self, ROW_NUM, COL_NUM):
        self.ROW_NUM = ROW_NUM
        self.COL_NUM = COL_NUM
        self.board = Board(self.ROW_NUM, self.COL_NUM)
        self.current_width = [550, 550, 550, 550, 550, 550, 550]
        self.player1_win = False
        self.player2_win = False
        self.X_COORDINATES = [50, 150, 250, 350, 450, 550, 650]
        self.Y_COORDINATES = [50, 150, 250, 350, 450, 550]
        self.time = 60
        self.is_player_turn = True
        self.ai_disk = []
        self.players = dict()

    def computer_make_move(self):
        """ computer makes move"""
        if not self.check_over():
            next_x = random.randint(0, self.COL_NUM-1)
            next_y = random.randint(0, self.ROW_NUM-1)

            while self.board.grid[next_y][next_x] is not None:
                next_x = random.randint(0, self.COL_NUM-1)
                next_y = random.randint(0, self.ROW_NUM-1)
            d = Disk(self.X_COORDINATES[next_x], -45, 203)
            d.draw_me(d.col, d.x, -45)
            d.display(d)
            self.handle_mouse_release(d)

        self.is_player_turn = True

    def player_make_move(self):
        global pressed
        global player1
        global d
        global col
        global over
        ZONE = 700
        if not self.check_over():
            if(mousePressed):
                if (mouseY < ZONE):
                    # only when mouseY is in this zone, show the disk
                    pressed = True
                    d = self.handle_mouse_press(mouseX, mouseY, col)

            elif (pressed):
                if(mouseY < ZONE):
                    if (d is not None):
                        self.handle_mouse_release(d)
                        player1 = False
                pressed = False
                self.is_player_turn = False

    def update(self):
        """update the game every frame"""
        global pressed
        global coordinates
        global player1
        global d
        global col
        global over
        ZONE = 700
        DELAY = 60
        RED = 0
        YELLOW = 203

        self.board.draw_me()
        if (not over):
            # if game is not over
            if self.is_player_turn:
                col = RED
                self.player_make_move()

            elif self.is_player_turn is False:

                col = YELLOW
                self.time -= 1
                if(self.time == 0):
                    self.computer_make_move()
                    self.time = DELAY
        else:
            self.message()

        for i in range(len(coordinates)):
            co = coordinates[i]
            self.stay(co)

        for i in range(len(self.ai_disk)):
            co = self.ai_disk[i]
            self.stay(co)
        self.board.draw_me()

    def message(self):
        """ print the result of the game"""
        FILL = (255, 69, 0)
        SIZE = 30
        WEIGHT = 3
        strokeWeight(WEIGHT)
        X = 40
        Y = -45
        fill(*FILL)
        if self.player1_win is True:
            textSize(SIZE)
            s = "You win!"
            text(s, X, Y)
        else:
            textSize(SIZE)
            s = "You lose!"
            text(s, X, Y)

    def check_row_win(self):
        """ check each row if there is a winning situation"""
        for i in range(self.ROW_NUM):
            for j in range(self.COL_NUM):
                try:
                    if (self.board.grid[i][j] == 1 and
                        self.board.grid[i][j+1] == 1 and
                        self.board.grid[i][j+2] == 1 and
                        self.board.grid[i][j+3] == 1):
                        self.player1_win = True
                    elif (self.board.grid[i][j] == 2 and
                            self.board.grid[i][j+1] == 2 and
                            self.board.grid[i][j+2] == 2 and
                            self.board.grid[i][j+3] == 2):
                        self.player2_win = True
                except IndexError:
                    return

    def check_column_win(self):
        """ check each column if there is a winning situation"""
        for i in range(self.ROW_NUM):
            for j in range(self.COL_NUM):
                try:
                    if (self.board.grid[i][j] == 1 and
                        self.board.grid[i+1][j] == 1 and
                        self.board.grid[i+2][j] == 1 and
                        self.board.grid[i+3][j] == 1):
                        self.player1_win = True
                    elif (self.board.grid[i][j] == 2 and
                            self.board.grid[i+1][j] == 2 and
                            self.board.grid[i+2][j] == 2 and
                            self.board.grid[i+3][j] == 2):
                        self.player2_win = True
                except IndexError:
                    return

    def check_diagional_win(self):
        """ check each diagional if there is a winning situation """
        for i in range(self.ROW_NUM):
            for j in range(self.COL_NUM):
                try:
                    if (self.board.grid[i][j] == 1 and
                        self.board.grid[i+1][j-1] == 1 and
                        self.board.grid[i+2][j-2] == 1 and
                        self.board.grid[i+3][j-3] == 1):
                        self.player1_win = True
                    elif (self.board.grid[i][j] == 2 and
                            self.board.grid[i+1][j-1] == 2 and
                            self.board.grid[i+2][j-2] == 2 and
                            self.board.grid[i+3][j-3] == 2):
                        self.player2_win = True
                except IndexError:
                    return

    def check_over(self):
        """check if the game is over"""
        global over
        self.check_column_win()
        self.check_row_win()
        self.check_diagional_win()
        if self.player1_win is True:
            print("Player1 wins!")
            over = True
            self.end_game()
            return True
        elif self.player2_win is True:
            print("Computer wins!")
            over = True
            return True
        return False

    def end_game(self):
        """ handle the end of the game"""
        name = self.get_player_name()
        if name in self.players:
            self.players[name.encode('ascii')] += 1
        else:
            self.players[name.encode('ascii')] = 1
        print(self.players)

    def convert(self, pressed_x):
        """ from x posistion, tell which column the disk is located"""
        for i in range(len(self.X_COORDINATES)):
            if pressed_x == self.X_COORDINATES[i]:
                return i

    def convert_y(self, y):
        """ convert y position to row number in the grid"""
        for i in range(len(self.Y_COORDINATES)):
            if y == self.Y_COORDINATES[i]:
                return i

    def handle_mouse_press(self, mouseX, mouseY, col):
        """ handle disk dropping animation"""
        ZONE = 700
        disk_x = 50
        MIN = 0
        Y = -45
        if (MIN < mouseX and mouseX < self.X_COORDINATES[0]):
            disk_x = self.X_COORDINATES[0]
        elif (self.X_COORDINATES[0] < mouseX and
              mouseX < self.X_COORDINATES[1]):
            disk_x = self.X_COORDINATES[1]
        elif (self.X_COORDINATES[1] < mouseX and
              mouseX < self.X_COORDINATES[2]):
            disk_x = self.X_COORDINATES[2]
        elif (self.X_COORDINATES[2] < mouseX and
              mouseX < self.X_COORDINATES[3]):
            disk_x = self.X_COORDINATES[3]
        elif (self.X_COORDINATES[3] < mouseX and
              mouseX < self.X_COORDINATES[4]):
            disk_x = self.X_COORDINATES[4]
        elif (self.X_COORDINATES[4] < mouseX and
              mouseX < self.X_COORDINATES[5]):
            disk_x = self.X_COORDINATES[5]
        elif (self.X_COORDINATES[5] < mouseX and
              mouseX < self.X_COORDINATES[6]):
            disk_x = self.X_COORDINATES[6]

        d = Disk(disk_x, Y, col)
        d.draw_me(col, disk_x, Y)
        return d

    def handle_mouse_release(self, d):
        """ handle the dropping of disk"""
        d.y = -45
        ACC = 0.5
        UPDATE = 100
        limit = self.current_width[self.convert(d.x)]
        if (limit > 0):
            while (d.y < limit):
                d.y = d.y + ACC
                d.draw_me(col, d.x, d.y)
                done = False
            if d.y == limit:
                done = True
                self.current_width[self.convert(d.x)] -= UPDATE
                if done:
                    self.add_grid(d)

    def add_grid(self, d):
        """ add the disk to the board after dropping"""
        if d.col == 0:
            self.board.grid[self.convert_y(d.y)][self.convert(d.x)] = 1
            coordinates.append(d)

        else:
            self.board.grid[self.convert_y(d.y)][self.convert(d.x)] = 2
            self.ai_disk.append(d)

    def stay(self, disk):
        """ display the disk object"""
        disk.display(disk)

    def setup(self):
        answer = self.input('enter your name')
        if answer:
            print('hi ' + answer)
        elif answer == '':
            print('[empty string]')
        else:
            print(answer)

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def get_player_name(self):
        answer = self.input()
        self.save_name(answer)
        return answer

    def save_name(self, name, file_name="scores.txt"):
        """ save user's name to file"""
        if name is not None and name != "Unknown":
            with open(file_name, "r+")as file:
                read_content = file.read()
                if name in self.players:
                    score = str(self.players[name.encode('ascill')])
                    content = name + " " + score + "\n"
                else:
                    score = str(1)
                    content = name + " " + score + "\n"
                file.seek(0, 0)
                file.write(content)
                file.write(read_content)
