import random

from solver import SudokuGrid

def getRandomEmptySquareIndex(sudoku:SudokuGrid)->int:
    empty_squares_number = random.randint(0, sudoku.grid.count("0")-1)
    for i in range(len(sudoku.grid)):
        if sudoku[i] == "0": empty_squares_number -= 1
        if empty_squares_number < 0:return i

    raise Exception("getRandomEmptySquareIndex: sudoku doesn't have any empty square")

def generate_sudoku(sudoku:SudokuGrid):
    index = getRandomEmptySquareIndex(sudoku)
    digits = [digit for digit in sudoku.getAvailableDigits(index)]

    while digits:
        digit = random.choice(digits)
        digits.remove(digit)

        sudoku[index] = digit

        result = sudoku.solve(nb_soluces=2)
        if result == 0:
            result = generate_sudoku(sudoku)
            if result:return result
        elif result == 1:return sudoku
        
        sudoku[index] = "0"
