"""Example id helpers for pipeline B."""


def airflow_dag_id(env: str) -> str:
    """Build a simple DAG id for an environment name."""
    return f"pipeline_b_{env.strip().lower()}"
