# Decide the number of rows
rows = 5

# Outer loop
for i in range(rows + 1):
    # Inner loop
    for j in range(i):
        print(i, end="")
    print("")