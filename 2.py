# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def _get_input():
    return sys.stdin.read().strip().splitlines()


def _process(x, y):
    mean_x = sum(i for i in x) / len(x)
    mean_y = sum(i for i in y) / len(y)
    var_x = sum((i - mean_x) ** 2 for i in x)
    cov_xy = sum((i - mean_x) * (j - mean_y) for i, j in zip(x, y))
    m = cov_xy / var_x
    return round(m, 3)

def main():
    # _input = _get_input()
    # data = [elem.split() for elem in _input]
    # p = [float(i) for i in data[0] if i.isdigit()]
    # h = [float(i) for i in data[1] if i.isdigit()]
    p = [15,12,8, 8, 7, 7, 7, 6, 5, 3]
    h = [10,25,17,11,13,17,20,13,9, 15]
    print(_process(p, h))
    
if __name__ == '__main__':
    main()
