def alternating_characters(s):
    if not (1 <= len(s) <= 10**5):
        raise ValueError("String length must be between 1 and 10^5")
    if not all(c in 'AB' for c in s):
        raise ValueError("String must contain only A and B")
    
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
    
    return deletions