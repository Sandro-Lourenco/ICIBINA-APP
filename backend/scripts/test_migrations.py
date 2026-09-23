from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from test_support.database import IntegrationDatabaseSettings  # noqa: E402


def run_alembic(*arguments: str, environment: dict[str, str]) -> None:
    subprocess.run(
        [sys.executable, "-m", "alembic", *arguments],
        cwd=BACKEND_ROOT,
        env=environment,
        check=True,
    )


def main() -> None:
    settings = IntegrationDatabaseSettings()  # type: ignore[call-arg]
    environment = os.environ.copy()
    environment["DATABASE_URL"] = settings.test_database_url.get_secret_value()
    environment["DATABASE_MIGRATION_URL"] = settings.test_database_migration_url.get_secret_value()

    run_alembic("downgrade", "base", environment=environment)
    run_alembic("upgrade", "head", environment=environment)
    run_alembic("current", environment=environment)
    run_alembic("heads", environment=environment)
    run_alembic("check", environment=environment)
    print("migration-test: clean *_test database upgraded to head without drift")


if __name__ == "__main__":
    main()
