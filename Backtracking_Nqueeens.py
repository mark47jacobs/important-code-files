def initialise(board,n):
    for keys in ["queen","row","col","nwtose","swtone"]:
        board[keys] = {}
    for i in range(n):
        board["queen"][i] = -1 
        board["row"][i] = 0
        board["col"][i] = 0
    for i in range(-(n-1),(n-1)):
        board["nwtose"][i] = 0 
    for i in range(2*n-1):
        board["swtone"][i] = 0 

def free(i,j,board):
    return(board["row"][i] == 0 and board["col"][j] == 0 and board["nwtose"][j-1] == 0 and board["swtone"][j+i] == 0 )

def addqueen(i,j,board):
    board["queen"][i] = j 
    board["row"][i] = 1
    board["col"][j] = 1
    board["nwtose"][j-i] = 1
    board["swtone"][j+i] = 1

def undoqueen(i,j,board):
    board["queen"][i] = -1
    board["row"][i] = 0
    board["col"][j] = 0
    board["nwtose"][j-i] = 0
    board["swtone"][j+i] = 0

def printboard(board):
    for row in sorted(board["queen"].keys()):
        print((row,board["queen"][row]))

def placequeen(i,board):
    n = len(board["queen"].keys())
    for j in range(n):
        if free(i,j,board):
            addqueen(i,j,board)
            if i == n-1:
                return(True)
            else:
                extsoln = placequeen(i+1,board)
            if extsoln:
                return(True)
            else:
                undoqueen(i,j,board)
    else:
        return(False)

board = {}
n = int(input("How many queens?  "))

initialise(board,n)
if placequeen(0,board):
    printboard(board)
