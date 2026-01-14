# Enter your code here. Read input from STDIN. Print output to STDOUT
# y on x -> y = cov(x, y) / Vx (x) + cte
# x on y -> x = cov(x, y) / vy (y) + cte

# Vx = stdx ** 2 = 9

# y = (4 / 5) x + 33 / 5
# cov(x, y) = (0.8) * 9 = 7.2
# x = (9 / 20) y + 107 / 20
# cov(x, y) / Vy = (9 / 20)
# 7.2 /  Vy = 9 / 20
# Vy / 7.2 = 20 / 9 -> Vy = 20 * 7.2 / 9 = 16

print(16.0)
