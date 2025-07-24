# Základní Git příkazy pro Visual Studio Code

| Příkaz                             | Význam                                                                 |
|-----------------------------------|------------------------------------------------------------------------|
| `git init`                        | Inicializuje nový Git repozitář v aktuální složce                      |
| `git clone <URL>`                 | Stáhne (naklonuje) repozitář z GitHubu do lokální složky               |
| `git status`                     | Zobrazí stav změn (co je upraveno, staged, nebo připraveno ke commitu) |
| `git add .`                      | Přidá všechny změněné/nové soubory ke commitu (do staging oblasti)     |
| `git commit -m "popis změn"`      | Uloží změny jako commit se zprávou                                     |
| `git log`                        | Zobrazí historii commitů                                               |
| `git diff`                       | Ukáže rozdíly mezi upravenými soubory a posledním commitem             |
| `git push`                       | Odesílá změny do vzdáleného repozitáře (např. na GitHub)               |
| `git pull`                       | Stáhne změny z GitHubu a sloučí je s lokálním repozitářem              |
| `git fetch`                      | Stáhne nové změny z GitHubu, ale **neprovádí sloučení (merge)**        |
| `git merge <větev>`              | Sloučí jinou větev do aktuální                                         |
| `git branch`                     | Vypíše existující větve                                                |
| `git branch <název>`             | Vytvoří novou větev                                                   |
| `git checkout <větev>`           | Přepne na jinou větev                                                  |
| `git checkout -b <název>`        | Vytvoří a přepne na novou větev                                       |
| `git remote -v`                  | Zobrazí URL vzdáleného repozitáře (např. GitHub)                      |
| `git remote set-url origin <URL>`| Změní URL vzdáleného repozitáře                                       |

---

### Tipy pro Visual Studio Code

- Levý panel **Source Control (ikona se třemi čarami)** ti umožňuje provádět:
  - `git add` (checkbox u změněného souboru)
  - `git commit` (pole pro zprávu + ikonka „✓“)
  - `git push` / `git pull` (ikonky v pravém dolním rohu)
