"""Validate the draft face/character library contract without external dependencies."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FACES = ROOT / "content" / "characters" / "pilot" / "faces.json"
PACKS = ROOT / "content" / "characters" / "pilot" / "packs.json"


def load(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    faces = load(FACES)
    packs = load(PACKS)
    assert faces["status"] == "draft"
    assert packs["status"] == "draft"
    assert len(faces["required_reference_slots"]) == 14
    face_codes = [record["hlf_code"] for record in faces["records"]]
    pack_codes = [record["hlc_code"] for record in packs["records"]]
    assert len(face_codes) == len(set(face_codes))
    assert len(pack_codes) == len(set(pack_codes))
    for code in face_codes:
        assert re.fullmatch(r"HLF-[0-9]{4}", code)
    for code in pack_codes:
        assert re.fullmatch(r"HLC-[0-9]{4}", code)
    for record in faces["records"]:
        assert record["is_synthetic"] is True
        assert 25 <= record["apparent_age"] <= 75
    print(f"face_records={len(face_codes)} character_packs={len(pack_codes)} status=draft")


if __name__ == "__main__":
    main()
