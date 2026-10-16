#!/usr/bin/env python3
"""Build a translation-only Workshop overlay for all mods in mods.json."""

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]


def collect_files():
    manifest = json.loads((ROOT / "mods.json").read_text(encoding="utf-8"))
    files = []
    used_ids = set()
    for mod in manifest["mods"]:
        workshop_id = mod["workshopId"]
        slug = mod["slug"]
        if not re.fullmatch(r"[0-9]+", workshop_id) or workshop_id in used_ids:
            raise ValueError(f"ID da Oficina inválido ou repetido: {workshop_id}")
        if not re.fullmatch(r"[A-Za-z0-9_-]+", slug):
            raise ValueError(f"Nome de pasta de mod inválido: {slug}")
        used_ids.add(workshop_id)
        language_root = ROOT / "mods" / slug / "Languages" / "PortugueseBrazilian"
        if not language_root.is_dir():
            raise ValueError(f"Tradução ausente: {language_root}")
        xml_files = sorted(language_root.rglob("*.xml"))
        if not xml_files:
            raise ValueError(f"Nenhum XML encontrado: {language_root}")
        for path in xml_files:
            if path.is_symlink():
                raise ValueError(f"Links simbólicos não são permitidos: {path}")
            root = ET.parse(path).getroot()
            if root.tag != "LanguageData":
                raise ValueError(f"Raiz XML inesperada em {path}: {root.tag}")
            keys = [element.tag for element in root]
            if len(set(keys)) != len(keys) or any(not (e.text or "").strip() for e in root):
                raise ValueError(f"Chaves duplicadas ou textos vazios em {path}")
            relative = path.relative_to(ROOT / "mods" / slug)
            files.append((path, f"{workshop_id}/{relative.as_posix()}"))
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="Tag de versão, por exemplo v1.0.0")
    args = parser.parse_args()
    if not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", args.version):
        parser.error("Use uma versão como v1.0.0")
    files = collect_files()
    output = ROOT / "dist" / f"RimWorld_Mods_PT-BR_{args.version}.zip"
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path, arcname in files:
            info = zipfile.ZipInfo(arcname, date_time=(2024, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    print(f"{output} ({len(files)} arquivos)")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, ET.ParseError) as error:
        sys.exit(str(error))
