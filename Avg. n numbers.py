n = int(input("Enter the total number you want to enter:"))

sum = 0

for i in range(n):
    x = int(input("Enter the number:"))
    sum = sum + x

avg = sum / n

print("Average=", avg)
