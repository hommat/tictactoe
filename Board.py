class Board:
  def __init__(self):
    self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  def draw(self):
    print(7 * "-")
    for row in self.grid:
      print("|", end="")
      for col in row:
        char = self.get_char(col)
        print(char, end="|")
      print("\n" + 7 * "-")

  def get_char(self, num):
    if num == 1:
      return "X"
    elif num == -1:
      return "O"
    else:
      return " "

  def has_winner(self):
    # horizontal
    for row in self.grid:
      row_sum = sum(row)
      if abs(row_sum) == 3:
        return True

    # vertical
    for col in range(3):
      col_sum = 0
      for row in self.grid:
        col_sum += row[col]

      if abs(col_sum) == 3:
        return True

    # diagonal
    diag_sum = 0
    for d in range(3):
      diag_sum += self.grid[d][d]
    
    if abs(diag_sum) == 3:
        return True

    # diagonal
    diag_sum = 0
    for d in range(3):
      diag_sum += self.grid[d][2-d]
    
    print(diag_sum)
    if abs(diag_sum) == 3:
        return True

  def make_move(self, is_x_turn):
    are_given_coors_proper = False
    while not are_given_coors_proper:
      x, y = self.get_move_coords()
      are_given_coors_proper = self.is_move_possible(x, y)
      if not are_given_coors_proper:
        print("Wrong coords, please enter again")

    self.grid[y][x] = 1 if is_x_turn else -1

  def get_move_coords(self):
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))

    return x, y

  def is_move_possible(self, x, y):
    if x < 0 or x > 2 or y < 0 or y > 2:
      return False
      
    return self.grid[y][x] == 0