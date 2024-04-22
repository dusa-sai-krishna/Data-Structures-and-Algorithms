
from tkinter import Frame, Label, CENTER
import logics
import constants as c


class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)

        self.commands = {c.UP_KEY:logics.move_up,
                         c.DOWN_KEY: logics.move_down,
                         c.LEFT_KEY: logics.move_left, 
                         c.RIGHT_KEY: logics.move_right,
                         }
        
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()
    
    def init_grid(self):
        background = Frame(self, bg=c.GAME_COLOR,
                           width=c.EDGE_LENGTH, height=c.EDGE_LENGTH)
        background.grid()

        for row in range(c.CELL_COUNT):
            grid_row = []
            for col in range(c.CELL_COUNT):
                cell = Frame(background, bg=c.EMPTY_COLOR,
                             width=c.EDGE_LENGTH / c.CELL_COUNT,
                             height=c.EDGE_LENGTH / c.CELL_COUNT)
                cell.grid(row=row, column=col, padx=c.CELL_PAD,
                          pady=c.CELL_PAD)
                t = Label(master=cell, text="",
                          bg=c.EMPTY_COLOR,
                          justify=CENTER, font=c.LABEL_FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)
    
    def init_matrix(self):
        self.matrix=logics.start_game()
        logics.add_new_2(self.matrix)
        logics.add_new_2(self.matrix)
        
    def update_grid_cells(self):
        for row in range(c.CELL_COUNT):
            for col in range(c.CELL_COUNT):
                new_number=self.matrix[row][col]
                if new_number==0:
                    self.grid_cells[row][col].configure(
                        text="", bg=c.EMPTY_COLOR
                    )
                else:
                    self.grid_cells[row][col].configure(
                        text=str(new_number),bg=c.TILE_COLORS[new_number],
                        fg=c.LABEL_COLORS[new_number]
                    )
        self.update_idletasks()
        
        
    def key_down(self,event):
        key=repr(event.char)
        if key in self.commands:
            self.matrix,changed=self.commands[repr(event.char)](self.matrix)
            if changed:
                logics.add_new_2(self.matrix)
                self.update_grid_cells()
                changed=False
                if logics.get_current_state(self.matrix)=='WON':
                    self.grid_cells[1][1].configure(
                        text='You',bg=c.EMPTY_COLOR
                    )
                    self.grid_cells[1][2].configure(
                        text='WIN!!!',bg=c.EMPTY_COLOR
                    )
                if logics.get_current_state(self.matrix)=='LOST':
                    self.grid_cells[1][1].configure(
                        text='You',bg=c.EMPTY_COLOR
                    )
                    self.grid_cells[1][2].configure(
                        text='LOSE!!!',bg=c.EMPTY_COLOR
                    )

gameGrid=Game2048()     