def sum(a,b,c):
    return a+b+c
def printboard(xstate,zstate,winner=None,win_indices=None):
    def mark_winner(symbol, index):
        if win_indices is not None and index in win_indices:
            return f"\033[91m{symbol}\033[0m"  # Use ANSI escape code for red color
        return symbol

    zero = mark_winner('X' if xstate[0] else ('O' if zstate[0] else 0), 0)
    one = mark_winner('X' if xstate[1] else ('O' if zstate[1] else 1), 1)
    two = mark_winner('X' if xstate[2] else ('O' if zstate[2] else 2), 2)
    three = mark_winner('X' if xstate[3] else ('O' if zstate[3] else 3), 3)
    four = mark_winner('X' if xstate[4] else ('O' if zstate[4] else 4), 4)
    five = mark_winner('X' if xstate[5] else ('O' if zstate[5] else 5), 5)
    six = mark_winner('X' if xstate[6] else ('O' if zstate[6] else 6), 6)
    seven = mark_winner('X' if xstate[7] else ('O' if zstate[7] else 7), 7)
    eight = mark_winner('X' if xstate[8] else ('O' if zstate[8] else 8), 8)

    print(f" {zero} | {one} | {two}  ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight}")

def checksum(xstate,zstate):
     wins=[[0,1,2],[0,3,6],[0,4,5],[1,4,5],[1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
     for win in wins:
         if (sum(xstate[win[0]],xstate[win[1]],xstate[win[2]]) == 3):
             print("X won the game")
             return 1,win
         if (sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3):
             print("O won the match")
             return 0,win
     return -1,None

if __name__=="__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X & 0 for O
    print("welcome to TIC TAC TOE")
    while (True):
        printboard(xstate, zstate)

        if turn == 1:
            print("X's chance")
            value = int(input("where you want to keep X on Board?"))
            xstate[value] = 1
        else:
            print("Y's chance")
            value = int(input("where you want to keep O on Board?"))
            zstate[value] = 1
        # print(sum(xstate[0], xstate[1], xstate[2]))
        result,win_indices=checksum(xstate, zstate)
        if ( result!=-1):
            printboard(xstate, zstate, result, win_indices)
            break
        turn = 1 - turn