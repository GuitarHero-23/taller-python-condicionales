while True:
    try:
        d = float(input("Digite la distancia recorrida en km: "))
        if d < 0:
            print("Distancia no valida.")
        else:
            break
    except ValueError:
        print("Distancia no valida.")

while True:
    try:
        h = int(input("Digite la hora de inicio de su viaje: "))
        if h >= 6 and h < 20:
            t = 0.5
            horario = "Diurno"
            break
        elif h >= 20 and h <= 24:
            t = 0.65
            horario = "Nocturno"
            break
        elif h >= 0 and h < 6:
            t = 0.65
            horario = "Nocturno"
            break
        else:
            print("Hora no valida.")
    except ValueError:
        print("Hora no valida.")

if d > 10:
    r = 2
else:
    r = 0

print(f"Horario: {horario}\nDistancia: {d}km\nTotal a pagar: ${t*d+r}")