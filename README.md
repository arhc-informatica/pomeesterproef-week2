# PO Meesterproef — Week 2 Starter (HTML/CSS)

Startertemplate (HTML/CSS + Flask) voor de PO Meesterproef.
Dit is de **week 2**-versie: HTML/CSS basis + GitHub inrichten. Database (week 3) en koppeling (week 4) volgen later via aparte template-repo's.
Je mag een eigen onderwerp kiezen.

> Dit is een **voorbeeld-template**. Je maakt hieruit geen nieuwe repo; je clonet hem in een nieuwe map als voorbeeld en kopieert code naar je eigen (lege) repo.

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

## Opdrachten (week 2)

- Pas de CSS aan met kleuren en fonts zoals je die hebt bedacht in je ontwerp.
- Breid de HTML uit zodat het je homepage van de app gaat worden.
- Maak een nieuwe pagina voor een van je pagina's zoals je die in je ontwerp hebt bedacht. Maak een route naar de pagina. Zorg dat de algemene CSS in je pagina zit.
- Maak een menu en zorg voor links naar de homepage en naar je nieuwe pagina.
- **Let op je taalgebruik:** zorg voor duidelijke koppen en korte, foutloze zinnen die passen bij jouw doelgroep.

## Vereisten

- Python 3.10 of hoger
- Git (zie hieronder)
- Een editor (bijv. VS Code)

## Project starten (lokaal)

> **Let op:** Maak eerst een **nieuwe lege repo** op GitHub en deel hem met je partner (zie stap 4). Daarna clone je die naar je laptop. De **template (week 2)** gebruik je als **voorbeeld** in een nieuwe map; daaruit kopieer je de code naar je eigen repo.

Stappen voor het voorbeeld (week 2 template):
- Template-repo (open in browser om te vinden): https://github.com/arhc-informatica/pomeesterproef-week2
1. Maak een nieuwe map aan en ga erin:
   ```bash
   mkdir pomeesterproef-week2-voorbeeld
   cd pomeesterproef-week2-voorbeeld
   ```
2. Clone de template in deze map (SSH):
   ```bash
   git clone git@github.com:arhc-informatica/pomeesterproef-week2.git .
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

> **Werken in je eigen project:** je eigen repo (`pomeesterproef-jouwnaam`) maak je aan via "Use this template" (stap 4) en deel je met je partner. Kopieer code uit het voorbeeld naar je eigen project, commit en push daarna in je eigen repo.

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

### 4. Jouw eigen (lege) repo maken — op de GitHub-website

> **Let op:** dit doe je in je **browser** op de GitHub-website, niet in de terminal.

1. Ga naar GitHub → **New repository** (of "+" → New repository).
2. Geef een naam, bijv. `pomeesterproef-jouwnaam` (of `pomeesterproef-jouwnaam1-en-jouwnaam2` bij samenwerken).
3. Kies **Private** (of Public, zoals de docent aangeeft).
4. **Laat "Initialize with README" uit** (lege repo).
5. Klik **Create repository**.

**Samenwerken?** Voeg je partner (en docent) toe als collaborator: repo → **Settings** → **Collaborators** → **Add people**.

Clone daarna je eigen (lege) repo naar je laptop:

```bash
git clone git@github.com:jouwnaam/pomeesterproef-jouwnaam.git
cd pomeesterproef-jouwnaam
```

Kopieer vervolgens de bestanden uit het **voorbeeld** (week 2 template) in deze map, commit en push.

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

1. **Eén persoon** maakt een **nieuwe lege repo** aan **op de GitHub-website** (browser, niet terminal) en kiest een naam, bijv. `pomeesterproef-jouwnaam1-en-jouwnaam2`.
2. Die persoon voegt de ander (en eventueel de docent) toe als **collaborator**: repo → **Settings** → **Collaborators** → **Add people** → vul de GitHub-gebruikersnaam van je partner (en van de docent) in → **Add**.
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

## .gitignore

Bestanden die niet in git thuishoren (`.venv/`, `*.db`) staan al in `.gitignore`.

## Hulp

Loop je vast? Zet de taak op 'Showstopper' en neem dit mee naar het Daltonuur.

### Routes

Een **route** is een koppeling tussen een URL (adres in de browser) en een Python-functie in je Flask-app. Wanneer een bezoeker een bepaalde URL opent, voert Flask de gekoppelde functie uit en stuurt het resultaat (bijv. een HTML-pagina) terug. Zo kun je meerdere pagina's maken zonder aparte HTML-bestanden handmatig te serveren.

Kijk op W3Schools: **Python → Flask → Routes** (https://www.w3schools.com/python/python_flask.asp).

### Pagina's

Nieuwe HTML-pagina's voeg je toe in de map `templates/` (bijv. `templates/nieuwepagina.html`). In Flask verwijs je ernaar met `render_template('nieuwepagina.html')` in de bijbehorende route. Zorg dat de algemene CSS ook in die pagina zit (via `{% extends %}` of door dezelfde `<link>` naar `static/css/style.css`).

Kijk op W3Schools: **Python → Flask → Templates** (https://www.w3schools.com/python/python_flask.asp).

### Menu

Een eenvoudig menu maak je met een `<nav>`-element met een `<ul>` van `<li>`-items, waarbij elke `<li>` een `<a href="...">` bevat naar de betreffende route (bijv. `/` en `/nieuwepagina`). Style het menu in je CSS (bijv. horizontaal met `display: flex`).

Kijk op W3Schools: **HTML → Navigation / CSS → Navbar** (https://www.w3schools.com/css/css_navbar.asp).

### Virtuele omgeving (venv)

Een **virtuele omgeving** isoleert de Python-pakketten van je project, zodat ze niet botsen met andere projecten.

- Aanmaken: `python3 -m venv .venv`
- Activeren (Linux/macOS): `source .venv/bin/activate`
- Activeren (Windows PowerShell): `.venv\Scripts\Activate.ps1`
- Dependencies installeren: `pip install -r requirements.txt`
- De map `.venv/` staat in `.gitignore` en wordt dus niet naar GitHub gestuurd.