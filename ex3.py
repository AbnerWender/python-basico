from math import sqrt
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)

if raiz_delta < 0:
    print("Delta negativo")
else:
    x1 = (-b + raiz_delta)/2*a
    x2 = (-b + raiz_delta)/2*a

print ("x1 = %d" %x1)
print("x2 = %d" %x2)