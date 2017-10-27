from random import randint

def generate_code():
    L =["k","w","g","r","b","y"]
    H = []
    for i in range(4): 
        H.append(L[randint(0,5)])
    return H
c = (generate_code())
score_white = 0
score_red = 0
tally = 0
print("The colors are: White(w) Black(k) Green(g) Red(r) Blue(b) Yellow(y)")
while score_red != 4:
    tally = tally + 1
    score_white=0
    score_red=0
    k = [0,0]
    w = [0,0]
    g = [0,0]
    r = [0,0]
    b = [0,0]
    y = [0,0]
    x=input("enter four colors: ")
    if x == "ans":
        print(c)
    guess=list(x)
    for i in range(4):    
        if c[i] == guess[i]:
            score_red=score_red+1
    for i in c:    
        if i == "k":
            k[0]=k[0]+1
        elif i == "w":
            w[0]=w[0]+1
        elif i == "g":
            g[0]=g[0]+1
        elif i == "r":
            r[0]=r[0]+1
        elif i == "b":
            b[0]=b[0]+1
        elif i == "y":
            y[0]=y[0]+1
    for i in guess:
        if i == "k":
            k[1]=k[1]+1
        elif i == "w":
            w[1]=w[1]+1
        elif i == "g":
            g[1]=g[1]+1
        elif i == "r":
            r[1]=r[1]+1 
        elif i == "b":
            b[1]=b[1]+1
        elif i == "y":
            y[1]=y[1]+1
    
    
    score_white=(min(k)+min(w)+min(g)+min(r)+min(b)+min(y))-score_red
    if score_white<0:
        score_white=0
    print(guess, "white ", score_white, " red ", score_red, "  turn: ",tally )    
    print()
print("it took u ", tally, " turns to win")    
if tally <= 3:
    print("luck only strikes once. congrats")
elif tally == 5:
    print("illuminati confermed    <0> ")
    print("luck only strikes once congrats!")
elif tally <= 7:
    print("eh...")
elif tally == 13:
    print("the devil is watching.")
    print("because...")
    print("you know..")
    print("unlucky number...")
    print("nevermind...")
print("product of bananas and monkeys inc. thank you for playing")
