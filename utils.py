def validate_numbers(*args):
    """Validate that all arguments are numeric."""
    for arg in args:
        if not isinstance(arg, (int, float)):
            return False
    return True.

def format_result(result):
    """Format the result for display."""
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result