print("███╗░░██╗██╗░██████╗░██╗░░██╗████████╗        ░██████╗███████╗░█████╗░ ")
print("████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝        ██╔════╝██╔════╝██╔══██╗ ")
print("██╔██╗██║██║██║░░██╗░███████║░░░██║░░░        ╚█████╗░█████╗░░██║░░╚═╝ ")
print("██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░        ░╚═══██╗██╔══╝░░██║░░██╗ ")
print("██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░        ██████╔╝███████╗╚█████╔╝ ")
print("╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░        ╚═════╝░╚══════╝░╚════╝░ ")
#======================================================================
#	Code by:	Baselifter		Date:   06.04.2024
#	Version: 	1.0				Mail:	project.northstorm@gmail.com
#----------------------------------------------------------------------
#	License: DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# 				  Copyright (C) 2004 Sam Hocevar
#  			  14 rue de Plaisance, 75014 Paris, France
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# 					  as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  				0. You just DO WHAT THE FUCK YOU WANT TO.
#----------------------------------------------------------------------

import random

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def shuffle_numbers():
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    return numbers

def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None

def is_valid_move(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    row, col = find_empty_location(board)

    if row is None:
        return True

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def generate_sudoku():
    # Leeres Sudoku-Brett erstellen
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Zufällige Reihenfolge der Zahlen für das gesamte Brett
    numbers = shuffle_numbers()

    for i in range(9):
        for j in range(9):
            board[i][j] = numbers[(i * 3 + i // 3 + j) % 9]

    # Sudoku lösen, um ein vollständiges Rätsel zu erhalten
    solve_sudoku(board)

    # Einige Zahlen entfernen, um das Rätsel zu generieren
    remove_count = random.randint(40, 50)
    for _ in range(remove_count):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        board[row][col] = 0

    return board

def check_solution(board):
    for i in range(9):
        for j in range(9):
            if not is_valid_move(board, i, j, board[i][j]):
                return False
    return True

def play_sudoku():
    print("Willkommen zum Sudoku-Spiel!")
    print("Bewege dich durch das Sudoku-Brett mit den Koordinaten (Zeile, Spalte) von 1 bis 9.")
    print("Gib eine Zahl von 1 bis 9 ein, um das Rätsel zu vervollständigen.")
    print("Gib '0' ein, um eine Zelle zu löschen.")
    print("Gib 'n' ein, um ein neues Spiel zu generieren.")
    print("Gib 'q' ein, um das Spiel zu beenden.")

    board = generate_sudoku()

    while True:
        print_board(board)
        print("\n")

        user_input = input("Gib deine Auswahl ein (Zeile Spalte Zahl): ")

        if user_input.lower() == 'q':
            print("Auf Wiedersehen!")
            break
        elif user_input.lower() == 'n':
            board = generate_sudoku()
            print("Ein neues Sudoku-Spiel wurde generiert!")
            continue

        try:
            row, col, num = map(int, user_input.split())
            if 1 <= row <= 9 and 1 <= col <= 9 and 0 <= num <= 9:
                if board[row-1][col-1] == 0 or num == 0:
                    if is_valid_move(board, row-1, col-1, num):
                        board[row-1][col-1] = num
                    else:
                        print("Ungültiger Zug! Bitte überprüfe deine Eingabe.")
                else:
                    print("Diese Zelle ist bereits gefüllt! Bitte wähle eine andere Zelle.")
            else:
                print("Ungültige Eingabe! Bitte gib Zeile, Spalte und Zahl im Bereich von 1 bis 9 ein.")
        except ValueError:
            print("Ungültige Eingabe! Bitte gib Zeile, Spalte und Zahl im Format 'Zeile Spalte Zahl' ein.")

        if check_solution(board):
            print("Herzlichen Glückwunsch! Du hast das Sudoku gelöst!")
            print("Möchtest du ein neues Spiel generieren? (Ja/Nein)")
            user_choice = input().lower()
            if user_choice.startswith('j'):
                board = generate_sudoku()

# Spiel starten
play_sudoku()
