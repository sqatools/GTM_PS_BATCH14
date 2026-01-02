# Fibonacci sequence implementation
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
fibonacci_sequence = fibonacci(10)
print("Fibonacci sequence:", fibonacci_sequence)