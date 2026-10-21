"""Validate the public index with the published manager contract."""

from pathlib import Path

from bazaar_contrib_manager.contracts import IndexDocument

document = IndexDocument.model_validate_json(Path("index.json").read_bytes())
print(f"Validated {len(document.contribs)} contrib entries")
