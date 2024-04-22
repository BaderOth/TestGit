def sum_range(x, y):
    if x > y:
        return 0

    total_sum = 0
    for num in range(x, y + 1):
        total_sum += num

    return total_sum


def main():
    x = int(input("Enter the start value (x): "))
    y = int(input("Enter the end value (y): "))

    result = sum_range(x, y)

    print(f"The sum from {x} to {y} is: {result}")


if __name__ == "__main__":
    main()
