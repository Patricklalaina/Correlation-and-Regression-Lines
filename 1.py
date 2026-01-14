# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


def _get_rxy(n, x, y):
    sum_x = sum(i for i in x)
    sum_y = sum(i for i in y)
    sum_xy = sum( i * j for i, j in zip(x, y))
    sum_sqrx = sum(i ** 2 for i in x)
    sum_sqry = sum(i ** 2 for i in y)
    num = n * sum_xy - sum_x * sum_y
    div = ((n * sum_sqrx - (sum_x ** 2)) * (n * sum_sqry - (sum_y ** 2))) ** 0.5
    return round(num / div, 3)


def _get_data():
    return sys.stdin.read().strip().splitlines()


def main():
    data = _get_data()
    # print(0.145)
    x = [15, 12,  8,   8,   7,   7,   7,   6,   5,   3]
    y = [10,  25,  17,  11,  13, 17,  20,  13,  9,   15]
    print(_get_rxy(len(x), x, y))

if __name__=='__main__':
    main()
