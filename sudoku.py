import os

board = [
    ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*']
]


def printBoard(board):
    separator = '  +-------+-------+-------+'
    print('  0  1  2  3  4  5  6  7  8')
    print(separator)

    for rowIndex, row in enumerate(board):
        print(rowIndex, '|', end=' ')
        for colIndex, cell in enumerate(board[rowIndex]):
            if colIndex == 3 or colIndex == 6:
                print('|', cell, end=' ')
            else:
                print(cell, end=' ')
        print('|')
        if rowIndex == 2 or rowIndex == 5 or rowIndex == 8:
            print(separator)


def stringtoBoard(string):
    if len(string) != 81:
        # invalid string
        return -1

    board = []
    for i in range(1, 10):
        rowString = string[(i - 1) * 9: i * 9]
        row = []

        for char in rowString:
            if char.isnumeric():
                row.append(char)
            elif char == '*':
                row.append(char)
            else:
                # invalid string
                return -1

        board.append(row)
    return board


def fileToBoard(filename):
    with open(filename, 'r') as f:
        return stringtoBoard(f.read())


def boardToString(board):
    boardString = ''
    for rowIndex, row in enumerate(board):
        for colIndex, cell in enumerate(board[rowIndex]):
            boardString += str(cell)
    return boardString


def boardToFile(board, filename):
    string = boardToString(board)
    print('Saving...')
    with open(filename + '.txt', 'w') as f:
        f.write(string)
    return 0


def checkCell(board, inputNum, cell):
    cellX, cellY = cell
    for i in range(9):
        if inputNum == board[cellX][i]:
            return False
        elif inputNum == board[i][cellY]:
            return False
    x0 = (cellX // 3) * 3
    y0 = (cellY // 3) * 3
    for y in range(3):
        for x in range(3):
            if inputNum == board[y0 + y][x0 + x]:
                return False
    return True


def checkBoard(board):
    for rowIndex, row in enumerate(board):
        for colIndex, cell in enumerate(board[rowIndex]):
            boardCopy = board.copy()
            boardCopy[rowIndex][colIndex] = '*'
            if not checkCell(boardCopy, cell, (rowIndex, colIndex)):
                return False
    return True


def delCell(board, cell):
    cellX, cellY = cell
    board[cellY][cellX] = '*'
    return 0


def placeNumber(board, inputNumber, cell):
    cellX, cellY = cell
    board[cellY][cellX] = inputNumber
    return 0


def takeCellInput():
    x = input('x: ')
    y = input('y: ')
    number = input('Tall: ')
    if x.isnumeric() and y.isnumeric() and number.isnumeric():
        x = int(x)
        y = int(y)
        number = int(number)
    else:
        return False
    if 0 < x < 10 and 0 < y < 10 and 0 < number < 10:
        return (x, y), number
    else:
        return False


def takeCellInput2():
    # lame kode men det får gå
    x = input('x: ')
    y = input('y: ')
    if x.isnumeric() and y.isnumeric():
        x = int(x)
        y = int(y)
    else:
        return False
    if 0 < x < 10 and 0 < y < 10:
        return (x, y)
    else:
        return False


def menu():
    global board
    print('1. Ins, for å legge til et tall.')
    print('2. Del, for å fjerne et tall.')
    print('3. Exp, for å eksportere brettet.')
    print('4. Load, for å laste et brett fra fil.')
    print('5. Quit, for å avslutte.')
    userInput = input('Input: ').lower()
    if userInput == 'ins':
        while True:
            while True:
                cell, number = takeCellInput()
                if cell:
                    break
                else:
                    print('Her er det noe som skurrer...')
            if checkCell(board, number, cell):
                placeNumber(board, number, cell)
                return 0
    elif userInput == 'del':
        while True:
            cell = takeCellInput2()
            if cell:
                delCell(board, cell)
                return 0
    elif userInput == 'exp':
        boardToFile(board, input('Filename: '))
        return 0
    elif userInput == 'load':
        filename = input('Filnavn: ')
        try:
            board = fileToBoard(filename)
        except:
            print('Filen eksisterer ikke...')
        return 0
    elif userInput == 'quit':
        exit()
    else:
        return -1


def main():
    while True:
        os.system('cls')
        printBoard(board)
        menu()
        if checkBoard(board):
            print('Du vant, grattis!')
            exit()


main()
