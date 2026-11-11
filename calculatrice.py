import random
import sys
import time


def format_nombre(n):
    return int(n) if n.is_integer() else n

sys.stdout.write("[*] Lancement du module en cours")
sys.stdout.flush()

for _ in range(3):
  time.sleep(0.5)  
  sys.stdout.write(".")
  sys.stdout.flush()

print() 

texte_cible = """
 █▀▀ █▀█ █   █▀▀ █  █ █   █▀█ ▀█▀ █▀█ █ █▀▀ █▀▀
 █   █▀█ █   █   █  █ █   █▀█  █  █▀▄ █ █   █▀▀
 ▀▀▀ ▀ ▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀ ▀  ▀  ▀ ▀ ▀ ▀▀▀ ▀▀▀
"""

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*<>/-=+"

lignes_cibles = texte_cible.strip("\n").split("\n")
lignes_actuelles = [" " * len(l) for l in lignes_cibles]

for _ in range(15):  
  affichage = []
  for i, ligne_cible in enumerate(lignes_cibles):
    nouvelle_ligne = ""
    for j, char_cible in enumerate(ligne_cible):
      if char_cible == " ":
        nouvelle_ligne += " "
      elif random.random() < 0.7:  
        nouvelle_ligne += char_cible
      else:  
        nouvelle_ligne += random.choice(chars)
    affichage.append(nouvelle_ligne)

  sys.stdout.write("\033[H\033[J")  
  print("\n".join(affichage))
  time.sleep(0.06)

print(texte_cible)

lancement = input("\n[+] Voulez-vous lancer la calculatrice ? (oui/non) : ")
if lancement.lower() == "oui":
  sys.stdout.write("[*] Demarrage du module en cours")
  sys.stdout.flush()

  for _ in range(3):
    time.sleep(0.5)  
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.150)

  print("\n") 

  nb_fact = int(input("Combien de facteurs voulez-vous calculer ? : "))

  if nb_fact < 2:
      print("Veuillez mettre au moins 2 facteurs.")
  else:
      nombres = []
      operations = []
      opv = ["+", "-", "*", "/"]

      nbr1 = float(input("Entrez le nombre n°1 : "))
      nombres.append(nbr1)

      for i in range(1, nb_fact):
          op = input(f"Opération après {format_nombre(nombres[-1])} (+, -, *, /) : ")
          while op not in opv:
              print("Opération invalide.")
              op = input("Choisissez une opération : ")
          operations.append(op)

          nbr = float(input(f"Entrez le nombre n°{i + 1} : "))
          nombres.append(nbr)
 
      resultat = nombres[0]
      calcul_text = str(format_nombre(nombres[0]))
      erreur = False

      for i in range(len(operations)):
          op = operations[i]
          nbr = nombres[i + 1]

          calcul_text += f" {op} {format_nombre(nbr)}"

          if op == "+":
              resultat += nbr
          elif op == "-":
              resultat -= nbr
          elif op == "*":
              resultat *= nbr
          elif op == "/":
              if nbr == 0:
                  erreur = True
                  break
              resultat /= nbr

      if erreur:
          print("Erreur : Division par zéro impossible !")
      else:
          print(f" {calcul_text} = {format_nombre(resultat)}")
time.sleep(60)
