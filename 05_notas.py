import sys
try:
    n1 = float(input("Ingrese nota #1: "))
    if n1 >= 0 and n1 <= 100:
        pass
    else:
        sys.exit("Nota no valida.")
    n2 = float(input("Ingrese nota #2: "))
    if n2 >= 0 and n2 <= 100:
        pass
    else:
        sys.exit("Nota no valida.")
    n3 = float(input("Ingrese nota #3: "))
    if n3 >= 0 and n3 <= 100:
        pass
    else:
        sys.exit("Nota no valida.")
except ValueError:
    sys.exit("Nota no valida.")

p = (n1 + n2 + n3)/3   

if p >= 0 and p < 60:
    print(f"Promedio: {p:.2f}\tReprobado")
elif p >= 60 and p < 70:
    print(f"Promedio: {p:.2f}\tSupletorio")
elif p >= 70 and p < 80:
    print(f"Promedio: {p:.2f}\tBueno")
elif p >= 80 and p < 90:
    print(f"Promedio: {p:.2f}\tMuy bueno")
elif p >= 90 and p <= 100:
    print(f"Promedio: {p:.2f}\tExcelente")