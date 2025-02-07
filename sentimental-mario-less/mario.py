def main():
    while True:
        try:
            # Solicitar al usuario la altura de la pirámide
            height = int(input("Height: "))
            if 1 <= height <= 8:
                break
            else:
                print("Por favor, ingrese un número entre 1 y 8.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Construir la pirámide
    for i in range(1, height + 1):
        # Imprimir espacios en blanco para alinear a la derecha
        print(" " * (height - i), end="")
        # Imprimir los bloques de la pirámide
        print("#" * i)

if __name__ == "__main__":
    main()
