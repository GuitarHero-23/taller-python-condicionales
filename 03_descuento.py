s = float(input("Ingrese el subtotal: $"))
t = input("Ingrese su membresía\nVip\nRegular\n: ").lower()
if t == "vip":
    d = s*0.15
elif t == "regular":
    if s >= 100:
        d = s*0.05
    else:
        d = 0
else:
    print("Respuesta no valida")
    d = 0
    
if s > 0:
    print(f"Subtotal: ${s}\nDescuento aplicado: ${d}\nTotal final: ${s-d}")
else:
    print("Subtotal no valido. Digite un subtotal positivo.")