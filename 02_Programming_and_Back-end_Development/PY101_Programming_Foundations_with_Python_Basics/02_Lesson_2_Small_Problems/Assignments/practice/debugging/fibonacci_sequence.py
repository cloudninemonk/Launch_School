# Original code

def fibonacci_sequence(n):
    sequence = [0, 1]
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    for i in range(2, n):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    
    return sequence

fib_numbers = fibonacci_sequence(8)
print(f"First 7 Fibonacci numbers: {fib_numbers}")

# Updated code