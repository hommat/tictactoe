from Board import Board

is_game_over = False
is_x_turn = True
board = Board()
board.draw()

while not is_game_over:
  print("Player " + ("X" if is_x_turn else "O") + " turn")
  board.make_move(is_x_turn)
  board.draw()
  if(board.has_winner()):
    print("Player " + ("X" if is_x_turn else "O") + " is the winner!")
    is_game_over = True
  is_x_turn = not is_x_turn
