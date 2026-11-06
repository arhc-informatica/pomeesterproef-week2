# PO Meesterproef — Starterproject

Startertemplate (HTML/CSS + Flask) voor de PO Meesterproef "Bouw een Maatschappelijke Webapp".
Dit is de **week 2**-versie: HTML/CSS basis + GitHub inrichten. Database en koppeling volgen in week 3/4.

## Wat zit erin?

```
POMeesterproef/
├── app.py              # Flask-app (route "/" toont index.html)
├── database.py         # Placeholder voor de database (week 3)
├── requirements.txt    # Python-dependencies
├── templates/
│   └── index.html      # HTML-pagina (Jinja2-template)
├── static/
│   ├── css/style.css   # Basis styling
│   └── js/script.js    # JavaScript (wordt later toegevoegd)
├── doc/
│   └── PO Meesterproef.pdf
└── .gitignore
```

## Vereisten

- Python 3.10 of hoger
- Git (zie hieronder)
- Een editor (bijv. VS Code)

## Project starten (lokaal)

Open een terminal in de projectmap en voer uit:

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

Je hebt nog nooit met een git-repository gewerkt? Geen probleem. Volg deze stappen.

### 1. Git installeren

- **Linux (Ubuntu/Debian):** `sudo apt install git`
- **macOS:** `brew install git` (of installeer Xcode Command Line Tools)
- **Windows:** download Git van https://git-scm.com en installeer (kies "Git Bash").

Controleer of het werkt:

```bash
git --version
```

### 2. Je identiteit instellen (éénmalig)

Git heeft je naam en e-mail nodig voor commits:

```bash
git config --global user.name "Jouw Naam"
git config --global user.email "jouw@email.nl"
```

### 3. SSH-key instellen (public key in je GitHub-profiel)

GitHub accepteert geen wachtwoord meer voor git-push. Je gebruikt een **SSH-key** (een sleutelpaar: private key op je computer, public key in je GitHub-profiel).

#### Stap 3a — Controleer of je al een key hebt

**macOS / Linux (Terminal):**
```bash
ls ~/.ssh/id_ed25519.pub
```

**Windows (Git Bash):**
```bash
ls ~/.ssh/id_ed25519.pub
```

Als het bestand bestaat, ga naar stap 3c. Zo niet, ga door.

#### Stap 3b — Een nieuwe SSH-key maken

**macOS / Linux (Terminal) en Windows (Git Bash):**
```bash
ssh-keygen -t ed25519 -C "jouw@email.nl"
```

- Druk Enter bij "Enter file in which to save..." (standaardlocatie).
- Druk Enter bij "Enter passphrase" (of typ een wachtwoordzin als je dat wilt; onthoud hem dan wel).

Dit maakt twee bestanden in `~/.ssh/`: `id_ed25519` (private, **nooit delen**) en `id_ed25519.pub` (public, mag je delen).

**Windows (PowerShell, zonder Git Bash):**
```powershell
ssh-keygen -t ed25519 -C "jouw@email.nl"
```
Het bestand komt in `C:\\Users\\<jouwnaam>\\.ssh\\`.

#### Stap 3c — Public key kopiëren

**macOS:**
```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

**Linux:**
```bash
cat ~/.ssh/id_ed25519.pub
# selecteer en kopieer de hele regel (begint met ssh-ed25519)
```

**Windows (Git Bash):**
```bash
clip < ~/.ssh/id_ed25519.pub
```

**Windows (PowerShell):**
```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | Set-Clipboard
```

#### Stap 3d — Public key toevoegen aan je GitHub-profiel

1. Ga naar https://github.com en log in.
2. Klik rechtsboven op je avatar → **Settings**.
3. Links in het menu: **SSH and GPG keys**.
4. Klik **New SSH key**.
5. **Title:** geef een naam, bijv. "MacBook school" of "Windows laptop".
6. **Key type:** Authentication Key.
7. **Key:** plak de gekopieerde public key (Ctrl+V / Cmd+V).
8. Klik **Add SSH key**. Bevestig eventueel met je wachtwoord.

#### Stap 3e — Test de verbinding

```bash
ssh -T git@github.com
```

Antwoord (eerste keer): typ `yes` en Enter. Je ziet dan:
```
Hi jouwnaam! You've successfully authenticated, but GitHub does not provide shell access.
```
Dat is goed — het werkt!

### 4. Deze starter-repo clonen

"Clonen" betekent: een kopie van de repo naar je eigen computer halen. Gebruik de **SSH-URL** (begint met `git@github.com:`):

```bash
git clone git@github.com:<organisatie>/pomeesterproef-starter.git
cd POMeesterproef
```

> Vervang `<organisatie>` door wat de docent opgeeft (bijv. `git@github.com:arhc/pomeesterproef-starter.git`).
> Als de docent een HTTPS-link geeft, gebruik je die; dan wordt om je GitHub-wachtwoord/PAT gevraagd.

### 5. Een eigen repo maken op basis van deze code

Je wilt straks je eigen code opslaan in **jouw eigen** repository, niet in die van de docent. Doe het zo:

**Stap A — Maak een nieuwe (lege) repo op GitHub**

1. Ga naar https://github.com en log in.
2. Klik op **New repository** (groene knop, rechtsboven of op je profiel).
3. Geef een naam, bijv. `pomeesterproef-jouwnaam`.
4. Kies **Private** (of Public, zoals de docent aangeeft).
5. **Vink NIET** "Initialize with README" aan (we hebben al code).
6. Klik **Create repository**.
7. Op de volgende pagina zie je een SSH-URL, bijv. `git@github.com:jouwnaam/pomeesterproef-jouwnaam.git`. Kopieer die.

**Stap B — Koppel je lokale map aan jouw nieuwe repo**

Open een terminal in je projectmap (waar `app.py` staat) en voer uit:

```bash
# Verwijder de link naar de starter-repo van de docent
git remote remove origin

