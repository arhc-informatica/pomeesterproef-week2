# PO Meesterproef — Week 2 Starter (HTML/CSS)

Startertemplate (HTML/CSS + Flask) voor de PO Meesterproef "Bouw een Maatschappelijke Webapp".
Dit is de **week 2**-versie: HTML/CSS basis + GitHub inrichten. Database (week 3) en koppeling (week 4) volgen later via aparte template-repo's.

> Dit is een **template repository**. Klik op **"Use this template"** → **"Create a new repository"** om je eigen kopie te maken. Daarna werk je in jouw eigen repo.

## Wat zit erin?

```
pomeesterproef-week2/
├── app.py              # Flask-app (route "/" toont index.html)
├── database.py         # Placeholder voor de database (week 3)
├── requirements.txt    # Python-dependencies
├── templates/
│   └── index.html      # HTML-pagina (Jinja2-template)
├── static/
│   ├── css/style.css   # Basis styling
│   └── js/script.js    # JavaScript (wordt later toegevoegd)
└── .gitignore
```

## Vereisten

- Python 3.10 of hoger
- Git (zie hieronder)
- Een editor (bijv. VS Code)

## Project starten (lokaal)

> **Let op:** `git clone` maakt de map automatisch aan. Je hoeft dus **geen** map zelf aan te maken. Na het clonen ga je de map in.

Stappen:
1. Clone (maakt de map aan):
   ```bash
   git clone git@github.com:jouwnaam/pomeesterproef-jouwnaam.git
   ```
2. Ga de nieuwe map in:
   ```bash
   cd pomeesterproef-jouwnaam
   ```
   Controleer dat je in de map zit waar `app.py` staat (`ls` / `dir`).

Daarna in die map uitvoeren:

```bash
# 1. Virtuele omgeving aanmaken
python3 -m venv .venv

# 2. Activeren
# Linux/macOS:
source .venv/bin/activate
# Windows (PowerShell):
# .venv\Scripts\Activate.ps1

# 3. Dependencies installeren
pip install -r requirements.txt

# 4. App starten
python app.py
```

Open daarna http://127.0.0.1:5000 in je browser.

## Git voor beginners — stap voor stap

### 1. Git installeren

- **Linux (Ubuntu/Debian):** `sudo apt install git`
- **macOS:** `brew install git` (of installeer Xcode Command Line Tools)
- **Windows:** download Git van https://git-scm.com en installeer (kies "Git Bash").

Controleer of het werkt:

```bash
git --version
```

### 2. Je identiteit instellen (éénmalig)

```bash
git config --global user.name "Jouw Naam"
git config --global user.email "jouw@email.nl"
```

### 3. SSH-key instellen (public key in je GitHub-profiel)

GitHub accepteert geen wachtwoord meer voor git-push. Je gebruikt een **SSH-key**.

#### 3a — Controleer of je al een key hebt

```bash
ls ~/.ssh/id_ed25519.pub
```

Als het bestand bestaat, ga naar stap 3c.

#### 3b — Een nieuwe SSH-key maken

```bash
ssh-keygen -t ed25519 -C "jouw@email.nl"
```

Druk Enter bij de vragen (standaardlocatie, geen passphrase of onthoud hem).

#### 3c — Public key kopiëren

- **macOS:** `pbcopy < ~/.ssh/id_ed25519.pub`
- **Linux:** `cat ~/.ssh/id_ed25519.pub` (selecteer en kopieer)
- **Windows (Git Bash):** `clip < ~/.ssh/id_ed25519.pub`
- **Windows (PowerShell):** `Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | Set-Clipboard`

#### 3d — Public key toevoegen aan je GitHub-profiel

1. GitHub → rechtsboven avatar → **Settings** → **SSH and GPG keys**.
2. **New SSH key** → plak de key → **Add SSH key**.

#### 3e — Test de verbinding

```bash
ssh -T git@github.com
```

Je ziet: `Hi jouwnaam! You've successfully authenticated...` → werkt!

### 4. Jouw eigen repo maken (via template)

De docent-repo is een **template**: https://github.com/ehijzengsf/pomeesterproef-week2

1. Open die link in je browser.
2. Klik op de groene knop **"Use this template"** → **"Create a new repository"**.
3. Geef een naam, bijv. `pomeesterproef-jouwnaam`.
4. Kies **Private** (of Public, zoals de docent aangeeft).
5. Klik **Create repository**.

Nu heb je je eigen repo. Clone die:

```bash
git clone git@github.com:jouwnaam/pomeesterproef-jouwnaam.git
cd pomeesterproef-jouwnaam
```

### 5. Basis-workflow (elke keer dat je werkt)

```bash
git status
git add .
git commit -m "Beschrijf wat je hebt gedaan"
git push
```

### 6. Handige commando's

| Commando | Wat het doet |
|---|---|
| `git status` | Wat is er veranderd? |
| `git log --oneline` | Geschiedenis van commits |
| `git pull` | Nieuwe wijzigingen ophalen |
| `git diff` | Verschillen bekijken |
| `git restore <bestand>` | Wijziging ongedaan maken |

### 7. Veelgemaakte fouten

- **"fatal: not a git repository"** → Je staat niet in de projectmap (`cd`).
- **"Permission denied (publickey)"** → SSH-key niet geregistreerd (zie stap 3).
- **Merge conflict** → Vraag de docent om hulp.

## Samenwerken in een groepje van 2

Werken jullie met z'n tweeën aan één project? Doe het zo:

1. **Eén persoon** maakt de repo aan via "Use this template" en kiest een naam, bijv. `pomeesterproef-jouwnaam1-en-jouwnaam2`.
2. Die persoon voegt de ander toe als **collaborator**: repo → **Settings** → **Collaborators** → **Add people** → vul de GitHub-gebruikersnaam van je partner in → **Add**.
3. Je partner accepteert de uitnodiging (e-mail of via GitHub → "You have been invited").
4. **Beide** clonen dezelfde repo:
   ```bash
   git clone git@github.com:<eigenaar>/pomeesterproef-jouwnaam1-en-jouwnaam2.git
   cd pomeesterproef-jouwnaam1-en-jouwnaam2
   ```
5. **Werkafspraak (belangrijk!):**
   - Doe altijd eerst `git pull` voordat je begint.
   - Werk niet tegelijk aan hetzelfde bestand.
   - Commit en push regelmatig met duidelijke berichten.
   - Bij een conflict: overleg en los samen op, of vraag de docent.

> Tip: werk in aparte bestanden (bijv. één persoon HTML/CSS, de ander database) om conflicten te voorkomen.

## Versies per week

Elke week krijg je een **nieuwe template-repo** van de docent:

- **Week 2** (deze repo) — HTML/CSS basis
- **Week 3** — week 2 + database (.sql starter)
- **Week 4** — week 3 + koppeling formulier → database

Je hoeft niet van branch te wisselen; je maakt een nieuwe repo via "Use this template".

## .gitignore

Bestanden die niet in git thuishoren (`.venv/`, `*.db`) staan al in `.gitignore`.

## Hulp

Loop je vast? Zet de taak op 'Showstopper' en neem dit mee naar het Daltonuur.