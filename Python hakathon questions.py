def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]  # Starting with the first two terms
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence[:n]

def main():
    try:
        n = int(input("Enter the number of terms for Fibonacci sequence: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        fibonacci_sequence = generate_fibonacci_sequence(n)
        print("Fibonacci Sequence up to term", n, ":", fibonacci_sequence)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()


################## Question 2
def main():
    try:
        age = int(input("Enter your age: "))
        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")

if __name__ == "__main__":
    main()
