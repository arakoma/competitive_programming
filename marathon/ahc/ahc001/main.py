def input_all():
    n = int(input())
    xyr = [list(map(int, input().split())) for _ in range(n)]

    return n, xyr


def calc_output(n, xyr):
    output = []

    for i in range(n):
        x = xyr[i][0]
        y = xyr[i][1]
        r = xyr[i][2]
        output.append([x, y, x+1, y+1])

    return output


def output_all(output):
    for c in output:
        print(" ".join(list(map(str, c))))


def main():
    n, xyr = input_all()
    output = calc_output(n, xyr)
    output_all(output)


if __name__ == "__main__":
    main()