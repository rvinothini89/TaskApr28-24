# Define a lambda function for generating Fibonacci series iteratively
# Generating initial numbers of series using lambda and using the list for further processing
generate_fibonacci = lambda n: [1, 1] + [1]*(n) if n < 2 else [1]*(n)
fibonacci_series = generate_fibonacci(2)
a, b = fibonacci_series
while True:
    a, b = b, a + b
    if b > 50:
        break
    fibonacci_series.append(b)

# Print the Fibonacci series
print(fibonacci_series)