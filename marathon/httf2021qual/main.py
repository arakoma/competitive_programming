def input_xy():
    xy = [list(map(int, input().split())) for _ in range(100)]
    return xy

def input_xy_file(fname):
    with open(fname + ".txt") as f:
        xy = [list(map(int, s.split())) for s in f.readlines()]
    return xy

def output_ans_file(fname, ans):
    with open(fname + "_ans.txt", mode="w") as f:
        f.write(ans)

def move_to_xy(x, y, xnow, ynow):
    s = ""
    dx = x - xnow
    dy = y - ynow
    if dx < 0:
        s += "U" * (-dx)
    else:
        s += "D" * dx
    if dy < 0:
        s += "L" * (-dy)
    else:
        s += "R" * dy

    return s, x, y

def main(xy):
    ans = ""
    m = [[-1 for _ in range(20)] for _ in range(20)]
    for i in range(100):
        x, y = xy[i]
        m[x][y] = i
    #query = [[] for _ in range(100)]
    deck = []
    xnow, ynow = 0, 0

    # 全部回収
    for i in range(20):
        flag = False
        for j in range(20):
            if flag and j != 19:
                continue
            if m[xnow][ynow] >= 0:
                ans += "I"
                deck.append(m[xnow][ynow])
                m[xnow][ynow] = -1
            
            if 11 <= i < 19 and j == 9:
                flag = True
                continue
            
            if j < 19:
                if i % 2 == 0:
                    ans += "R"
                    ynow += 1
                else:
                    ans += "L"
                    ynow -= 1
        if i < 19:
            ans += "D"
            xnow += 1
    xnow, ynow = 19, 0

    # 全部置く(正方形)
    for i in range(10):
        for j in range(10):
            if m[xnow][ynow] < 0:
                ans += "O"
                c = deck.pop(-1)
                xy[c] = [xnow, ynow]
                m[xnow][ynow] = c
            if j < 9:
                if i % 2 == 0:
                    ans += "R"
                    ynow += 1
                else:
                    ans += "L"
                    ynow -= 1
        ans += "U"
        xnow -= 1
    """
    # 10の位で並べる
    L = [[10+d, 0] for d in range(10)]
    for i in range(100):
        c = deck.pop(-1)
        x, y = L[c//10]
        s, xnow, ynow = move_to_xy(x, y, xnow, ynow)
        ans += s + "O"
        xy[c] = [xnow, ynow]
        L[c//10][1] += 1 
    """

    """
    # 番号順に並べる
    for _ in range(100):
        c = deck.pop()
        x = c // 10 + 10
        y = c % 10
        s, xnow, ynow = move_to_xy(x, y, xnow, ynow)
        ans += s + "O"
        xy[c] = [x, y]
    """
    """
    # だいたい番号順に並べる
    e1 = [10, 0]
    e2 = [15, 0]
    e3 = [10, 5]
    e4 = [15, 5]
    for _ in range(100):
        c = deck.pop()
        if c < 25:
            if e1[1] >= 5:
                e1[1] = 0
                e1[0] += 1
            s, xnow, ynow = move_to_xy(e1[0], e1[1], xnow, ynow)
            ans += s + "O"
            xy[c] = [xnow, ynow]
            e1[1] += 1
        elif 25 <= c < 50:
            if e2[1] >= 5:
                e2[1] = 0
                e2[0] += 1
            s, xnow, ynow = move_to_xy(e2[0], e2[1], xnow, ynow)
            ans += s + "O"
            xy[c] = [xnow, ynow]
            e2[1] += 1
        elif 50 <= c < 75:
            if e3[1] >= 10:
                e3[1] = 5
                e3[0] += 1
            s, xnow, ynow = move_to_xy(e3[0], e3[1], xnow, ynow)
            ans += s + "O"
            xy[c] = [xnow, ynow]
            e3[1] += 1
        elif 75 <= c < 100:
            if e4[1] >= 10:
                e4[1] = 5
                e4[0] += 1
            s, xnow, ynow = move_to_xy(e4[0], e4[1], xnow, ynow)
            ans += s + "O"
            xy[c] = [xnow, ynow]
            e4[1] += 1
    """

    # 回収
    for i in range(100):
        x = xy[i][0]
        y = xy[i][1]
        s, xnow, ynow = move_to_xy(x, y, xnow, ynow)
        ans += s + "I"
        m[x][y] = -1
        xnow, ynow = x, y

        """
        # 一回集める
        if i == 49:
            s, xnow, ynow = move_to_xy(10, 0, xnow, ynow)
            ans += s
            cnt = 0
            for j in range(10, 20):
                for k in range(10):
                    if cnt == 0 and j >= 15:
                        continue
                    if j < 15 and m[xnow][ynow] >= 0:
                        ans += "I"
                        deck.append(m[xnow][ynow])
                        cnt += 1
                    if j >= 15 and m[xnow][ynow] < 0 and cnt > 0:
                        ans += "O"
                        c = deck.pop(-1)
                        xy[c] = [xnow, ynow]
                        m[xnow][ynow] = c 
                        cnt -= 1
                    if k < 9:
                        if j % 2 == 0:
                            ans += "R"
                            ynow += 1
                        else:
                            ans += "L"
                            ynow -= 1
                if j < 19:
                    ans += "D"
                    xnow += 1
        """

    return ans



if __name__ == "__main__":
    flag_file = 1
    file_name = "testCase_0"

    if flag_file:
        xy = input_xy_file(file_name)
        ans = main(xy)
        output_ans_file(file_name, ans)
    else:
        xy = input_xy()
        ans = main(xy)
        print(ans)