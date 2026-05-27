from difflib import get_close_matches


def suggest_command(user_input: str, commands: list[str], n: int = 3) -> list[str]:
    """Return up to n closest command matches (use difflib.get_close_matches)."""
    normalized = user_input.strip().lower()
    if not normalized:
        return []
    return get_close_matches(normalized, commands, n=n, cutoff=0.4)
