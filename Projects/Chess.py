import tkinter as tk
from tkinter import messagebox

BOARD_SIZE = 8

pieces =   {
    "K": "♔", "Q": "♕", "R": "♖", "B": "♗", "N": "♘", "P": "♙",
    "k": "♚", "q": "♛", "r": "♜", "b": "♝", "n": "♞", "p": "♟"
            }

initial_board = [
                    ["r" , "n" , "b" , "q" , "k" , "b" , "n" , "r" ],
                    ["p" , "p" , "p" , "p" , "p" , "p" , "p" , "p" ],
                    ["" , "" , "" , "" , "" , "" , "" , "" ],
                    ["" , "" , "" , "" , "" , "" , "" , "" ],
                    ["" , "" , "" , "" , "" , "" , "" , "" ],
                    ["" , "" , "" , "" , "" , "" , "" , "" ],
                    ["P" , "P" , "P" , "P" , "P" , "P" , "P" , "P" ],
                    ["R" , "N" , "B" , "Q" , "K" , "B" , "N" , "R" ],
                ]

class ChessApp:

    def __init__(self, root):
        self.root = root
        self.root.title("CHESS GAME")
        self.board = [row[:] for row in initial_board]
        self.selected_piece = None
        self.current_turn = "white"
        self.history = []
        self.square_colors = {}

        self.king_moved = {"white": False, "black": False}
        self.rook_moved =  {
            "white" : {"left":False, "right":False},
            "black" : {"left":False, "right":False}
                            }
        self.create_board()


    def create_board(self):
        self.buttons = []
        for row in range(BOARD_SIZE):
            row_buttons = []
            for col in range(BOARD_SIZE):
                if (row + col) % 2 == 0:
                    color = "#DFEDE2"
                else:
                    color = "#3F87D5"

                self.square_colors[(row , col)] = color

                btn  =  tk.Button(self.root, text = pieces.get(self.board[row][col], ""),font = ("Segoe UI Symbol",28) , width = 2, height = 1, bg = color,relief = "flat" , command = lambda r = row, c = col : self.on_click(r,c))
                btn.grid(row = row , column = col)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        undo_btn = tk.Button(self.root, text = "Undo", font=("Arial",14),command = self.undo_move)
        undo_btn.grid(row = BOARD_SIZE, column = 0, columnspan=BOARD_SIZE, sticky="we")

    def on_click(self, row, col):
        if self.selected_piece:
            sr, sc = self.selected_piece
            self.buttons[sr][sc].config(relief = "raised")
            if self.is_valid_move(sr, sc, row, col):
                
                saved_src = self.board[sr][sc]
                saved_dst = self.board[row][col]

                self.history.append([r[:] for r in self.board])

                self.board[row][col] = saved_src
                self.board[sr][sc] = ""

                if self.is_in_check(self.current_turn):
                    self.board = self.history.pop()
                    self.update_board()
                    self.selected_piece = None
                    return
                    
                if saved_src.lower() == "k" and abs(col - sc) == 2:
                    if col > sc:
                        self.board[row][5] = self.board[row][7]
                        self.board[row][7] = ""
                    else:
                        self.board[row][3] = self.board[row][0]
                        self.board[row][0] = ""

                if saved_src.lower() == "k":
                    self.king_moved[self.current_turn] = True
                if saved_src.lower() == "r":
                    if sc == 0:
                        self.rook_moved[self.current_turn]["left"] = True
                    elif sc ==7:
                        self.rook_moved[self.current_turn]["right"] = True

                self.switch_turn()
                self.update_board()

                if self.is_checkmate():
                    messagebox.showinfo("Game Over",f"{'Black' if self.current_turn == 'white' else 'White'} wins by checkmate!")
                    self.root.quit()

                

            self.selected_piece = None

        elif self.board[row][col] != "" and self.is_correct_turn(row,col):
            self.reset_highlights()
            self.selected_piece = (row,col)
            self.buttons[row][col].config(bg="#FFD700")
            self.highlight_moves(row,col)

    def reset_highlights(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                self.buttons[row][col].config(bg=self.square_colors[(row , col)])

    def move_piece(self, src_row, src_col,dest_row, dest_col):
        self.board[dest_row][dest_col] = self.board[src_row][src_col]
        self.board[src_row][src_col] = ""
        self.update_board()
        if self.is_checkmate():
            messagebox.showinfo("Game Over",f"{self.current_turn.capitalize()} wins by checkmate!")
            self.root.quit()

    def highlight_check(self):
        if self.is_in_check(self.current_turn):
            king_pos = self.find_king(self.current_turn)
            if king_pos:
                r,c = king_pos
                self.buttons[r][c].config(bg = "#FB0404")

    def highlight_moves(self,row,col):
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if self.is_valid_move(row,col,r,c):
                    saved_src = self.board[row][col]
                    saved_dst = self.board[r][c]

                    self.board[r][c] = saved_src
                    self.board[row][col] = ""

                    safe = not self.is_in_check(self.current_turn)

                    self.board[row][col] = saved_src
                    self.board[r][c] = saved_dst

                    if safe:
                        if saved_dst != "":
                            self.buttons[r][c].config(bg="#FFB6C1")
                        else:
                            self.buttons[r][c].config(bg="#90EE90")

    def update_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                self.buttons[row][col]["text"]=pieces.get(self.board[row][col],"")
        self.reset_highlights()
        self.highlight_check()

    def switch_turn(self):
        self.current_turn = "black" if self.current_turn == "white" else "white"

    def undo_move(self):
        if not self.history:
            return
        
        self.board = self.history.pop()
        self.current_turn ="black" if self.current_turn == "white" else "white"
        self.update_board()

    def find_king(self, color):
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                piece = self.board[r][c]
                if piece == ("K" if color == "white" else "k"):
                    return r, c
        return None
    
    def is_in_check(self, color):
        king_pos = self.find_king(color)
        if not king_pos:
            return False

        kr, kc = king_pos
        opponent = "black" if color == "white" else "white"

        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                piece = self.board[r][c]
                if piece != "" and (
                    (piece.isupper() and opponent == "white") or
                    (piece.islower() and opponent == "black")
                ):
                    if self.is_valid_move(r, c, kr, kc):
                        return True
        return False



    def is_correct_turn(self,row,col):
        pieces = self.board[row][col]
        return (pieces.isupper() and self.current_turn == "white") or (pieces.islower() and self.current_turn == "black")

    def is_valid_move(self, src_row, src_col,dest_row, dest_col):
        pieces = self.board[src_row][src_col]
        target = self.board[dest_row][dest_col]

        if target != "" and (pieces.isupper() == target.isupper()):
            return False
        
        dr = dest_row - src_row
        dc = dest_col - src_col
        #pawn
        if pieces.lower() == "p":
            direction = -1 if pieces.isupper() else 1
            start_row = 6 if pieces.isupper() else 1

            if dc == 0 and dr == direction and target == "":
                return True
            
            if(dc == 0 and src_row == start_row and dr == 2*direction and target == "" and self.board[src_row + direction][src_col]==""):
                return True
            
            if abs(dc) == 1 and dr == direction and target != "":
                return True
            
            return False
        #rook
        if pieces.lower() == "r":
            if dr != 0 and dc != 0:
                return False
            
            step_r = 0 if dr == 0 else dr // abs(dr)
            step_c = 0 if dc == 0 else dc // abs(dc)
                        
            r , c = src_row + step_r, src_col + step_c
            while (r,c) != (dest_row,dest_col):
                if self.board[r][c]!= "":
                    return False
                r += step_r
                c += step_c
            return True
        #bishop
        if pieces.lower() == "b":
            if abs(dr) != abs(dc):
                return False
            step_r = dr // abs(dr)
            step_c = dc // abs(dc)

            r,c = src_row + step_r, src_col + step_c
            while(r,c) != (dest_row,dest_col):
                if self.board[r][c] != "":
                    return False
                r += step_r
                c += step_c
            return True
        #knight
        if pieces.lower() == "n":
            if (abs(dr), abs(dc)) in [(2, 1), (1, 2)]:
                return True
            return False
        #queen
        if pieces.lower() == "q":
            if abs(dr) == abs(dc):
                step_r = dr // abs(dr)
                step_c = dc // abs(dc)
            elif dr == 0 or dc == 0:
                step_r = 0 if dr == 0 else dr // abs(dr)
                step_c = 0 if dc == 0 else dc // abs(dc)
            else :
                return False
            
            r,c = src_row + step_r, src_col + step_c
            while (r,c) != (dest_row,dest_col):
                if self.board[r][c] != "":
                    return False
                r += step_r
                c += step_c
            return True
        
        #king
        if pieces.lower() == "k":

            # normal king move
            if abs(dr) <= 1 and abs(dc) <= 1:
                return True

            # castling
            if dr == 0 and abs(dc) == 2:
                row = src_row

                # king-side castling
                if dc == 2:
                    if self.board[row][5] == "" and self.board[row][6] == "" and self.board[row][7].lower() == "r":
                        return True

                # queen-side castling
                if dc == -2:
                    if self.board[row][1] == "" and self.board[row][2] == "" and self.board[row][3] == "" and self.board[row][0].lower() == "r":
                        return True

            return False

    
    def is_checkmate(self):
        if not self.is_in_check(self.current_turn):
            return False
        for sr in range(BOARD_SIZE):
            for sc in range(BOARD_SIZE):
                piece = self.board[sr][sc]
                if piece == "":
                    continue
                if (piece.isupper() and self.current_turn == "white") or \
                    (piece.islower() and self.current_turn == "black"):

                    for dr in range(BOARD_SIZE):
                        for dc in range(BOARD_SIZE):
                            if self.is_valid_move(sr,sc,dr,dc):
                                saved_src = self.board[sr][sc]
                                saved_dst = self.board[dr][dc]

                                self.board[dr][dc] = saved_src
                                self.board[sr][sc] = ""
                                safe = not self.is_in_check(self.current_turn)
                                self.board[sr][sc] = saved_src
                                self.board[dr][dc] = saved_dst
                                if safe:
                                    return False
        return True



if __name__ == "__main__":
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()