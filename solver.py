class SudokuGrid:
    def __init__(self, grid:str):
        self.grid = grid

    def getFirstEmptySquareIndex(self)->int:
        return self.grid.find("0")

    def getAvailableHorizontalDigits(self, index:int)->list[str]:
        horizontal_start = index - index % 9
        return self.grid[horizontal_start:horizontal_start+9]

    def getAvailableVerticalDigits(self, index:int)->list[str]:
        vertital_start = index % 9
        return [self.grid[vertital_start + i*9] for i in range(9)]

    def getAvailableSquareDigits(self, index:int)->list[str]:
        square_x_start = index - index % 3
        square_y_start = index - index % 27
        square_start = square_x_start + square_y_start
        return [self.grid[square_start + i%3 + i//3*9] for i in range(9)]

    def getAvailableDigits(self, index:int)->list[str]:
        # "1" -> "9"
        possible_moves = [chr(49+i) for i in range(9)]

        horizontal_digits = self.getAvailableHorizontalDigits(index)
        vertical_digits = self.getAvailableVerticalDigits(index)
        square_digits = self.getAvailableSquareDigits(index)
        digits = horizontal_digits + vertical_digits + square_digits

        return filter(lambda digit: not digit in digits, possible_moves)
