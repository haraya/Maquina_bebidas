def maquina_bebidas(nombre, cantidad):
    # stock = 0
    monto = 0
    total = 10
    print(f"Ha seleccionado {nombre}")
    if cantidad <= 0:
        print("Productos agotados")
    else:
        print("Total a pagar: ", 10)
        while monto < 10:
            monedas = int(input("Deposite moneda (acepta $1 $2 $5 $10): "))
            if monedas != 1 and monedas != 2 and monedas != 5 and monedas != 10:
                print("\u001b[31;1mLa moneda es incorrecta, intentelo de nuevo\u001b[0m")
            else:
                monto = monto + monedas
                total -= monedas
                print("Total depositado: $", monto, "\nFalta por pagar: ", total)


            if monto == 10:
                print("\u001b[32;1mHa completado el pago exitosamente\nRecoja su producto\u001b[0m")
        stock = cantidad - 1
        print("Productos en stock", stock)

        monto = 0
    cantidad -= 1
    return cantidad


cocacola = 5
fanta = 5
manzanita = 5
sprite = 5
cocacolalight = 5

bebida = 0


while bebida != 5:
    try:
        print("\nMenu refrescos\n"
              "1.Coca cola\n"
              "2.Fanta\n"
              "3.Manzanita\n"
              "4.Sprite\n"
              "5.Coca cola light\n"
              "6.Salir")
        bebida = int(input("Ingrese una opcion: "))

        if bebida == 1:
            cocacola = maquina_bebidas("Coca Cola", cocacola)

        elif bebida == 2:
            fanta = maquina_bebidas("Fanta", fanta)

        elif bebida == 3:
            manzanita = maquina_bebidas("Manzanita", manzanita)

        elif bebida == 4:
            sprite = maquina_bebidas("Sprite", sprite)

        elif bebida == 5:
            cocacolalight = maquina_bebidas("Coca Cola light", cocacolalight)

        elif bebida == 6:
            print("Saliendo del programa....")
            break

        else:
            print("\u001b[31;1mEl dato infresado es incorrecto, intente de nuevo\n\u001b[0m")
    except:
        print("\u001b[31;1mEl dato infresado es incorrecto, intente de nuevo\n\u001b[0m")