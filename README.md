# Image Optimization Tool

Ein schlankes CLI-Tool zur automatischen Bildoptimierung für das Web. Bilder aus dem `input/`-Ordner werden verkleinert, komprimiert und als **JPEG** und **WebP** in den `output/`-Ordner geschrieben.

## Features

- **Dual-Export** — Jedes Bild wird als `.jpg` und `.webp` ausgegeben
- **Automatische Skalierung** — Die längste Kante wird auf maximal 1920 px begrenzt; kleinere Bilder bleiben unverändert
- **EXIF-Korrektur** — Rotierte Fotos (z. B. Handy-Hochformat) werden automatisch korrekt ausgerichtet
- **Transparenz-Handling** — PNG mit Alpha-Kanal (RGBA) wird auf weißem Hintergrund für JPEG abgeflacht
- **Fortschrittsausgabe** — Dimensionen, Dateigrößen und Einsparung in % pro Bild
- **Fehlerresistent** — Beschädigte oder nicht lesbare Dateien werden übersprungen und geloggt

## Voraussetzungen

- Python 3.10+
- [Pillow](https://python-pillow.org/)

## Installation

```bash
git clone https://github.com/dein-name/image-optimization.git
cd image-optimization
pip install -r requirements.txt
```

## Nutzung

1. Bilder in den `input/`-Ordner legen
2. Script ausführen:

```bash
python optimize.py
```

3. Optimierte Bilder befinden sich im `output/`-Ordner

### Beispiel-Output

```
Image Optimization Tool
==================================================
Input-Ordner : /pfad/zum/projekt/input
Output-Ordner: /pfad/zum/projekt/output
Max. Kantenlaenge: 1920px  |  JPEG: 85%  |  WebP: 80%
==================================================
3 Bild(er) gefunden

[1/3] foto.jpg
  Dimension : 4000x3000px -> 1920x1440px
  Original  : 5.2 MB
  JPEG      : 312.4 KB (+94%)
  WebP      : 134.7 KB (+97%)

...

==================================================
Fertig!
  Verarbeitet : 3
  Fehler      : 0
==================================================
```

## Unterstuetzte Formate

| Eingabe | Ausgabe |
|---------|---------|
| `.jpg`, `.jpeg` | `.jpg` + `.webp` |
| `.png` | `.jpg` + `.webp` |
| `.webp` | `.jpg` + `.webp` |
| `.bmp`, `.tiff`, `.tif` | `.jpg` + `.webp` |

## Ordnerstruktur

```
image-optimization/
├── input/           # Quellbilder hier ablegen
├── output/          # Optimierte Bilder (wird automatisch erstellt)
├── optimize.py
├── requirements.txt
└── README.md
```

## Konfiguration

Die Standardwerte lassen sich direkt am Anfang von `optimize.py` anpassen:

```python
MAX_SIZE     = 1920   # Maximale Kantenlange in Pixeln
QUALITY_JPG  = 85     # JPEG-Qualitat (0-95)
QUALITY_WEBP = 80     # WebP-Qualitat (0-100)
```

## Roadmap

- [ ] CLI-Argumente (`--max-size`, `--quality-jpg`, `--quality-webp`)
- [ ] `--skip-existing` — bereits verarbeitete Bilder ueberspringen
- [ ] Unterordner-Struktur beibehalten
- [ ] Fortschrittsbalken mit `tqdm`
- [ ] AVIF-Export als drittes Format

## Lizenz

MIT
