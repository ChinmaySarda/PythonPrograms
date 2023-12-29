number = int(input("How many numbers do you want in your series? "))
x = 1
y = 2
print(x)
print(y)
for n in range(number-2):
    z = x + y
    x = y
    y = z
    print(z)
