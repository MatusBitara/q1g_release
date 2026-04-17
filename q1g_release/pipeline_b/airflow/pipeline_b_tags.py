"""Example tag formatting for pipeline B."""


def format_image_tag(repository: str, tag: str) -> str:
    """Join repository and tag into a single image reference string."""
    return f"{repository}:{tag}"
