# Face and Character Library

This is the draft data contract for fictional adult faces and character packs that can anchor future image and video work.

## Scope

- `HLF-0001` style codes identify a face identity record.
- `HLC-0001` style codes identify a styled character pack that points to one face.
- Every record is synthetic and represents a fictional adult. The minimum apparent age is 25.
- A face record describes identity and default styling. A character pack may override hair, makeup, build, and expression without changing the face identity.
- Reference images, prompts, and video briefs are added only after the pilot has passed the review gates. Draft records are not public catalog entries.

## Safety and review gates

Before a record can be published it needs: prompt linting, a celebrity-similarity screen, an age screen, duplicate-face screening, a manual review by someone other than the creator, and a complete reference set generated with one model version.

The library does not accept real-person uploads, face swaps, impersonation, sexual content, or characters presented as real people. A removed code is retired permanently.

## Repository layout

```text
content/characters/
  schema/face-record.schema.json
  schema/character-pack.schema.json
  pilot/faces.json
  pilot/packs.json
```

The pilot manifest intentionally contains draft records without public images. Generated reference images and private prompts stay in the existing R2 workflow until review is complete.

Run the lightweight contract check with:

```bash
python scripts/validate_character_library.py
```

