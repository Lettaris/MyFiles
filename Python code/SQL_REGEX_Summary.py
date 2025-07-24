import os
import re

# Funkce pro extrahování tabulek ze SQL skriptu s číslem řádku a detekcí OUTER APPLY a UNION ALL
def extract_tables_from_sql(sql_script):
    # Regulární výraz pro hledání tabulek ve formátu:
    # [CZ-DB].NazevDBschema.dbo.[SpecifikaceNazvuTabulky$NazevTabulky]
    pattern = r'(\bfrom\b|\bjoin\b|\bleft join\b|\bright join\b|\binner join\b|\bouter apply\b)\s+\[([a-zA-Z0-9_-]+)\]\.([a-zA-Z0-9_-]+)\.dbo\.\[([^\]]+?)\]'
    
    # Používáme findall pro extrakci všech tabulek
    matches = []
    lines = sql_script.splitlines()  # Split the script into individual lines
    
    # Seznam pro sledování, zda jsme narazili na OUTER APPLY
    outer_apply_found = False
    
    for line_number, line in enumerate(lines, start=1):  # Start from line 1 for better readability
        found_matches = re.findall(pattern, line, re.IGNORECASE)
        
        # Kontrola, zda je v aktuálním řádku OUTER APPLY
        if 'OUTER APPLY' in line.upper():
            outer_apply_found = True
            operation = 'OUTER APPLY'
        # Kontrola, zda je v aktuálním řádku UNION ALL
        elif 'UNION ALL' in line.upper():
            operation = 'UNION ALL'
            # Když najdeme UNION ALL, přidáme ho jako operaci
            found_matches = [(line_number, operation, "", "", "")]
        elif 'FROM' in line.upper() or 'JOIN' in line.upper() or 'LEFT JOIN' in line.upper() or 'INNER JOIN' in line.upper():
            if outer_apply_found:
                # Pokud je předchozí řádek obsahující OUTER APPLY, použijeme OUTER APPLY pro tento řádek
                operation = 'OUTER APPLY'
                outer_apply_found = False  # Reset po použití OUTER APPLY
            else:
                operation = line.split()[0].upper()  # Použijeme původní operaci (FROM, JOIN, LEFT JOIN, ...)
        
        if found_matches:
            for match in found_matches:
                dbserver, dbname, table = match[1], match[2], match[3]
                matches.append((line_number, operation, dbserver, dbname, table))
    
    return matches

# Funkce pro prohledání složky a zpracování SQL souborů
def process_sql_files(input_folder, output_file, output_list_file):
    # Otevření výstupního souboru v režimu 'w' pro přepsání souboru
    with open(output_file, 'w', encoding='utf-8') as output, \
         open(output_list_file, 'w', encoding='utf-8') as output_list:  # 'w' režim přepíše existující soubor
        output.write("--- Table Summary ---\n")
        output_list.write("--- Table List ---\n")
        
        # Projdeme všechny soubory ve složce
        for filename in os.listdir(input_folder):
            if filename.endswith(".sql"):  # Filtrujeme jen soubory s příponou .sql
                file_path = os.path.join(input_folder, filename)
                # Otevření souboru a načtení obsahu
                with open(file_path, 'r', encoding='utf-8') as file:
                    sql_script = file.read()
                    
                    # Debugging: Vytiskneme celý SQL skript pro ověření
                    print(f"\nProcessing file: {filename}")
                    print(f"SQL Script:\n{sql_script}\n")

                    table_operations = extract_tables_from_sql(sql_script)
                
                # Pokud byly nalezeny tabulky a operace, přidáme název souboru a tabulky
                tables_found = 0
                if table_operations:
                    output.write(f"\nSQL: {filename}\n")  # Přidání názvu souboru
                    for line_number, operation, dbserver, dbname, table in table_operations:
                        # Formát tabulky: [DBserver].DbName.dbo.[tabulka]
                        formatted_table = f"[{dbserver}].{dbname}.dbo.[{table}]"
                        if operation != 'UNION ALL':  # `UNION ALL` zapisujeme pouze do TableSummary_RELATION.txt
                            output_list.write(f"[{dbserver}].{dbname}.dbo.[{table}]\n")
                            tables_found += 1
                        output.write(f"Line {line_number}: {operation.upper()} - {formatted_table}\n")
                    # Přidání názvu SQL souboru a počtu tabulek do TableSummaryList.txt
                    output_list.write(f"{filename}\n")
                    output_list.write(f"Number of tables found in {filename}: {tables_found}\n")
                else:
                    print(f"No tables found in {filename}")

# Cesta k složce s SQL soubory
input_folder = r'C:\Users\rbartkova\Documents\Profinit\ALEF\Reporty\Python\Reports\IN'  # Změňte na skutečnou cestu k složce s SQL soubory

# Vytvoření cesty k výstupnímu souboru včetně složek Reports\OUT
output_folder = r'C:\Users\rbartkova\Documents\Profinit\ALEF\Reporty\Python\Reports\OUT'
output_file = os.path.join(output_folder, 'TableSummary_RELATION.txt')
output_list_file = os.path.join(output_folder, 'TableSummaryList.txt')

# Pokud složka OUT neexistuje, vytvořte ji
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Spuštění zpracování
process_sql_files(input_folder, output_file, output_list_file)
print(f"Tabulky byly zapsány do souborů {output_file} a {output_list_file}")
