# Task 1
##fibonacci series generator 

def default_fibonacci(n):
    if n <= 0 :
        return []

    fib_sequence = [0,1]

    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence 

def custom_fibonacci(start_value,num_terms):
    if num_terms <= 0:
        return []
    if num_terms == 1:
        return [start_value]
    
    fib_series = [start_value,start_value+1]

    while len(fib_series) < num_terms:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series

while True:
    print("\nChoose your fibonacci series: ")
    print("\n[1]Default\t\t[2]Custom\t\t[3]Exit")

    ch = input("Enter your choice (1, 2 or 3): ")

    if ch == '1':
        n = int(input("Enter the number of terms: "))
        print(default_fibonacci(n))

    elif ch == '2':
        start_value = int(input("Enter the starting value of series: "))
        num_terms = int(input("Enter the number of terms: "))
        print(custom_fibonacci(start_value,num_terms))

    elif ch == '3':
        print("Thank You!!!")
        break
        


