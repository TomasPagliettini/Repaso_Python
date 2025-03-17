def corroborar_step(numero):
    numero = int(numero)
    primer_digito = str(abs(numero))[0] 
    digito_anterior = 0
    numero = str(numero)
    for a in numero:
        if (a > primer_digito) or (a < primer_digito):
            digito_anterior = a
            if (digito_anterior > a) or (digito_anterior < a):
                digito_anterior = a
        else: 
            print("NO")
            breakpoint
    


a = input("Ingrese un numero: ")
b = corroborar_step(a)
print(b)