# Koppel aan jouw eigen repo (SSH-URL)
git remote add origin git@github.com:jouwnaam/pomeesterproef-jouwnaam.git

# (optioneel) controleer
git remote -v
```

**Stap C — Eerste commit en push**

```bash
git add .
git commit -m "Start: week 2 starterproject"
git branch -M main
git push -u origin main
```

Nu staat jouw code op GitHub! 🎉

> Let op: de eerste `git push` kan vragen om de host-key te accepteren. Typ `yes` en Enter.

### 4. Een eigen repo maken op basis van deze code

Je wilt straks je eigen code opslaan in **jouw eigen** repository, niet in die van de docent. Doe het zo:

**Stap A — Maak een nieuwe (lege) repo op GitHub**

1. Ga naar https://github.com en log in (of maak een account).
2. Klik op **New repository** (groene knop).
3. Geef een naam, bijv. `pomeesterproef-jouwnaam`.
4. Kies **Private** (of Public, zoals de docent aangeeft).
5. **Vink NIET** "Initialize with README" aan (we hebben al code).
6. Klik **Create repository**.
7. Kopieer de URL die GitHub toont (bijv. `https://github.com/jouwnaam/pomeesterproef-jouwnaam.git`).

**Stap B — Koppel je lokale map aan jouw nieuwe repo**

Open een terminal in je projectmap (waar `app.py` staat) en voer uit:

```bash
# Verwijder de link naar de starter-repo van de docent
git remote remove origin

# Koppel aan jouw eigen repo
git remote add origin https://github.com/jouwnaam/pomeesterproef-jouwnaam.git

# (optioneel) controleer
git remote -v
```

**Stap C — Eerste commit en push**

```bash
git add .
git commit -m "Start: week 2 starterproject"
git branch -M main
git push -u origin main
```

Nu staat jouw code op GitHub! 🎉

### 5. Basis-workflow (elke keer dat je werkt)

```bash
# Status bekijken
git status

# Wijzigingen klaarzetten
git add .

# Opslaan met een bericht
git commit -m "Beschrijf wat je hebt gedaan"

# Uploaden naar GitHub
git push
```

### 6. Handige commando's

| Commando | Wat het doet |
|---|---|
| `git status` | Wat is er veranderd? |
| `git log --oneline` | Geschiedenis van commits |
| `git pull` | Nieuwe wijzigingen van GitHub ophalen |
| `git diff` | Verschillen bekijken |
| `git restore <bestand>` | Wijziging in een bestand ongedaan maken |

### 7. Veelgemaakte fouten (en oplossingen)

- **"fatal: not a git repository"** → Je staat niet in de projectmap. Gebruik `cd` om ernaar toe te gaan.
- **"Authentication failed"** → Gebruik een Personal Access Token (PAT) in plaats van je wachtwoord. Zie GitHub Docs → "Creating a personal access token".
- **Merge conflict** → Vraag de docent of een klasgenoot om hulp; dit komt later in de cursus.

## Versies per week (organisatie)

De docent beheert deze startercode per week via **branches**:

- `week-2` — huidige versie (HTML/CSS basis) ← je begint hier
- `week-3` — week 2 + database (.sql starter + `database.py`)
- `week-4` — week 3 + koppeling (formulier → database)

### Welke versie ophalen?

```bash
# Lijst van branches bekijken
git branch -a

# Naar een andere week wisselen (bijv. week 3)
git checkout week-3
# of (nieuwere git-versies):
git switch week-3
```

> Tip: maak eerst een commit van je eigen werk voordat je wisselt van branch, anders raak je wijzigingen kwijt.

## .gitignore

Bestanden die **niet** in git thuishoren (zoals de virtuele omgeving `.venv/` en de database `*.db`) staan al in `.gitignore`. Voeg er zelf niets aan toe dat geheim is (wachtwoorden, API-keys).

## Hulp

Loop je vast? Zet de taak op 'Showstopper' en neem dit mee naar het Daltonuur. De docent helpt je persoonlijk.