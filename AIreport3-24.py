a, b = 1, 3
for i in range(101):
    fib = [a, b]
    a = fib[1]
    b = fib[0] + fib[1]
    print('{}th fib. number is {}'.format((i + 1),b))
