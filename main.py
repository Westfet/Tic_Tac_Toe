board = [i for i in range(1, 10)]
win_comb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9),
            (1, 5, 9), (3, 5, 7)]


def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|',
              board[2 + i * 3], '|')
    print('-------------')


def take_input(player_choosing):
    while True:
        value = input("Выберите номер клетки, куда поставить " +
                      player_choosing + '?')
        if not value.isdigit():
            print('Введите число:')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Эта клетка уже занята, повторите ввод:')
            continue
        board[value - 1] = player_choosing
        break


def check_win():
    for each in win_comb:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return True
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, "выиграл!")
                break
        counter += 1
        if counter > 8:
            draw_board()
            print("Ничья!")
            break


main()
