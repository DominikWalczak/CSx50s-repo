x = input("Expression: ")
xL = x.split()
a = int(xL[0])
b = int(xL[2])
c = 0
match xL[1]:
    case "+":
        c = a + b
    case "-":
        c = a - b
    case "*":
        c = a * b
    case "/":
        c = a / b

print(f"{c:.1f}")
