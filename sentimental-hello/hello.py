

def get_int(numero):
    while True:
        try:
            altura= int(input("Height: "))
            if altura >= 1 or altura <= 8:
                break

 for i in range(1, height + 1):
        # Imprimir espacios en blanco para alinear a la derecha
        print(" " * (height - i), end="")
        # Imprimir los bloques de la pirámide
        print("#" * i)

