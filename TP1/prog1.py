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
try : 
	a = input("Entrez le premier nombre : ")
	b = input("Entrez le second nombre : ")
	a = float(a)
	b = float(b)
	res = f.puissance(a, b)
   
	print(f"Le résultat de {a} élevé à la puissance {b} est : {res}")

except TypeError as e:
    print(f"Erreur :{e}")

except ValueError :
	print ("Only integers are allowed")








