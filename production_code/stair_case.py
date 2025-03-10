def staircase(n, display):
    if not (0 < n <= 30):
        raise ValueError("n must be between 1 and 30")
    result = []
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        chars = display * i
        result.append(spaces + chars)
    return "\n".join(result)