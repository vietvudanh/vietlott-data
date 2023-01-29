"""helpers for formatting"""


def format_shorten_dict(self, dict):
    """format a dict with shortened keys"""
    return {k: v[:200] if type(v) == str else v for k, v in dict.items() if len(k) < 10}
