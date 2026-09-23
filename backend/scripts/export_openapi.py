from __future__ import annotations

import argparse
import json
from pathlib import Path

from icibina.main import app


def main() -> None:
    parser = argparse.ArgumentParser(description="Export the ICIBINA OpenAPI document")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "openapi.json",
    )
    args = parser.parse_args()
    args.output.write_text(
        json.dumps(app.openapi(), indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"OpenAPI exported to {args.output}")


if __name__ == "__main__":
    main()
