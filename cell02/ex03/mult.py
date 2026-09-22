x = input("Enter the first number:\n")
y = input("Enter the second number:\n")
mult = int(x)*int(y)
print(f"{x} x {y} = {mult}")
if mult == 0:
    print("The result is positive and negative.")
elif mult > 0:
    print("The result is positive.")
elif mult < 0:
    print("The result is negative.")