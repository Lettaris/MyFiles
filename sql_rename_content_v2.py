import os
import re

def upravit_sql_soubor(soubor, slozka, novy_nazev):
    cesta = os.path.join(slozka, soubor)
    
    try:
        # Pokusíme se otevřít soubor s kódováním utf-8
        with open(cesta, 'r', encoding='utf-8') as file:
            radky = file.readlines()
    except UnicodeDecodeError:
        try:
            # Pokud dojde k chybě, zkusíme otevřít soubor s kódováním utf-16
            with open(cesta, 'r', encoding='utf-16') as file:
                radky = file.readlines()
        except UnicodeDecodeError:
            # Pokud stále ne, zkusíme kódování latin-1
            with open(cesta, 'r', encoding='latin-1') as file:
                radky = file.readlines()

    # Změníme první řádek
    if radky:
        radky[0] = radky[0].replace("USE [ALEF_40_SKOLENI]", "USE [ALEF_40]")
    
    # Regulární výraz pro hledání "SKOLENI Nazev firmy" nebo podobného vzoru
    skolení_pattern = r"SKOLENI\s+[^\$]+"  # Detekuje "SKOLENI" následované jakýmkoliv textem až k symbolu $

    # Odstranění specifikované části textu na konci souboru
    odstraneni_pattern = r"ON \[Data Filegroup 1\]\s*\)\s*ON \[Data Filegroup 1\]\s*GO\s*SET ANSI_PADDING OFF\s*GO\s*$"

    # Změníme řádky, které obsahují CREATE TABLE a CONSTRAINT
    for i in range(len(radky)):
        # Změna v CREATE TABLE (detekujeme vzor "SKOLENI <nějaký název>")
        if radky[i].startswith("CREATE TABLE [dbo].[SKOLENI"):
            radky[i] = re.sub(skolení_pattern, f"{novy_nazev}", radky[i])
        
        # Změna v CONSTRAINT (detekujeme vzor "SKOLENI <nějaký název>")
        if radky[i].startswith(" CONSTRAINT [SKOLENI"):
            radky[i] = re.sub(skolení_pattern, f"{novy_nazev}", radky[i])

    # Odstranění textu na konci souboru
    content = ''.join(radky)
    content = re.sub(odstraneni_pattern, "", content, flags=re.DOTALL)

    # Uložíme změněný obsah zpět do souboru
    with open(cesta, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Soubor {soubor} byl upraven.")

def zpracovat_soubory(slozka, novy_nazev):
    # Zkontrolujeme, zda složka existuje
    if not os.path.exists(slozka):
        print(f"Složka {slozka} neexistuje.")
        return
    
    soubory = [f for f in os.listdir(slozka) if f.endswith(".sql")]
    
    if not soubory:
        print(f"Žádné SQL soubory ve složce {slozka}.")
        return

    # Projdeme všechny soubory ve složce
    for soubor in soubory:
        upravit_sql_soubor(soubor, slozka, novy_nazev)

# Příklad použití
slozka = r'C:\Users\rbartkova\Documents\Profinit\ALEF\Reporty\DB Objects\L0'  # Zadejte správnou cestu ke složce
novy_nazev = 'alef_general'        # Zadejte požadovaný nový název
zpracovat_soubory(slozka, novy_nazev)
