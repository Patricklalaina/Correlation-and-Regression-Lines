def _x_on_y(y):
    return round((9 * y + 107) / 20, 1)


def _y_on_x(x):
    return round((4 * x + 33) / 5, 1)

def main():
    print(_x_on_y(7))
    
if __name__=='__main__':
    main()
