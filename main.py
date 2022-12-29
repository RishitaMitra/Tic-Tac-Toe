def printboard(xState, yState):
    zero='X' if xState[0] else ('O' if yState[0] else 0)
    one='X' if xState[1] else ('O' if yState[1] else 1)
    two='X' if xState[2] else ('O' if yState[2] else 2)
    three='X' if xState[3] else ('O' if yState[3] else 3)
    four='X' if xState[4] else ('O' if yState[4] else 4)
    five='X' if xState[5] else ('O' if yState[5] else 5)
    six='X' if xState[6] else ('O' if yState[6] else 6)
    seven='X' if xState[7] else ('O' if yState[7] else 7)
    eight='X' if xState[8] else ('O' if yState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--| --| --")
    print(f"{three} | {four} | {five} ")
    print(f"--| --| --")
    print(f"{six} | {seven} | {eight} ")
    pass

def checkwin(xState, yState):
    xwins=[[0,1,2] ,[3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in xwins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]])==3):
            print("X won the match")
            return 1
        if(sum(yState[win[0]], yState[win[1]], yState[win[2]])==3):
            print("O won the match")
            return 0
    return -1

def sum(a, b, c):
    return a+b+c

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 #1 for x and 0 for 0
    print("welcome to tic-tac-toe")
    while(True):
        printboard(xState, yState)
        if(turn == 1):
            print("X's chance")
            value = int(input("please enter a value:"))  # enter values from 0 to 8 for the positions you want
            xState[value]=1
        else:
            print("0's chance")
            value = int(input("please enter a value:"))  # enter values from 0 to 8 for the positions you want
            yState[value]=1
        cwin=checkwin(xState,yState)
        if(cwin!=-1):

            break
        turn=1-turn
