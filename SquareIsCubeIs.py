num = int(input("How many numbers do you want squared and cubed?\n"))
def calculate(m):
    print("Number: ",m,"   Square: ",m**2,"   Cube: ",m*m*m)
for a in range(num + 1):
    calculate(a)
