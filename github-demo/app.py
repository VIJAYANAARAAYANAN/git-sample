def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    # Get user input
    num = int(input("Enter a positive integer: "))
    
    if num < 0:
        print("Factorial does not exist for negative numbers.")
    else:
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
        print("HEllo")
        print("hi new")
if __name__ == '__main__':
    main()

