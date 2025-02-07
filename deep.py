def respuesta(x):
    if x == "42":
        print("Yes")
    elif x == ("Forty-Two"):
        print("Yes")
    elif x == ("Forty Two"):
        print("Yes")
    else:
        print("No")


def main():

    # ask the user for the input
    pregunta = input("What is the Anser to the Great Question of Life, the Universe, and Everything? ").title().strip()

    respuesta(pregunta)


main()
