# Prompt the user to enter the height of the pattern
height = int(input("Enter the height of the pattern: "))

# Print the pattern A
for row in range(height):
    for col in range(height):
        if (
            (row == 0 and col != height // 2) or  # top horizontal line
            (row == height // 2) or  # middle horizontal line
            (col == 0 and row != 0 and row != height // 2) or  # left vertical line
            (col == height - 1 and row != 0 and row != height // 2)  # right vertical line
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print()




