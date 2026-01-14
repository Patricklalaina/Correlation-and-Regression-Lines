# Enter your code here. Read input from STDIN. Print output to STDOUT


def _get_slope_and_cnst(x, y):
    mean_x = sum(i for i in x) / len(x)
    mean_y = sum(i for i in y) / len(y)
    var_x = sum((i - mean_x) ** 2 for i in x)
    cov_xy = sum((i - mean_x) * (j - mean_y) for i, j in zip(x, y))
    b1 = cov_xy / var_x
    b0 = mean_y - b1 * mean_x
    return b0, b1

def main():
    p = [15,12,8, 8, 7, 7, 7, 6, 5, 3]
    h = [10,25,17,11,13,17,20,13,9, 15]
    b0, b1 = _get_slope_and_cnst(p, h)
    h_predict = round(b1 * 10 + b0, 1)
    print(h_predict)
    
if __name__ == '__main__':
    main()
