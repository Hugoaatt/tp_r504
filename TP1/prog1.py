print("Hello word !")

while True:
    try:
        nombre = int(input("Entrez un nombre : "))
        carre = nombre ** 2
        print(f"Le carré de {nombre} est {carre}.")
    
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        
    except KeyboardInterrupt:
        print("\nFin du programme.")
        break


import fonctions as f

a = float(input("Entrez la base (a) : "))
b = float(input("Entrez l'exposant (b) : "))

res = f.puissance(a, b)
print(f"{a} à la puissance {b} est {res}.")

