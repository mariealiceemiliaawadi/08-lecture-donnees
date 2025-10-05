#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            # Retirer le saut de ligne et séparer par ';', puis convertir en int
            l.append([int(x) for x in line.strip().split(';') if x])
    return l

def get_list_k(data, k):
    # Retourne la k-ième liste (indice k)
    if 0 <= k < len(data):
        return data[k]
    else:
        return None

def get_first(l):
    if l:
        return l[0]
    else:
        return None

def get_last(l):
    if l:
        return l[-1]
    else:
        return None

def get_max(l):
    if l:
        return max(l)
    else:
        return None

def get_min(l):
    if l:
        return min(l)
    else:
        return None

def get_sum(l):
    if l:
        return sum(l)
    else:
        return None

#### Fonction principale

def main():
    data = read_data("listes.csv")
    print(f"Nombre de listes lues : {len(data)}")
    for i, l in enumerate(data[:3]):  # Affiche les 3 premières listes
        print(f"Liste {i}: {l}")
        print(f"  Premier: {get_first(l)}")
        print(f"  Dernier: {get_last(l)}")
        print(f"  Max: {get_max(l)}")
        print(f"  Min: {get_min(l)}")
        print(f"  Somme: {get_sum(l)}")
    k = 2
    print(f"\nListe d'indice {k}: {get_list_k(data, k)}")

if __name__ == "__main__":
    main()


