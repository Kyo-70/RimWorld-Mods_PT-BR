#!/usr/bin/env python3
"""Compare translated XML keys and placeholders with a local upstream mod."""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = re.compile(r"\{[^{}]+\}")


def check(mod_root, source_root):
    target = mod_root / "Languages" / "PortugueseBrazilian"
    source = source_root / "Languages" / "English"
    errors = []
    count = 0
    for target_file in sorted(target.rglob("*.xml")):
        relative = target_file.relative_to(target)
        source_file = source / relative
        if not source_file.is_file():
            errors.append(f"Arquivo original ausente: {source_file}")
            continue
        original = ET.parse(source_file).getroot()
        translated = ET.parse(target_file).getroot()
        original_keys = {element.tag: element.text or "" for element in original}
        translated_keys = {element.tag: element.text or "" for element in translated}
        for key in sorted(original_keys.keys() ^ translated_keys.keys()):
            errors.append(f"Chave ausente ou excedente em {relative}: {key}")
        for key in original_keys.keys() & translated_keys.keys():
            old, new = original_keys[key], translated_keys[key]
            if Counter(PLACEHOLDER.findall(old)) != Counter(PLACEHOLDER.findall(new)):
                errors.append(f"Marcadores diferentes em {relative}: {key}")
            if old.count("\\n") != new.count("\\n") or old.count("\n") != new.count("\n"):
                errors.append(f"Quebras de linha diferentes em {relative}: {key}")
            if not new.strip():
                errors.append(f"Texto vazio em {relative}: {key}")
        count += len(translated_keys)
    for source_file in sorted(source.rglob("*.xml")):
        if not (target / source_file.relative_to(source)).is_file():
            errors.append(f"Arquivo de tradução ausente: {source_file.relative_to(source)}")
    return count, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mod", required=True, help="Pasta do mod em mods/")
    parser.add_argument("--source", required=True, type=Path, help="Raiz do mod original clonado")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "mods.json").read_text(encoding="utf-8"))
    if args.mod not in {mod["slug"] for mod in manifest["mods"]}:
        parser.error("Mod não cadastrado em mods.json")
    count, errors = check(ROOT / "mods" / args.mod, args.source)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        sys.exit(f"Falha: {len(errors)} problema(s)")
    print(f"Tradução verificada: {count} chaves, marcadores e quebras de linha correspondentes")


if __name__ == "__main__":
    main()
