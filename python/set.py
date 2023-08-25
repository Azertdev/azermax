# Créer un ensemble
mon_set = {1, 2, 3, 4}
autre_set = {"a", "b", "c"}
s = set()
# Ajouter un élément à un ensemble
mon_set.add(5)
s.add(5)
s.add(4)
s.add(1)
s.add(9)
s.add(9)
s.add(9)
print(s)

# Supprimer un élément d'un ensemble
mon_set.remove(3)  # Lève une exception si l'élément n'existe pas
mon_set.discard(2)  # Ne lève pas d'exception si l'élément n'existe pas

# Vérifier si un élément est dans un ensemble
if "a" in autre_set:
    print("L'ensemble contient 'a'")

# Parcourir un ensemble avec une boucle
for element in mon_set:
    print(element)

# Opérations ensemblistes
ensemble1 = {1, 2, 3}
ensemble2 = {3, 4, 5}

union = ensemble1 | ensemble2  # Union
intersection = ensemble1 & ensemble2  # Intersection
difference = ensemble1 - ensemble2  # Différence
print(union)
print(intersection)
print(difference)