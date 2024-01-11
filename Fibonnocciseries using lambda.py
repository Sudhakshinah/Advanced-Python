def fibonacci(count):

    # Initialize the series

    fib_list = [1, 2]
    list((map(lambda i: fib_list.append(fib_list[i-1]+fib_list[i-2]),
         range(2, count))))
    return fib_list[0:count]


print(fibonacci(50))



