class SudokuGrid:
    def __init__(self, grid:str):
        self.grid = grid

    def __getitem__(self, item:int):
        return self.grid[item]

    def __setitem__(self, item:int, value:str):
        list_grid = list(self.grid)
        list_grid[item] = value
        self.grid = "".join(list_grid)

    def getFirstEmptySquareIndex(self)->int:
        return self.grid.find("0")

    def getAvailableHorizontalDigits(self, index:int)->list[str]:
        horizontal_start = index - index % 9
        return [digit for digit in self[horizontal_start:horizontal_start+9]]

    def getAvailableVerticalDigits(self, index:int)->list[str]:
        vertital_start = index % 9
        return [self[vertital_start + i*9] for i in range(9)]

    def getAvailableSquareDigits(self, index:int)->list[str]:
        square_x_start = index % 9 - index % 3
        square_y_start = index - index % 27
        square_start = square_x_start + square_y_start
        return [self[square_start + i%3 + i//3*9] for i in range(9)]

    def getAvailableDigits(self, index:int)->list[str]:
        # "1" -> "9"
        possible_moves = [chr(49+i) for i in range(9)]

        horizontal_digits = self.getAvailableHorizontalDigits(index)
        vertical_digits = self.getAvailableVerticalDigits(index)
        square_digits = self.getAvailableSquareDigits(index)
        digits = horizontal_digits + vertical_digits + square_digits

        return filter(lambda digit: not digit in digits, possible_moves)

    def solve(self, nb_soluces:int=1)->int:
        index = self.getFirstEmptySquareIndex()
        if index == -1:return nb_soluces - 1

        digits = self.getAvailableDigits(index)
        for digit in digits:
            self[index] = digit
            nb_soluces  = self.solve(nb_soluces)
            if nb_soluces == 0:return 0
            self[index] = "0"
        return nb_soluces
