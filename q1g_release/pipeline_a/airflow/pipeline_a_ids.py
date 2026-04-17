"""Example stable identifiers for pipeline A runs."""

import hashlib


def run_fingerprint(dag_id: str, logical_date_iso: str) -> str:
    """Return a short hex fingerprint for a DAG run key (example only)."""
    raw = f"{dag_id}|{logical_date_iso}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:12]
