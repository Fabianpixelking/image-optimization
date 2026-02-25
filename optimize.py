"""
Image Optimization Tool
Liest Bilder aus input/, optimiert sie und speichert JPEG + WebP in output/.
"""

import os
import sys
from pathlib import Path
from PIL import Image, ImageOps

# --- Konfiguration ---
INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")
MAX_SIZE = 1920          # längste Kante in Pixeln
QUALITY_JPG = 85
QUALITY_WEBP = 80

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif", ".webp"}


def format_bytes(num_bytes: int) -> str:
    """Gibt eine lesbare Dateigröße zurück (KB oder MB)."""
    if num_bytes >= 1_000_000:
        return f"{num_bytes / 1_000_000:.1f} MB"
    return f"{num_bytes / 1_000:.1f} KB"


def to_rgb(img: Image.Image) -> Image.Image:
    """Konvertiert ein Bild in den RGB-Modus. Transparenz wird auf weißem Hintergrund abgelegt."""
    if img.mode == "RGB":
        return img
    if img.mode in ("RGBA", "LA", "PA"):
        background = Image.new("RGB", img.size, (255, 255, 255))
        mask = img.split()[-1] if img.mode in ("RGBA", "LA") else img.convert("RGBA").split()[-1]
        background.paste(img.convert("RGBA"), mask=mask)
        return background
    return img.convert("RGB")


def process_image(src_path: Path) -> tuple[bool, str]:
    """
    Verarbeitet ein einzelnes Bild.
    Gibt (True, info_string) bei Erfolg zurück, (False, error_string) bei Fehler.
    """
    try:
        src_size = src_path.stat().st_size
        stem = src_path.stem

        with Image.open(src_path) as img:
            # EXIF-Orientierung korrigieren (Hochformat-Fotos vom Handy etc.)
            img = ImageOps.exif_transpose(img)
            original_dimensions = img.size

            # Farbmodus normalisieren
            img = to_rgb(img)

            # Größe anpassen (nur verkleinern, nie vergrößern)
            if max(img.size) > MAX_SIZE:
                img.thumbnail((MAX_SIZE, MAX_SIZE), Image.LANCZOS)

            new_dimensions = img.size

            # JPEG speichern
            jpg_path = OUTPUT_DIR / f"{stem}.jpg"
            img.save(
                jpg_path,
                format="JPEG",
                quality=QUALITY_JPG,
                optimize=True,
                progressive=True,
            )

            # WebP speichern
            webp_path = OUTPUT_DIR / f"{stem}.webp"
            img.save(
                webp_path,
                format="WEBP",
                quality=QUALITY_WEBP,
                method=6,
            )

        jpg_size = jpg_path.stat().st_size
        webp_size = webp_path.stat().st_size

        resized = (
            f"{original_dimensions[0]}x{original_dimensions[1]}px -> {new_dimensions[0]}x{new_dimensions[1]}px"
            if original_dimensions != new_dimensions
            else f"{original_dimensions[0]}x{original_dimensions[1]}px (unveraendert)"
        )

        savings_jpg = (1 - jpg_size / src_size) * 100
        savings_webp = (1 - webp_size / src_size) * 100

        info = (
            f"  Dimension : {resized}\n"
            f"  Original  : {format_bytes(src_size)}\n"
            f"  JPEG      : {format_bytes(jpg_size)} ({savings_jpg:+.0f}%)\n"
            f"  WebP      : {format_bytes(webp_size)} ({savings_webp:+.0f}%)"
        )
        return True, info

    except Exception as exc:
        return False, str(exc)


def main():
    # Verzeichnisse prüfen / anlegen
    if not INPUT_DIR.exists():
        print(f"[FEHLER] Input-Ordner '{INPUT_DIR}' nicht gefunden.")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Bilddateien sammeln
    images = [
        p for p in sorted(INPUT_DIR.iterdir())
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not images:
        print(f"Keine unterstützten Bilder in '{INPUT_DIR}' gefunden.")
        print(f"Unterstützte Formate: {', '.join(sorted(SUPPORTED_EXTENSIONS))}")
        sys.exit(0)

    print(f"Image Optimization Tool")
    print(f"{'=' * 50}")
    print(f"Input-Ordner : {INPUT_DIR.resolve()}")
    print(f"Output-Ordner: {OUTPUT_DIR.resolve()}")
    print(f"Max. Kantenlaenge: {MAX_SIZE}px  |  JPEG: {QUALITY_JPG}%  |  WebP: {QUALITY_WEBP}%")
    print(f"{'=' * 50}")
    print(f"{len(images)} Bild(er) gefunden\n")

    processed = 0
    skipped = 0
    errors = 0

    for i, img_path in enumerate(images, start=1):
        print(f"[{i}/{len(images)}] {img_path.name}")
        success, info = process_image(img_path)

        if success:
            print(info)
            processed += 1
        else:
            print(f"  [FEHLER] {info}")
            errors += 1

        print()

    # Zusammenfassung
    print(f"{'=' * 50}")
    print(f"Fertig!")
    print(f"  Verarbeitet : {processed}")
    print(f"  Fehler      : {errors}")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
