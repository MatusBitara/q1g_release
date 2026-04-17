"""Example helpers for pipeline A paths."""

from pathlib import Path


def default_dag_folder() -> Path:
    """Return a conventional Airflow DAGs directory path (example only)."""
    return Path(__file__).resolve().parent / "dags"
