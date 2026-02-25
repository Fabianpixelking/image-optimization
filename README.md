# 🖼️ Image Optimization Tool

Ein CLI-Tool zur automatischen Bildoptimierung für das Web. Das Tool liest alle Bilddateien aus dem `input/`-Ordner, optimiert sie und speichert die Ergebnisse im `output/`-Ordner.

---

## 🎯 Ziel

Alle Bilder aus dem Input-Ordner automatisch für den Einsatz im Web optimieren:

- **Format-Konvertierung:** Jedes Bild wird als optimiertes `.jpg` **und** als optimiertes `.webp` ausgegeben
- **Größenanpassung:** Die längste Kante wird auf **maximal 1920 Pixel** begrenzt (kleinere Bilder bleiben unverändert)
- **Qualitätsoptimierung:** Komprimierung für schnelle Ladezeiten bei guter visueller Qualität

---

## 📁 Ordnerstruktur

```
image-optimization/
├── input/              # Quellbilder hier ablegen
├── output/             # Optimierte Bilder werden hier ausgegeben
│   ├── bild1.jpg       # Optimiertes JPEG
│   ├── bild1.webp      # Optimiertes WebP
│   ├── bild2.jpg
│   ├── bild2.webp
│   └── ...
├── optimize.py         # Haupt-Script
├── requirements.txt    # Python-Abhängigkeiten
├── .gitignore
└── README.md
```

---

## ⚙️ Geplante Features

### MVP (v1.0)

- [ ] **Input-Ordner scannen** — Alle gängigen Bildformate erkennen (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.webp`)
- [ ] **Größenanpassung** — Bilder proportional skalieren, sodass die längste Kante max. 1920px beträgt
- [ ] **JPEG-Export** — Optimiertes JPEG mit konfigurierbarer Qualität (Standard: 85%)
- [ ] **WebP-Export** — Optimiertes WebP mit konfigurierbarer Qualität (Standard: 80%)
- [ ] **Dateinamen beibehalten** — Originalname wird für beide Output-Dateien übernommen (z.B. `foto.jpg` + `foto.webp`)
- [ ] **Fortschrittsanzeige** — Konsolenausgabe mit Verarbeitungsstatus pro Bild
- [ ] **Fehlerbehandlung** — Beschädigte oder nicht unterstützte Dateien überspringen und loggen

### Optional (v1.1+)

- [ ] Konfigurierbare maximale Kantenlänge (CLI-Argument)
- [ ] Konfigurierbare Qualitätsstufen (CLI-Argument)
- [ ] Unterordner-Struktur im Input beibehalten
- [ ] Bereits verarbeitete Bilder überspringen (Skip-Logik)
- [ ] Batch-Verarbeitung mit Fortschrittsbalken (z.B. `tqdm`)

---

## 🛠️ Technologie-Stack

| Komponente       | Technologie                          |
|------------------|--------------------------------------|
| Sprache          | **Python 3.10+**                     |
| Bildverarbeitung | **Pillow** (PIL Fork)                |
| CLI              | **argparse** (Python Standardlib)    |
| Fortschritt      | **print** / optional `tqdm`          |

---

## 🚀 Geplante Nutzung

```bash
# 1. Abhängigkeiten installieren
pip install -r requirements.txt

# 2. Bilder in den input/-Ordner legen

# 3. Script ausführen
python optimize.py

# 4. Optimierte Bilder befinden sich im output/-Ordner
```

### Optionale CLI-Argumente (v1.1+)

```bash
python optimize.py --max-size 1920 --quality-jpg 85 --quality-webp 80
```

---

## 📋 Implementierungsplan

### Schritt 1: Setup
- `requirements.txt` mit Pillow erstellen
- Grundstruktur des Scripts `optimize.py` anlegen

### Schritt 2: Kern-Logik
1. **Input-Ordner lesen** — Alle Bilddateien identifizieren
2. **Bild laden** — Mit Pillow öffnen und EXIF-Orientierung berücksichtigen
3. **Größe anpassen** — Proportional skalieren, falls längste Kante > 1920px
4. **Als JPEG speichern** — Optimiert mit konfigurierter Qualität
5. **Als WebP speichern** — Optimiert mit konfigurierter Qualität
6. **Fortschritt ausgeben** — Dateiname, Originalgröße → neue Größe, Dateigröße

### Schritt 3: Fehlerbehandlung & Polish
- Try/Except um die Bildverarbeitung
- Zusammenfassung am Ende (Anzahl verarbeitet, übersprungen, Fehler)
- Output-Ordner automatisch erstellen falls nicht vorhanden

---

## 📄 Lizenz

Privates Projekt
