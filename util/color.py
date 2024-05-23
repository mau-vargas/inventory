from colorama import Fore, Back, Style, init

# Inicializar colorama
init(autoreset=True)

RED = Fore.RED
GREEN = Fore.GREEN

print(RED + "Este texto es rojo")
print(GREEN + "Este texto es verde")
print(Back.YELLOW + "Este texto tiene un fondo amarillo")
print(Style.BRIGHT + "Este texto es brillante")
print(Fore.BLUE + Back.WHITE + "Texto azul con fondo blanco")
print("Este texto vuelve a ser normal")

if __name__ == "__main__":
    pass
