rows = int(input("Enter Triangle Alphabets Pattern Rows = "))
print("===Print Triangle Alphabets Pattern ===")

for i in range(0, rows):
    alphabet = 65
    for j in range(rows, i, -1):
        print(end = '')
    for k in range(0, i + 1):
        print('%c' %(alphabet + k), end = '')
    print()