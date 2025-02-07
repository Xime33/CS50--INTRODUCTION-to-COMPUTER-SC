from cs50 import get_float

def main():

    while True:
        change = get_float("Change owed: ")
        if change >= 0:
            break


    cents = round(change * 100)

    # Calcular la cantidad mínima de monedas
    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents


    total_coins = quarters + dimes + nickels + pennies

   
    print(total_coins)

if __name__ == "__main__":
    main()
