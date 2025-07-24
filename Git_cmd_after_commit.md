# 🔁 Co následuje po `git commit`?

Po příkazu `git commit`, který uloží změny do **lokální historie**, obvykle následují další Git příkazy – v závislosti na tom, co právě děláš.

---

## 📌 Nejčastější scénáře po `git commit`

| Scénář                              | Následující příkaz                         | Význam                                                                 |
|-------------------------------------|--------------------------------------------|------------------------------------------------------------------------|
| 📨 Chceš změny odeslat na GitHub    | `git push origin main`                     | Odešle commit(y) do vzdáleného repozitáře                             |
| 🔁 Chceš stáhnout a sloučit cizí změny | `git pull origin main`                     | Stáhne změny z GitHubu a sloučí je s tvými                            |
| 🌱 Pracuješ ve větvi a chceš ji sloučit | `git checkout main` → `git merge jmenovetev` | Sloučí vedlejší větev do hlavní                                       |
| 🔄 Chceš si zkontrolovat historii   | `git log --oneline`                        | Rychlý přehled commitů                                                 |
| 📤 Chceš nahrát vše v jednom kroku  | `git add . && git commit -m "..." && git push` | Přidání, commit a push v jednom kroku                                 |

---

## 🔁 Větvení a práce v týmu

```bash
git checkout -b novafunkce      # vytvoř a přepni na novou větev
git push -u origin novafunkce   # pushni novou větev na GitHub
```

## 🧪 Příklad typického postupu (lokálně → GitHub)

```bash
git status                              # zjistit, co je změněno
git add .                               # přidat všechny změny
git commit -m "Přidání nové funkce"     # uložit změny lokálně
git pull origin main --rebase           # stáhnout nové změny a zarovnat
git push origin main                    # odeslat commit na GitHub
```

## ✍️ Rychlá poznámka

```bash
git commit                              # lokální akce – změny se uloží jen u tebe
git push                                # odeslání změn na vzdálený repozitář (např. GitHub)
git pull                                # stažení změn od ostatních a jejich sloučení s tvou prací
```
