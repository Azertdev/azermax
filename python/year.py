def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def get_days_in_month(year, month):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def main():
    year = int(input("Entrez une année : "))
    month = int(input("Entrez un mois (1 à 12) : "))
    
    if 1 <= month <= 12:
        days = get_days_in_month(year, month)
        print(f"Le mois {month} de l'année {year} a {days} jours.")
    else:
        print("Mois invalide. Veuillez entrer un mois entre 1 et 12.")

if __name__ == "__main__":
    main()
