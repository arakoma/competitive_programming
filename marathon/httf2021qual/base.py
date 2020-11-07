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

def main(xy):
    ans = ""
    m = [[-1 for _ in range(20)] for _ in range(20)]
    for i in range(100):
        x, y = xy[i]
        m[x][y] = i
    #query = [[] for _ in range(100)]
    deck = []
    xnow, ynow = 0, 0
    
    for i in range(100):
        x = xy[i][0]
        y = xy[i][1]
        dx = x - xnow
        dy = y - ynow
        if dx < 0:
            ans += "U" * (-dx)
        else:
            ans += "D" * dx
        if dy < 0:
            ans += "L" * (-dy)
        else:
            ans += "R" * dy
        ans += "I"
        xnow, ynow = x, y
    
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