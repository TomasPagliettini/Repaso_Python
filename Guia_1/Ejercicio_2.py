año_actual = int(input("Ingrese el año actual: "))
if (año_actual % 4 == 0 and año_actual %100 != 0):
    print("Este año es bisciesto")
else:
    print("Este año no es bisciesto")