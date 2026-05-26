import os

files = [
    "index.html",
    "projets.html",
    "contact.html",
    "detail-tp-info-indus.html",
    "detail-bras-robotique.html",
    "detail-hackathon.html",
    "sae-thermo.html"
]

lang_selector_en = """
        <div class="lang-selector">
            <button class="lang-btn">
                <img src="https://flagcdn.com/w40/gb.png" alt="English"> EN <i class="fa-solid fa-chevron-down" style="font-size: 0.8rem;"></i>
            </button>
            <div class="lang-dropdown">
                <a href="{fr_link}" class="lang-option">
                    <img src="https://flagcdn.com/w40/fr.png" alt="Français"> Français
                </a>
            </div>
        </div>
"""

lang_selector_fr = """
        <div class="lang-selector">
            <button class="lang-btn">
                <img src="https://flagcdn.com/w40/fr.png" alt="Français"> FR <i class="fa-solid fa-chevron-down" style="font-size: 0.8rem;"></i>
            </button>
            <div class="lang-dropdown">
                <a href="{en_link}" class="lang-option">
                    <img src="https://flagcdn.com/w40/gb.png" alt="English"> English
                </a>
            </div>
        </div>
"""

def add_selector(content, is_fr, filename):
    en_filename = filename
    fr_filename = filename.replace(".html", "_fr.html")
    
    selector = lang_selector_fr.format(en_link=en_filename) if is_fr else lang_selector_en.format(fr_link=fr_filename)
    
    if "</nav>" in content:
        content = content.replace("</nav>", "</nav>" + selector)
    return content

def fix_links(content, is_fr):
    if is_fr:
        for f in files:
            content = content.replace(f'href="{f}"', f'href="{f.replace(".html", "_fr.html")}"')
    return content

# Quick translations for the nav
translations_nav = {
    "Accueil": "Home",
    "Mes Projets": "My Projects",
    "Contact": "Contact",
    "Mes Réalisations": "My Projects",
    "À propos de moi": "About me",
    "Expériences Professionnelles": "Professional Experience",
    "Mes Compétences": "My Skills"
}

def translate_basic(content, is_fr):
    if not is_fr:
        for k, v in translations_nav.items():
            content = content.replace(f'>{k}<', f'>{v}<')
    return content

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # Create French version
    fr_content = fix_links(add_selector(content, True, f), True)
    with open(f.replace(".html", "_fr.html"), "w") as file:
        file.write(fr_content)
        
    # Update English version
    en_content = translate_basic(fix_links(add_selector(content, False, f), False), False)
    with open(f, "w") as file:
        file.write(en_content)

print("Done")
