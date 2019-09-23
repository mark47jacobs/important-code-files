def LCW(u,v):
    LCWdp = []
    for i in range(len(u)+1):
        LCWdp.append([])
        for _ in range(len(v)+1):
            LCWdp[i].append(0)
    
    for r in range(len(u)+1):
        LCWdp[r][len(v)] = 0 # r is for row

    for c in range(len(v)+1):
        LCWdp[len(u)][c] = 0 # c is for row
    
    maxLCW = 0
    for c in range(len(v)-1,-1,-1):
        for r in range(len(u)-1,-1,-1):
            if u[r] == v[c]:
                LCWdp[r][c] = 1 + LCWdp[r+1][c+1]
            else:
                LCWdp[r][c] = 0
            if LCWdp[r][c] > maxLCW:
                maxLCW = LCWdp[r][c]

    return(maxLCW)

def LCS(u,v):

    LCSdp = []
    for i in range(len(u)+1):
        LCSdp.append([])
        for _ in range(len(v)+1):
            LCSdp[i].append(0)

    for r in range(len(u)+1):
        LCSdp[r][len(v)] = 0 # r is for row

    for c in range(len(v)+1):
        LCSdp[len(u)][c] = 0 # c is for row 
    
    for c in range(len(v)-1,-1,-1):
        for r in range(len(u)-1,-1,-1):
            if u[r] == v[c]:
                LCSdp[r][c] = 1 + LCSdp[r+1][c+1]
            else:
                LCSdp[r][c] = max(LCSdp[r+1][c],LCSdp[r][c+1])

    return(LCSdp[0][0])

print("Enter two strings whose longest common subword(LCW) and longest common subsequence(LCS you want o find...")
u = input("Enter first string: ")
v = input("Enter second string: ")
print("length of the longest commomn word is : "+ str(LCW(u,v)))
print("length of the longest common subsequence is : "+ str(LCS(u,v)))


        