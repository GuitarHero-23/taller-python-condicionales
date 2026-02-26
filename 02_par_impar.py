n = int(input("Digite un número entero: "))
if n%2 == 1:
    print("Su número es impar")
else:
    print("Su número es par")

e = int(input("Digite su edad: "))
if e >= 18:
    print("Usted es mayor de edad")
elif e < 0:
    print("Edad no valida")
else:
    print("Usted es menor de edad")