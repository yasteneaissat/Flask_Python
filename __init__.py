def somme_conditionnelle(n):
    somme = 0
    for i in range(1, n + 1):
        # Si le nombre est divisible par 5 ou 7
        if i % 5 == 0 or i % 7 == 0:
            # Si le nombre est divisible par 11, on passe au nombre suivant
            if i % 11 == 0:
                continue
            # Ajouter le nombre à la somme
            somme += i
        
        # Si la somme dépasse 5000, on arrête immédiatement la boucle
        if somme > 5000:
            break
    
    return somme

# Demander à l'utilisateur de saisir un nombre
n = int(input("Entrez la valeur de n : "))

# Calculer et afficher la somme
resultat = somme_conditionnelle(n)
print(f"La somme finale est : {resultat}")
