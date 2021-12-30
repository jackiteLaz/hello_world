from random import randint


def generate_code():
    color_abv = ["k", "w", "g", "r", "b", "y"]
    cm_code = []
    for i in range(4):
        cm_code.append(color_abv[randint(0, 5)])
    return cm_code


color_dict = {"k": "black",
              "w": "white",
              "g": "green",
              "r": "red",
              "b": "blue",
              "y": "yellow"}
Solution = (generate_code())
score_white = 0
score_red = 0
Round_Num = 0
print("The colors are: White(w) Black(k) Green(g) Red(r) Blue(b) Yellow(y)")
while score_red != 4:
    Round_Num = Round_Num + 1
    score_white = 0
    score_red = 0
    k = [0, 0]
    w = [0, 0]
    g = [0, 0]
    r = [0, 0]
    b = [0, 0]
    y = [0, 0]
    x = input("enter four colors: ")
    if x == "ans":
        print(Solution)
    guess = list(x)
    for i in range(4):
        if Solution[i] == guess[i]:
            score_red = score_red + 1
    for i in Solution:
        if i == "k":
            k[0] += 1
        elif i == "w":
            w[0] += 1
        elif i == "g":
            g[0] += 1
        elif i == "r":
            r[0] += 1
        elif i == "b":
            b[0] += 1
        elif i == "y":
            y[0] += 1
    for i in guess:
        if i == "k":
            k[1] += 1
        elif i == "w":
            w[1] += 1
        elif i == "g":
            g[1] += 1
        elif i == "r":
            r[1] += 1
        elif i == "b":
            b[1] += 1
        elif i == "y":
            y[1] += 1

    score_white = (min(k) + min(w) + min(g) + min(r) + min(b) + min(y)) - score_red
    if score_white < 0:
        score_white = 0
    print(list(map(lambda co: color_dict[co], guess)), "white ", score_white, " red ", score_red, "  turn: ", Round_Num)
    print()
print("it took u ", Round_Num, " turns to win")
if Round_Num <= 3:
    print("luck only strikes once. Congrats!")
elif Round_Num == 5:
    print("Illuminati confirmed    <0> ")
    print("luck only strikes once. congrats!")
elif Round_Num <= 7:
    print("eh...")
elif Round_Num == 13:
    print("The Devil is watching.")
    print("because...")
    print("you know..")
    print("unlucky number...")
    print("never mind...")
print("product of Bananas and Monkeys Inc. Thank you for playing!")
