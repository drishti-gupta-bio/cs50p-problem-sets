while True:
    height= input("Height: ")
    if height.isdigit():
        height = int(height)
        if 1 <= height <= 8:
            break
    print("Invalid input. Please enter a positive integer between 1 and 8.")
for i in range(1, height + 1):
    print("#" *i)