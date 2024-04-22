def subtraction_range(x, y):
    if x > y:
        return 0

    total_subtraction = x
    for num in range(x + 1, y + 1):
        total_subtraction -= num
    
    return total_subtraction

def main():
    x = int(input("Enter the start value (x): "))
    y = int(input("Enter the end value (y): "))

    result = subtraction_range(x, y)

    print(f"The subtraction from {x} to {y} is: {result}")

if __name__ == "__main__":
    main()
