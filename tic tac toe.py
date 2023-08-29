d = [[' ' for _ in range(3)] for _ in range(3)]


def display():
    print('\n    0   1   2\n')
    print('0   {} | {} | {}'.format(d[0][0], d[0][1], d[0][2]))
    print('    ----------')
    print('1   {} | {} | {}'.format(d[1][0], d[1][1], d[1][2]))
    print('    ----------')
    print('2   {} | {} | {}\n'.format(d[2][0], d[2][1], d[2][2]))


def x_game():
    print('\n\tX turn')
    co_ordinates('x')
    display()


def o_game():
    print('\n\tO turn')
    co_ordinates('o')
    display()


def co_ordinates(player):
    c1, c2 = input('Enter the co_ordinates by space: ').split()
    c1 = int(c1)
    c2 = int(c2)
    if 0 <= c1 < 3 or 0 <= c2 < 3:
        if d[c1][c2] == ' ':
            d[c1][c2] = player
    else:
        print('The place is filled.')
        co_ordinates(player)


def winner(player):
    for i in range(3):
        if all([d[i][j] == player for j in range(3)]) or all([d[j][i] == player for j in range(3)]):
            return True
    if all([d[i][i] == player for i in range(3)]) or all([d[i][2 - i] == player for i in range(3)]):
        return True
    return False


if __name__ == '__main__':
    print('\n..........Start Your Game......')
    display()
    play = 0
    while play <= 3:
        x_game()
        if winner('x'):
            print("X is a Winner")
            break
        o_game()
        if winner('o'):
            print("O is a Winner")
            break
        play += 1
    if play == 4:
        print("Game Tied")


