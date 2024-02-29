def print_fibonacci(length):
    if length < 0:
        print("Length should be a non-negative integer")
        return
    elif length == 0:
        fib_sequence = []
    elif length == 1:
        fib_sequence = [0]
    elif length == 2:
        fib_sequence = [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print(fib_sequence)


