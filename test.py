def product_range(x, y):
    if x > y:
        return 1

    total_product = 1
    for num in range(x, y + 1):
        total_product *= num
    
    return total_product

def main():
    x = int(input("Enter the start value (x): "))
    y = int(input("Enter the end value (y): "))

    result = product_range(x, y)

    print(f"The product from {x} to {y} is: {result}")

if __name__ == "__main__":
    main()
