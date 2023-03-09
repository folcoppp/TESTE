def pertence_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

num = int(input("Digite um número: "))

fib = [0, 1]
while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])

if num in fib:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")
