import os

def prejdeme_soubory(slozka, novy_nazev):
    # Projdeme všechny soubory ve složce
    for soubor in os.listdir(slozka):
        # Zkontrolujeme, zda soubor odpovídá požadovanému formátu
        if soubor.startswith("dbo.SKOLENI") and soubor.endswith(".sql"):
            # Získáme část za posledním $ (Nazev tabulky) a odstraníme ".Table"
            cast_nazev_tab = soubor.split('$')[-1].replace(".Table", "")
            
            # Vytvoříme nový název souboru bez přípony .sql, protože ji soubory již mají
            novy_soubor = f"{novy_nazev}${cast_nazev_tab}"
            
            # Určujeme celé cesty k souborům
            puvodni_cesta = os.path.join(slozka, soubor)
            nova_cesta = os.path.join(slozka, novy_soubor)
            
            # Přejmenujeme soubor
            os.rename(puvodni_cesta, nova_cesta)
            print(f"Soubor {soubor} byl přejmenován na {novy_soubor}")

# Příklad použití
slozka = r'C:\Users\rbartkova\Documents\Profinit\ALEF\Reporty\DB Objects\L0'  # Zadejte správnou cestu ke složce
novy_nazev = 'alef_general'    # Zadejte požadovaný nový název
prejdeme_soubory(slozka, novy_nazev)
