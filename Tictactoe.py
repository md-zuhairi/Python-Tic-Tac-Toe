theboard = {'7':' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '1':' ','2':' ','3':' '}
def printboard(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('- + - + -')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('- + - + -')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])

reset_board_keys = []

for key in theboard:
    reset_board_keys.append(key)

def game():

    turn = 'X'
    count = 1

    for i in range(10):
        printboard(theboard);
        print("Its "+turn+" turn, which place you wanna move to ?");

        move = input()

        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1

        else:
            print("The place is already occupied , where else you wanna move to ?")
            continue

        # Checking for who won the game.
        if count >= 5:

            if theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                printboard(theboard)
                print("\n*** Game Over ***\n")
                print("---- The player "+turn+" wins ----\n")
                break

            elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                printboard(theboard)
                print("\n*** Game Over ***\n")
                print("---- The player "+turn+" wins ----\n")
                break

            elif theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                printboard(theboard)
                print("\n*** Game Over ***\n")
                print("---- The player "+turn+" wins ----\n")
                break

            elif theboard['7'] == theboard['4'] == theboard['1'] != ' ':
                printboard(theboard)
                print("\n*** Game Over ***\n")
                print("---- The player "+turn+" wins ----\n")
                break

            elif theboard['8'] == theboard['5'] == theboard['2'] != ' ':
                printboard(theboard)
                print("\n*** Game Over ***\n")
                print("---- The player "+turn+" wins ----\n")
                break

            elif theboard['9'] == theboard['6'] == theboard['3'] != ' ':
                printboard(theboard)
                print("\n*** Game Over ***\n")
                print("---- The player "+turn+" wins ----\n")
                break

            elif theboard['7'] == theboard['5'] == theboard['3'] != ' ':
                printboard(theboard)
                print("\n*** Game Over ***\n")
                print("---- The player "+turn+" wins ----\n")
                break
            elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                printboard(theboard)
                print("\n*** Game Over ***\n")
                print("---- The player " + turn + " wins ----\n")
                break

        # Condition for if its a tie

        if count == 9:
            print("\n*** Game Over ***\n")
            print("---- It's a tie :) ----")


        # Changing the turn of players

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X';
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in reset_board_keys:
            theboard[key] = " "

        game()


if __name__ == '__main__':
    game()