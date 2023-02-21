a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
D=(b**2)-(4*a*c) # discriminant
print("The value of discriminant is",D)
sol1 = (-b+D**0.5/2*a)
sol2 = (+b-D**0.5/2*a)
print("The roots of this quadraticn equations are",sol1,"and",sol2)