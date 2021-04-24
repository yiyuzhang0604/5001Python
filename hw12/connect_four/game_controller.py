from board import Board
from disk import Disk

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
        self.current_width = [550, 550,550,550,550,550,550]
        self.player1_win = False
        self.player2_win = False

    def update(self):
        """update the game every frame"""
        global pressed
        global coordinates
        global player1
        global d
        global col
        global over
        ZONE = 700

        self.board.draw_me()
        if (not over):
            # if game is not over
            if player1:
                col = 0
            else:
                col = 203
            if(mousePressed):
                if (mouseY < ZONE):
                    # only when mouseY is in this zone, show the disk
                    pressed = True
                    d = self.handle_mouse_press(mouseX, mouseY, col)
            elif (pressed):
                if(mouseY < ZONE):
                    if (d is not None):
                        self.handle_mouse_release(d)
                        if len(coordinates) % 2 == 0:
                            player1 = True
                        else:
                            player1 = False
                pressed = False
                # when mouseY is out of zone, need to reset pressed
        # display the disk after dropping is finished
        for i in range(len(coordinates)):
            co = coordinates[i]
            self.stay(co)
        self.check_over()
        self.board.draw_me()
    
    def check_row_win(self):
        """ check each row if there is a winning situation"""
        for i in range(self.ROW_NUM):
            for j in range(self.COL_NUM):
                try:
                    #print(i)
                    #print(j)
                    if (self.board.grid[i][j] == 1 and self.board.grid[i+1][j] == 1 and
                       self.board.grid[i+2][j] == 1 and self.board.grid[i+3][j] == 1):
                           self.player1_win = True
                    elif (self.board.grid[i][j] == 2 and self.board.grid[i+1][j] == 2 and
                         self.board.grid[i+2][j] == 2 and self.board.grid[i+3][j] == 2):
                           self.player2_win = True
                except IndexError:
                    return
                           
    def check_column_win(self):
        """ check each column if there is a winning situation"""
        for i in range(self.ROW_NUM):
            for j in range(self.COL_NUM):
                try:
                    if (self.board.grid[i][j] == 1 and self.board.grid[i][j+1] == 1 and
                       self.board.grid[i][j+2] == 1 and self.board.grid[i][j+3] == 1):
                           self.player1_win = True
                    elif (self.board.grid[i][j] == 2 and self.board.grid[i][j+1] == 2 and
                         self.board.grid[i][j+2] == 2 and self.board.grid[i][j+3] == 2):
                           self.player2_win = True
                except IndexError:
                    return
    
    def check_diagional_win(self):
        """ check each diagional if there is a winning situation """
        for i in range(self.ROW_NUM):
            for j in range(self.COL_NUM):
                try:
                    if (self.board.grid[i][j] == 1 and self.board.grid[i+1][j-1] == 1 and
                       self.board.grid[i+2][j-2] == 1 and self.board.grid[i+3][j-3] == 1):
                           self.player1_win = True
                    elif (self.board.grid[i][j] == 2 and self.board.grid[i+1][j-1] == 2 and
                         self.board.grid[i+2][j-2] == 2 and self.board.grid[i+3][j-3] == 2):
                           self.player2_win = True
                except IndexError:
                    return
        

        

    def check_over(self):
        """check if the game is over"""
        global over
        self.check_column_win()
        self.check_row_win()
        self.check_diagional_win()
        FILL = (200, 3, 0)
        SIZE = 28
        X = 29
        Y = -20
        fill(*FILL)
        
        if self.player1_win == True:
            textSize(SIZE)
            text("Player1 wins!",X,Y)
            print("Player1 wins!")
            over = True
            
            
        elif self.player2_win == True:
            textSize(SIZE)
            text("Player2 wins!",X,Y)
            print("Player2 wins!")
            over = True
        

    def convert(self, pressed_x):
        """ from x posistion, tell which column the disk is located"""
        X_COORDINATES = [50,150,250,350,450,550,650]
        for i in range(len(X_COORDINATES)):
            if pressed_x == X_COORDINATES[i]:
                return i
            
    def convert_y(self,y):
        """ convert y position to row number in the grid"""
        Y_COORDINATES = [50,150,250,350,450,550]
        for i in range(len(Y_COORDINATES)):
            if y == Y_COORDINATES[i]:
                return i; 

    def handle_mouse_press(self, mouseX, mouseY, col):
        """ handle disk dropping animation"""
        ZONE = 700
        X_COORDINATES = [50,150,250,350,450,550,650]
        disk_x = 50
        if (0 < mouseX and mouseX < 50):
            disk_x = X_COORDINATES[0]
        elif (50 < mouseX and mouseX < 150):
            disk_x = X_COORDINATES[1]
        elif (150< mouseX and mouseX < 250):
            disk_x = X_COORDINATES[2]
        elif (250< mouseX and mouseX < 350):
            disk_x = X_COORDINATES[3]
        elif (350< mouseX and mouseX < 450):
            disk_x = X_COORDINATES[4]
        elif (450< mouseX and mouseX < 550):
            disk_x = X_COORDINATES[5]
        elif (550< mouseX and mouseX < 650):
            disk_x = X_COORDINATES[6]
        

        #limit = self.current_width[0]
        d = Disk(disk_x, -45,col)
        d.draw_me(col, disk_x, -45)
        return d

    def handle_mouse_release(self, d):
        d.y = -45
        ACC = 0.5
        UPDATE = 100
        limit = self.current_width[self.convert(d.x)]
        if (limit > 0):
            while (d.y < limit):
                d.y = d.y + ACC
                d.draw_me(col, d.x, d.y)
            coordinates.append(d)
            self.current_width[self.convert(d.x)] -= UPDATE
        if not over:
            if d.col == 0:
                self.board.grid[self.convert_y(d.y)][self.convert(d.x)] = 1
            else:
                self.board.grid[self.convert_y(d.y)][self.convert(d.x)] = 2
        print(self.board.grid)
        
            

    def stay(self, disk):
        disk.display(disk)
