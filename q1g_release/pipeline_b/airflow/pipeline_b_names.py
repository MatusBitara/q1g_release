"""Example name normalization for pipeline B."""


def normalize_task_id(raw: str) -> str:
    """Return a simple normalized task id (example only)."""
    return "_".join(raw.strip().lower().split())
