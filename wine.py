def pour_wine(rows, wine_quantity):
    pyramid = [[0] * (i + 1) for i in range(rows)]

    pyramid[0][0] = wine_quantity

    for i in range(rows):
        for j in range(len(pyramid[i])):
            if pyramid[i][j] > 1:
                overflow = pyramid[i][j] - 1
                pyramid[i][j] = 1

                if i + 1 < rows:
                    pyramid[i + 1][j] += overflow / 2
                    pyramid[i + 1][j + 1] += overflow / 2

    return pyramid

def print_pyramid(pyramid):
    for i in range(len(pyramid)):
        row = pyramid[i]
        row_str = ' '.join(f"{x:.2f}" for x in row)
        print(' ' * (len(pyramid) - i - 1) + row_str)

def main():
    rows = int(input("Enter the number of rows: "))
    wine_quantity = float(input("Enter the quantity of wine: "))
    bottle_row = int(input("Enter the row number to check the wine quantity: "))
    bottle_number = int(input("Enter the bottle number to check the wine quantity: "))

    if bottle_row > rows or bottle_number > bottle_row:
        print("Invalid bottle position")
        return

    pyramid = pour_wine(rows, wine_quantity)
    print("Pyramid shape and wine quantities:")
    print_pyramid(pyramid)

    print(f"\nThe wine quantity in row {bottle_row}, bottle {bottle_number} is {pyramid[bottle_row-1][bottle_number-1]:.2f} liters.")

if __name__ == "__main__":
    main()
