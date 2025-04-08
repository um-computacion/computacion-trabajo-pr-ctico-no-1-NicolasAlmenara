def decimal_to_roman(num):
    valores = { 1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
    resultado=""
    for v in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        while num >= v:
            resultado += valores[v]
            num -= v
    return resultado    

def main():
    repeat = "y"
    while repeat=="y":
        decimal = int(input("ingrese un numero decimal"))
        while decimal>3999:
            print("el decimal debe ser menor a 3999")
            decimal = int(input("ingrese un numero decimal"))
        roman = decimal_to_roman(decimal)
        print(f"{decimal} en romano es {roman}")
        repeat = str(input("si desea realizar otra conversion ingrese y (yes), si no, ingrese cualquier letra")).lower()


if __name__ == "__main__":
    main()
